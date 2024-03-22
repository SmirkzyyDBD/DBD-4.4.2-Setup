import os
import requests
from zipfile import ZipFile
import urllib.parse
import ctypes
from url import fileURL

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("4.4.2 Launcher Installer v1.1")


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
        print("[MESSAGE] Enter the path to your 4.4.2 root folder:")
        dbd_path = input("- ")

        if not os.path.exists(os.path.join(dbd_path, 'DeadByDaylight\\Binaries\\Win64\\steam_lobby.exe')):
            print("[ERROR] 4.4.2 root folder was not found.")
            input("[MESSAGE] Press ENTER to continue...")
        else:
            return dbd_path

if __name__ == "__main__":
    download_url = fileURL
    
    DbD_path = get_path()
    
    download_and_extract(download_url, DbD_path)
    
    print("[SUCCESS] Launcher installed succesfully.")
    input("[MESSAGE] Press ENTER to EXIT...")
