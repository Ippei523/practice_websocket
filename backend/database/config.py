import os
from dotenv import load_dotenv

load_dotenv()


# 環境変数から設定を取得する場合
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_URL = f"postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE_NAME}"


class Config:
    print(f"DATABASE_URL: {DATABASE_URL}")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
