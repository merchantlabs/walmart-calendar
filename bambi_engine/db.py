import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from urllib.parse import quote_plus

load_dotenv(find_dotenv())

def connection(name=os.environ.get("DB_NAME")):

    params = quote_plus("DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={password}".format(
        driver="ODBC Driver 13 for SQL Server",
        server = os.environ.get("DB_HOST"),
        db = name,
        user = os.environ.get("DB_USER"),
        password = os.environ.get("DB_PASS")
    ))

    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    return engine.connect()
