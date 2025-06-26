from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"[+] {filename} encrypted successfully to {filename}.enc")

def decrypt_file(encrypted_filename, output_filename):
    key = load_key()
    f = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"[+] {encrypted_filename} decrypted successfully to {output_filename}")