#!/usr/bin/env python3
"""
Génère les QR codes pour le concours.
Usage :
  python generate_qrs.py https://ton-app.onrender.com
"""
import sys
import json
import qrcode
from pathlib import Path

BASE_DIR = Path(__file__).parent
QR_DIR = BASE_DIR / "qrcodes"
PULLS_FILE = BASE_DIR / "static" / "pulls.json"

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_qrs.py https://ton-domaine.com")
        sys.exit(1)

    base_url = sys.argv[1].rstrip("/")
    QR_DIR.mkdir(exist_ok=True)

    with open(PULLS_FILE, "r", encoding="utf-8") as f:
        pulls = json.load(f)

    for pull in pulls:
        url = f"{base_url}/?id={pull['id']}"
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(QR_DIR / f"{pull['id']}.png")
        print(f"QR généré : {pull['id']} → {url}")

    print(f"\n{len(pulls)} QR codes générés dans {QR_DIR}")

if __name__ == "__main__":
    main()
