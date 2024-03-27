import os
import requests
from zipfile import ZipFile
import urllib.parse
import ctypes
from download import fileURL
import hashlib

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("4.4.2 Launcher Installer v1.2")


def download_and_extract(url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    parsed_url = urllib.parse.urlparse(url)
    file_name = os.path.join(destination_folder, os.path.basename(parsed_url.path))

    response = requests.get(url)
    with open(file_name, "wb") as zip_file:
        zip_file.write(response.content)

    with ZipFile(file_name, "r") as zip_ref:
        zip_ref.extractall(destination_folder)

    os.remove(file_name)

def check_dbd_path(destination_folder):
    dbd_path = os.path.join(destination_folder, "DeadByDaylight.exe")
    return os.path.exists(dbd_path)

def get_path():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[MESSAGE] Enter the path to your DbD 4.4.2 root folder:")
        dbd_path = input("[INPUT] - ")

        dbd_exe_path = os.path.join(dbd_path, "DeadByDaylight.exe")
        if not os.path.exists(dbd_exe_path):
            print("[ERROR] DbD root folder was not found.")
            input("[MESSAGE] Press ENTER to continue...")
        else:
            expected_hash = "A071830466701D8FABEAC2DDF88A70DD"
            md5_hash = compute_md5(dbd_exe_path)
            if md5_hash.lower() != expected_hash.lower():
                print("[ERROR] Wrong DbD version was entered.")
                input("[MESSAGE] Press ENTER to continue...")
            else:
                return dbd_path
        
def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096) , b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == "__main__":
    download_url = fileURL
    
    DbD_path = get_path()
    
    print("[MESSAGE] Installing files...")
    download_and_extract(download_url, DbD_path)
    
    print("[SUCCESS] Launcher installed succesfully.")
    input("[MESSAGE] Press ENTER to EXIT...")
    