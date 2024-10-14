#!/bin/bash

python3 -m venv backend/venv
pip install -r backend/requirements.txt
source backend/venv/bin/activate
python3 backend/main.py
