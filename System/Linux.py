import subprocess
import sys
import os

def check_git_version():
    try:
        git_version = subprocess.check_output(["git", "--version"]).decode("utf-8")
        return git_version
    except Exception as e:
        print("Git is not installed. Installing now...")
        oprendszer = sys.platform
        if oprendszer.startswith('win'):
            print("Please install Git manually from the official website.")
        elif oprendszer.startswith('linux'):
            os.system('sudo apt update')
            os.system('sudo apt install git -y')
        elif oprendszer.startswith('darwin'):
            os.system('brew install git')
        git_version = subprocess.check_output(["git", "--version"]).decode("utf-8")
        return git_version


def check_brew_version():
    try:
        brew_version = subprocess.check_output(["brew", "--version"]).decode("utf-8")
        return brew_version
    except Exception as e:
        print("Git is not installed. Installing now...")
        oprendszer = sys.platform
        if oprendszer.startswith('win'):
            print("Please install Git manually from the official website.")
            pass
        elif oprendszer.startswith('linux'):
            os.system('sudo apt update')
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        elif oprendszer.startswith('darwin'):
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        brew_version = subprocess.check_output(["brew", "--version"]).decode("utf-8")
        return brew_version