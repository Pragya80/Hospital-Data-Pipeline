#This file handles two important tasks:
#1️⃣ Ensures required folders exist
#2️⃣ Prints clean pipeline logs

from pathlib import Path


def ensure_directories():
    directories = ["bronze", "silver", "gold", "visualizations"]

    for directory in directories:
        Path(directory).mkdir(exist_ok=True)

def log(message):
    print(f"[INFO] {message}")