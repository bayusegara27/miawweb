import os
from flask import Flask, request, render_template, redirect, url_for, session
from expert_system import ExpertSystem
import bcrypt
import mysql.connector
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
system = ExpertSystem()

# Get environment variables from GitHub Secrets
db_config = {
    'MYSQL_HOST': os.getenv('MYSQL_HOST'),
    'MYSQL_PORT': int(os.getenv('MYSQL_PORT', 3306)),  # Default to 3306 if not set
    'MYSQL_USER': os.getenv('MYSQL_USER'),
    'MYSQL_PASSWORD': os.getenv('MYSQL_PASSWORD'),
    'MYSQL_DB': os.getenv('MYSQL_DB')
}

# Function to get a database connection using mysql-connector-python
def get_db_connection():
    return mysql.connector.connect(
        host=db_config['MYSQL_HOST'],
        port=db_config['MYSQL_PORT'],
        user=db_config['MYSQL_USER'],
        password=db_config['MYSQL_PASSWORD'],
        database=db_config['MYSQL_DB']
    )

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'secretkey')

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v2/',
    client_kwargs={
        'scope': 'openid email profile'
    },
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            stored_password = user[3]  # Index 3 is the password column
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                session['user_id'] = user[0]
                session['email'] = user[2]
                session['type'] = user[4]

                if session['type'] == 3:
                    return redirect('/home-admin')
                else:
                    return redirect('/home')
            else:
                return "Password incorrect", 400
        else:
            return "Email not found", 400

    return render_template('login.html')

@app.route('/login/google')
def login_google():
    redirect_uri = 'https://ayamsuwir.azurewebsites.net/login/google/callback'
    return google.authorize_redirect(redirect_uri)

@app.route('/login/google/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()

    # Check if user exists in database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (user_info['email'],))
    user = cursor.fetchone()

    if not user:
        # Register the user if not exists
        cursor.execute(
            "INSERT INTO users (name, email, password, type) VALUES (%s, %s, %s, %s)",
            (user_info['name'], user_info['email'], '', 1)  # Default type = 1 (Free)
        )
        connection.commit()
        cursor.execute("SELECT * FROM users WHERE email = %s", (user_info['email'],))
        user = cursor.fetchone()

    cursor.close()
    connection.close()

    # Log the user in
    session['user_id'] = user[0]
    session['email'] = user[2]
    session['type'] = user[4]

    return redirect('/home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        password_repeat = request.form['password_repeat']

        if password != password_repeat:
            return "Password does not match, please try again.", 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                           (name, email, hashed_password))
            connection.commit()
            cursor.close()
            connection.close()

            return redirect(url_for('login'))
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template('register.html')

@app.route('/dok')
def dok():
    if 'type' not in session:
        return redirect(url_for('login'))

    user_type = session['type']
    if user_type == 1:
        return redirect('/free')
    elif user_type == 2:
        return redirect('/prem')
    else:
        return redirect('/error.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('home.html', email=session.get('email'), user_type=session.get('type'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cek')
def cek():
    return render_template('cek.html')

@app.route("/diagnose", methods=["POST"])
def diagnose():
    symptoms_input = request.form.get("symptoms")
    user_symptoms = symptoms_input.split(", ")
    return render_diagnosis(system, user_symptoms)

def render_diagnosis(system, user_symptoms):
    possible_diseases = []
    for code, disease in system.diseases_rules.items():
        matched_symptoms = [symptom for symptom in disease["symptoms"] if symptom in user_symptoms]
        if len(matched_symptoms) == len(disease["symptoms"]) or len(matched_symptoms) >= 2:
            possible_diseases.append((disease["name"], disease, len(matched_symptoms)))

    possible_diseases.sort(key=lambda x: x[2], reverse=True)
    return render_template("hasil.html", possible_diseases=possible_diseases)

@app.route("/free")
def free():
    if 'type' not in session or session['type'] not in [1, 3]:
        return redirect('/home')
    return render_template("free.html")

@app.route("/prem")
def prem():
    if 'type' not in session or session['type'] not in [2, 3]:  # 2 = Premium, 3 = Admin
        return redirect('/free')  # Arahkan ke halaman free jika bukan premium atau admin
    return render_template("prem.html")

@app.route("/home-admin")
def homeadmin():
    if 'type' not in session or session['type'] not in [3]:
        return redirect('/home')
    return render_template("home-admin.html")

@app.route('/akun')
def akun():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, type, password FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if not user:
        return "User not found", 404

    name = user[0]
    user_type = "Free" if user[1] == 1 else "Premium"
    has_password = True if user[2] else False  # Check if password is set

    return render_template('akun.html', name=name, user_type=user_type, has_password=has_password)

@app.route('/set_password', methods=['POST'])
def set_password():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    password = request.form['password']

    # Hash the password before saving it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('akun'))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' not in session or session.get('type') != 3:
        return "Access Denied", 403

    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_type = request.form.get('type')

        cursor.execute("UPDATE users SET type = %s WHERE id = %s", (new_type, user_id))
        connection.commit()

    cursor.execute("SELECT id, name, email, type FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('admin.html', users=users)

@app.route("/pay")
def pay():
    return render_template("pay.html")

@app.route("/tim")
def tim():
    return render_template("tim.html")

if __name__ == "__main__":
    app.run(debug=True)
