#! /bin/bash

# 現在のディレクトリに移動
cd frontend
echo "Moved to frontend directory"

# アプリケーションを起動
echo "Starting the frontend application ..."
if ! npm run dev
then
    echo "Failed to start the application"
    exit 1
fi

# フロントエンドアプリケーションが起動したことを表示
echo "Frontend application started"