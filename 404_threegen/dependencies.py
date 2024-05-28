import subprocess

import sys


DEPENDENCIES = ("numpy", "requests")


def installed() -> bool:
    try:
        import numpy
        import requests

        return True
    except:
        return False


def install() -> None:
    # upgrade pip
    python_exe = sys.executable
    subprocess.check_output([python_exe, "-m", "ensurepip"])
    subprocess.check_output([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    for dep in DEPENDENCIES:
        print(f"Installing {dep}")
        subprocess.check_output([python_exe, "-m", "pip", "install", dep])
