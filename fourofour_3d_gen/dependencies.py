import subprocess
import sys


DEPENDENCIES = (
    "numpy",
    "pydantic",
    "websocket-client",
    "mixpanel",
)


def installed() -> bool:
    try:
        import numpy
        import pydantic
        import websocket
        import mixpanel

        return True
    except:
        return False


def install() -> None:
    python_exe = sys.executable
    subprocess.check_output([python_exe, "-m", "ensurepip"])
    subprocess.check_output([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    for dep in DEPENDENCIES:
        print(f"Installing {dep}")
        subprocess.check_output([python_exe, "-m", "pip", "install", dep])
