import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host=os.getenv("DM_HOST"),
            database=os.getenv("DM-NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DM_PASSWORD"),
            port=os.getenv("DB_PORT")
        )