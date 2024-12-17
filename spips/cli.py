# spips/cli.py

import sys
import os

def generate_structure():
    # Direktori yang perlu dibuat
    directories = [
        "database",
        "models",
        "routes",
        "views",
        "app",
    ]

    # Membuat direktori
    for dir_name in directories:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"Dibuat direktori: {dir_name}")
        else:
            print(f"Direktori {dir_name} sudah ada.")

    # Membuat file template untuk database dan model
    with open("database/database.data.spips", "w") as f:
        f.write("# Database configuration\n")
        f.write("host = 'localhost'\n")
        f.write("port = 5432\n")
        f.write("username = 'root'\n")
        f.write("password = 'password'\n")
        f.write("database = 'spips_db'\n")
    print("Created 'database.data.spips'")

    with open("models/model.py", "w") as f:
        f.write("# Model definition for SPIPS\n")
        f.write("class Model:\n")
        f.write("    def __init__(self, name):\n")
        f.write("        self.name = name\n")
        f.write("\n")
        f.write("    def save(self):\n")
        f.write("        # Logic untuk menyimpan model ke database\n")
        f.write("        pass\n")
    print("Created 'model.py'")

    with open("routes/route.py", "w") as f:
        f.write("# Routes for SPIPS\n")
        f.write("def home():\n")
        f.write("    # Logic untuk route '/'\n")
        f.write("    print('Welcome to SPIPS!')\n")
    print("Created 'route.py'")

    with open("views/welcome.part.spips", "w") as f:
        f.write("# Welcome view template for SPIPS\n")
        f.write("{{ welcome_message }}\n")
    print("Created 'welcome.part.spips'")

    with open("app.py", "w") as f:
        f.write("# Main application for SPIPS\n")
        f.write("from routes import home\n")
        f.write("\n")
        f.write("def main():\n")
        f.write("    home()\n")
        f.write("\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")
    print("Created 'app.py'")

def version():
    print("SPIPS versi 0.2.0")

def main():
    if len(sys.argv) < 2:
        print("Gunakan perintah: spips <command>")
        return

    command = sys.argv[1].lower()  # Mengonversi perintah menjadi lowercase
    if command == "generate": # artisan
        generate_structure()
    elif command == "version":
        version()
    else:
        print(f"Perintah '{command}' tidak dikenal.")

if __name__ == '__main__':
    main()