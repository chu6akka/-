python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

pyinstaller --onefile --windowed --name "RussianTextAnalyzer" gui_app.py

Write-Host "Готово. EXE файл находится в папке dist\\RussianTextAnalyzer.exe"
