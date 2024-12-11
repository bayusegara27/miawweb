from flask import Flask, request, render_template, redirect, url_for, session
from expert_system import ExpertSystem
import bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)
system = ExpertSystem()

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'  # Ganti dengan nama host MySQL
app.config['MYSQL_USER'] = 'sql12751318'  # Ganti dengan username MySQL
app.config['MYSQL_PASSWORD'] = 'Pbp9b7DqvN'  # Ganti dengan password MySQL
app.config['MYSQL_DB'] = 'sql12751318'  # Ganti dengan nama database MySQL
app.secret_key = 'secretkey'

# Inisialisasi MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        # Ambil data dari form login
        email = request.form['email']
        password = request.form['password']
        
        # Query database untuk memeriksa pengguna berdasarkan email
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()  # Ambil satu hasil pencarian
        
        if user:
            # Verifikasi password dengan hash yang ada di database
            stored_password = user[3]  # Index 3 adalah kolom password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Password cocok, simpan informasi pengguna dalam session
                session['user_id'] = user[0]  # Simpan ID pengguna di session
                session['email'] = user[2]    # Simpan email pengguna di session
                session['type'] = user[4]     # Simpan type pengguna di session
                # Arahkan pengguna berdasarkan type
                if session['type'] == 3:
                    return redirect('/home-admin')  # Arahkan ke halaman admin
                else:
                    return redirect('/home')  # Arahkan ke halaman pengguna biasa
            else:
                return "Password salah", 400  # Password salah
        else:
            return "Email tidak ditemukan", 400  # Email tidak ditemukan

    # Jika GET request, render halaman login
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ambil data dari form
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        password_repeat = request.form['password_repeat']

        # Validasi password dan password repeat
        if password != password_repeat:
            return "Password tidak cocok, silakan coba lagi.", 400

        # Enkripsi password dengan bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            # Menyisipkan data ke database
            cur = mysql.connection.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cur.execute(query, (name, email, hashed_password))
            mysql.connection.commit()  # Simpan perubahan ke database
            cur.close()

            # Redirect setelah berhasil registrasi
            return redirect(url_for('login'))  # Ganti 'login' dengan nama route login Anda

        except Exception as e:
            return f"Terjadi kesalahan: {e}", 500

    # Jika metode GET, render halaman registrasi
    return render_template('register.html')

@app.route('/dok')
def dok():
    if 'type' not in session:
        return redirect(url_for('login'))  # Arahkan ke halaman login jika session tidak ada
    
    user_type = session['type']  # Ambil type dari session
    if user_type == 1:
        return redirect('/free')  # Pengguna dengan type 1 diarahkan ke free.html
    elif user_type == 2:
        return redirect('/prem')  # Pengguna dengan type 2 diarahkan ke prem.html
    else:
        return redirect('/error.html')  # Tangani error jika type tidak valid


@app.route('/home')
def home():
    # Pastikan pengguna sudah login (ada session)
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Jika belum login, arahkan ke login

    # Render halaman home
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
    user_symptoms = symptoms_input.split(", ")  # Memisahkan input gejala
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
    return render_template("free.html")

@app.route("/prem")
def prem():
    return render_template("prem.html")

@app.route("/home-admin")
def homeadmin():
    return render_template("home-admin.html")

@app.route('/akun')
def akun():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Pastikan pengguna login

    user_id = session['user_id']  # Ambil ID pengguna dari session

    # Query database untuk mengambil nama dan type akun
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, type FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()  # Ambil hasil query

    if not user:
        return "User not found", 404

    name = user[0]  # Nama pengguna
    user_type = "Free" if user[1] == 1 else "Premium"  # Tentukan tipe akun

    # Kirim data ke template
    return render_template('akun.html', name=name, user_type=user_type)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Hapus semua data dari session
    return redirect(url_for('login'))  # Arahkan ke halaman login

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # Pastikan hanya admin yang dapat mengakses halaman ini
    if 'user_id' not in session or session.get('type') != 3:  
        return "Access Denied", 403  # Jika bukan admin, akses ditolak

    cur = mysql.connection.cursor()

    # Jika ada perubahan type yang dilakukan admin
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_type = request.form.get('type')

        # Update type akun di database
        cur.execute("UPDATE users SET type = %s WHERE id = %s", (new_type, user_id))
        mysql.connection.commit()

    # Ambil semua akun dari database
    cur.execute("SELECT id, name, email, type FROM users")
    users = cur.fetchall()

    # Kirim data pengguna ke template
    return render_template('admin.html', users=users)

@app.route("/pay")
def pay():
    return render_template("pay.html")

@app.route("/tim")
def tim():
    return render_template("tim.html")


if __name__ == "__main__":
    app.run(debug=True)
