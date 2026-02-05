#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Installation complete."
echo "Run the GUI with:"
echo "  source .venv/bin/activate && python gui_app.py"
