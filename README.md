# Keylogger with Key Generation and Decryption

## Project Overview

This project implements a **keylogger** to capture keystrokes, **generates an encryption key** for secure storage, and provides the ability to **decrypt** the logged keystrokes. The project consists of three main components:

1. **Keylogger**: Captures and stores keystrokes in a file.
2. **Key Generation**: Generates an encryption key for securing the captured keystrokes.
3. **Decryption**: Decrypts the encrypted log file using the generated key.

### Disclaimer
This project is meant **for educational purposes only**. Unauthorized usage of keyloggers to capture and store private information without consent is illegal and unethical. Always ensure you have proper permission to conduct such activities.

---

## Features

- **Capture Keystrokes**: Logs every keystroke made by the user.
- **Secure Logging**: Encrypts the keystroke logs using a generated key file.
- **Decryption**: Allows you to decrypt the log file to view the captured keystrokes.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/keylogger-project.git
   cd keylogger-project
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The dependencies include:
   - `pynput`: To capture keyboard inputs.
   - `cryptography`: To handle encryption and decryption.

---

## Usage

### 1. Running the Keylogger
   The keylogger script will start capturing keystrokes and log them to a file.
   
   ```bash
   python keylogger.py
   ```

   The keystrokes will be logged in an encrypted file (e.g., `logfile.txt`).

### 2. Generating the Encryption Key
   Generate a new encryption key that will be used to encrypt the keystrokes.

   ```bash
   python generate_key.py
   ```

   This will generate a key file named `key.key`. Store this key in a safe place as it is required for decrypting the log file.

### 3. Decrypting the Log File
   To view the captured keystrokes, use the key to decrypt the log file.

   ```bash
   python decrypt_log.py --key key.key --log logfile.txt
   ```

   This will output the decrypted keystrokes to the terminal or to a specified file.

---

## File Structure

```bash
keylogger-project/
│
├── keylogger.py        # Main keylogger script
├── generate_key.py     # Script to generate encryption key
├── decrypt_log.py      # Script to decrypt log file using key
├── requirements.txt    # Required dependencies
└── README.md           # Project documentation (this file)
```

---

## How It Works

1. **Keylogger**: 
   - Uses the `pynput` library to capture keyboard inputs and logs them to a file.
   - The captured keystrokes are stored in an encrypted format using the `cryptography` library.

2. **Key Generation**:
   - A symmetric encryption key is generated and saved to a file (`key.key`).
   - The key is used to encrypt and decrypt the keystroke logs.

3. **Decryption**:
   - The `decrypt_log.py` script reads the encrypted log file and decrypts it using the key stored in `key.key`.
   - The decrypted output is then displayed in a readable format.

---

## Dependencies

Ensure you have the following Python packages installed (or use the `requirements.txt`):
- `pynput`
- `cryptography`

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

## Ethical Use

Please use this keylogger responsibly and only on systems where you have permission. Unauthorized surveillance or logging of keystrokes on devices you do not own or without explicit permission may result in legal consequences.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or contributions, please contact **Yash Tiwari** via [email](mailto:yashtiw2002@gmail.com).
