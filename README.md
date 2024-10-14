# WebSocketを利用したAPI通信の勉強

## 概要

- WebSocket技術のキャッチアップのために開発
- アプリの内容は双方向通信で行うチャットアプリとなっています
- 技術選定理由
  - フロントエンドをNext.jsにしている理由は特になし
  - バックエンドをFlaskにしているのは技術キャッチアップのため

## 使用技術

- 言語・FrameWork
  - FE: React, Next.js, TypeScript, Chakra UI, CSS
  - BE: Python, Flask
- 開発環境
  - Mac

## 環境構築

### frontend編

1. 今後書いていく予定

### backend編

1. ```cp .env.sample .env```のコマンドを実行して、.envファイルを作成する
2. .envファイルに必要な情報を記述する
   - .envファイルは秘匿ファイルを記述するためのファイルです
   - こちらにはローカルの情報を書き、git上には上げないようにしましょう
3. ```python3 -m venv venv```でPythonの仮想環境をプロジェクトディレクトリへ移動させる(環境によっては、```python -m venv venv```で実行できる。alias次第)
4. ```pip install -r requirements.txt```でプロジェクトに必要なパッケージをすべてインストールする
5. ```source venv/bin/activate```で仮想環境の中に入る
6. ```python3 main.py```のコマンドを実行して、Runnning on <http://127.0.0.1:5500>と出れば成功です
