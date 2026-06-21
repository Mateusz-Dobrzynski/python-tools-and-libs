from sqlalchemy import create_engine

user = "root"
password = "root"
host = "127.0.0.1"
port = 3306
database = "fridge"


def get_connection():
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    return engine
