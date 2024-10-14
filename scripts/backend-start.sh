#!/bin/bash

# 古い仮想環境を削除
rm -rf backend/venv
echo "Old virtual environment removed"

# 仮装環境を作成
python3 -m venv backend/venv
echo "Virtual environment created"

# ディレクトリに移動
cd backend

# 仮想環境をアクティブにする
echo "Creating virtual environment ..."
source venv/bin/activate

# 必要なライブラリをインストール
echo "Installing requirements ..."
pip install -r requirements.txt

# アプリケーションを起動
echo "Starting the application ..."
if ! python3 main.py
then
    echo "Failed to start the application"
    exit 1
fi

# バックエンドアプリケーションが起動したことを表示
echo "Backend application started"
