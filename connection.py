import psycopg2
import configparser


def get_connection():
    config = configparser.ConfigParser()
    config.read("config.properties")

    database_name = config.get("database", "database")
    database_user = config.get("database", "user")
    database_password = config.get("database", "password")
    database_host = config.get("database", "host")
    database_port = config.get("database", "port")

    conn = psycopg2.connect(
        database=database_name,
        user=database_user,
        password=database_password,
        host=database_host,
        port=database_port,
    )
    return conn
