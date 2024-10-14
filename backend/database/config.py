import os


# 環境変数から設定を取得する場合
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_URL = f"mysql+pymysql://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE_NAME}"


class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
