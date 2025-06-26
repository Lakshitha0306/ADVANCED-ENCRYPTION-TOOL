import file_crypto

def menu():
    while True:
        print("\n=== AES File Encryption Tool ===")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            file_crypto.generate_key()

        elif choice == '2':
            filename = input("Enter filename to encrypt: ").strip()
            file_crypto.encrypt_file(filename)

        elif choice == '3':
            enc_file = input("Enter encrypted file name (e.g., file.txt.enc): ").strip()
            out_file = input("Enter output file name (e.g., file.txt): ").strip()
            file_crypto.decrypt_file(enc_file, out_file)

        elif choice == '4':
            print("Goodbye.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()