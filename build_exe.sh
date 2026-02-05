#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

pyinstaller --onefile --windowed --name "RussianTextAnalyzer" gui_app.py

echo "Готово. Файл находится в папке dist/RussianTextAnalyzer"
