import psycopg2
from psycopg2 import sql
from config import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_PORT
)


def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print("Ошибка подключения к базе данных:", e)
        return None


def get_all_documents() -> list:
    conn = get_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cur:

            query = """
            SELECT id, title, content, author_id, created_at
            FROM documents;
            """
            cur.execute(query)
            rows = cur.fetchall()
            return rows
    finally:
        conn.close()


# Тест функции
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Соединение с базой данных успешно!")
        conn.close()

        s = sql
