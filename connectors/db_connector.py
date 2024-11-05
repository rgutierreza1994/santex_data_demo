from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from typing import Generator

schema = "demo_datalake"
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]


connection_uri = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/santex"


engine = create_engine(
    url=connection_uri,
)


def get_session() -> Generator[Session, None, None]:
    global db_session
    if "db_session" not in globals():
        base_session = sessionmaker(bind=engine)
        db_session = base_session()

    yield db_session
