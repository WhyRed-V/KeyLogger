
# Keylogger and Data Encryption Project

## Overview

This project consists of a keylogger that collects various system data, including keystrokes, system information, audio, and screenshots. The collected data is encrypted using the `Fernet` encryption algorithm and can be decrypted later using the same encryption key. Additionally, there is functionality to generate a new encryption key if needed.

## Files

### 1. `keylogger.py`
This script captures the following information:
- **System Information**: Processor, OS, machine info, IP addresses.
- **Keystrokes**: Logs all keys pressed by the user.
- **Audio Recording**: Records a 10-second audio clip from the microphone.
- **Screenshots**: Captures a screenshot of the user’s screen.
- **Clipboard Data**: Retrieves and logs any copied text.

After collecting this data, it encrypts the files using a `Fernet` key and saves the encrypted files.

### 2. `GenerateFile.py`
This script generates a new encryption key and stores it in a file named `encryption_key.txt`. The key is essential for both encrypting and decrypting the data.

### 3. `decrypter.py`
This script decrypts the encrypted files generated by `keylogger.py`. It uses the same `Fernet` key for decryption and restores the original data, including:
- System information
- Audio recording
- Screenshots
- Key log

## Setup

### Prerequisites
- Python 3.x
- Required Libraries (install via `pip`):
  - `cryptography`
  - `pynput`
  - `sounddevice`
  - `scipy`
  - `PIL` (Pillow)
  - `requests`

Install the libraries with:
```bash
pip install cryptography pynput sounddevice scipy Pillow requests
```

### Usage

1. **Generate a New Encryption Key (Optional)**
   If you want to generate a new encryption key, run the `GenerateFile.py` script:
   ```bash
   python GenerateFile.py
   ```
   The key will be saved in `encryption_key.txt`.

2. **Run the Keylogger**
   Run the `keylogger.py` script to start logging and encrypting data:
   ```bash
   python keylogger.py
   ```

3. **Decrypt the Encrypted Data**
   After collecting the data, you can decrypt it using the `decrypter.py` script:
   ```bash
   python decrypter.py
   ```

## Security Considerations

- Ensure the `Fernet` key is securely stored and not shared publicly. The same key is required for both encryption and decryption.
- Be mindful of legal and ethical guidelines when using keyloggers, as capturing sensitive information without consent is illegal in many jurisdictions.

## License

This project is intended for educational purposes. Please ensure that you comply with local laws and regulations regarding data collection and privacy.
