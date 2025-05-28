"""
    Содержит классы для работы DB
    UserS - Запросы связанные с пользователями
    Documents - Запроссы связанные с документами
"""

import os
import datetime
import sqlite3

DB_CONFIG = {
    'login': "admin",
    'passvord': "admin",
    'host': "192.168.1.14",
    'port': 5432,
    'dbname': 'postgres'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_connection():
    """
        Создает и возвращает соединение с базой данных
    """
    db_path = os.path.join(BASE_DIR, "db", "db.db").replace("app/", "")

    if not os.path.exists(db_path):
        return None

    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        return e


class BaseModel:
    """
        Базовый класс для запросов
    """

    def __init__(self):
        pass

    def execute_query(self, query, params=None, fetch=False):
        """
            Универсальный метод выполнения запросов
        """
        conn = get_connection()
        if not conn:
            return None

        try:
            cur = conn.cursor()
            cur.execute(query, params or ())

            if fetch:
                result = cur.fetchall()
            else:
                result = True

            conn.commit()
            return result

        except sqlite3.Error as e:
            return e
        finally:
            if not fetch:
                conn.close()


class UserS(BaseModel):
    """
        Делает заапросы связанные с Пользоватилями
    """

    def __init__(self):
        super().__init__()

    def get_users(self):
        """
            Возврашает списак всех пользоваитлей
        """

        query = """
                    SELECT * FROM users;
                """
        res = self.execute_query(query, fetch=True)
        return reversed(list(res))

    def create_user(self,
                    login: str,
                    password_hash: str,
                    user_name: str,
                    role: str):
        """
            Отвечает за создание новаго пользоватиля.
        """

        created_at = str(datetime.datetime.now().strftime("%d.%m.%Y"))

        query = """
        INSERT INTO users (login, password_hash, username, "role", created_at)
        VALUES(?, ?, ?, ?, ?)
        """
        params = (
            login,
            password_hash,
            user_name,
            role,
            created_at
        )

        self.execute_query(query, params)

    def get_username_by_id(self, id: str):
        """
            Возврашает имя пользоватиля по ID.
        """
        query = """
                SELECT username
                FROM users
                WHERE id = ?
                """
        params = (id,)
        return self.execute_query(query, params, True)[0]["username"]

    def get_role_by_id(self, id):
        """
            Возврашает роль пользоватиля по ID.
        """
        query = """
                SELECT role
                FROM users
                WHERE id = ?
                """
        params = (id,)
        return self.execute_query(query, params, True)[0]["role"]

    def update_user(self,
                    id: str,
                    login: str,
                    password_hash: str,
                    user_name: str,
                    role: str):
        query = """
            UPDATE users
            SET login=?, password_hash=?, username=?, "role"=?'
            WHERE id=?
        """
        params = (login, password_hash, user_name, role, id)
        return self.execute_query(query, params)

    def user_loging(self, login: str, password: str):
        """
            Проверяет авторизацию
        """
        query = """
            SELECT id, role
            FROM users
            WHERE login = ? and password_hash = ?
            """
        params = (login, password)
        return dict(self.execute_query(query, params, True))


class Documents(BaseModel):
    """
        Отвечает за работу с таблицей Документы
    """

    def __init__(self):
        super().__init__()

    def get_documents(self) -> list:
        """
            Возвращает список всех документов из базы данных
        """

        query = """
        SELECT id, title, content, author_id, created_at
        FROM documents;
        """
        return reversed(self.execute_query(query, fetch=True))

    def create_documents(self, title: str, content: bytes, auter_id: int):
        """
            Добавляет новый Документов
        """
        created_at = str(datetime.datetime.now().strftime("%d.%m.%Y - %H:%M"))
        query = """
                INSERT INTO documents (title, content, author_id, created_at)
                VALUES(?, ?, ?, ?);
                """
        params = (title, content, auter_id, created_at)
        return self.execute_query(query, params)

    def get_documents_by_author_id(self, author_id: str):
        """
            Возврашает списак всех файлов ID пользоватиля
        """
        query = """
        SELECT id, title, content, author_id, created_at
        FROM documents
        WHERE author_id = ?;
        """
        params = (author_id,)

        return self.execute_query(query, params, fetch=True)

    def get_documents_by_username(self, user_name: str):
        """
            Возврашает списак всех файлов User_name пользоватиля
        """
        query = """
                SELECT id, title, content, author_id, created_at
                FROM documents
                WHERE author_id = (SELECT id
                                   FROM users
                                   WHERE LOWER(username) LIKE LOWER(?))
                """
        params = (f"%{user_name}%",)
        return self.execute_query(query, params, True)

    def get_documents_by_title(self, document_name: str):
        """
            Возврашает файл по названию
        """

        query = """
                SELECT id, title, content, author_id, created_at
                FROM documents
                WHERE title LIKE ?
                """
        params = (f"%{document_name}%",)
        return self.execute_query(query, params, True)

    def get_documests_date(self, data: str):
        """
            Возвращает файлы по дате создание
        """
        query = """
        SELECT id, title, content, author_id, created_at
        FROM documents
        WHERE created_at  LIKE ?
        """
        params = (f"{data}%",)
        return self.execute_query(query, params, True)

    def get_documents_by_id(self, document_id: int):
        """
            Возврашает файл по названию
        """

        query = """
                SELECT id, title, content, author_id, created_at
                FROM documents
                WHERE id = ?
                """
        params = (document_id,)
        return self.execute_query(query, params, True)

    def remove_delite_by_id(self, document_id):
        """
            Удоляет документ по id
        """
        query = """
                DELETE FROM documents WHERE id=?
                """
        params = (document_id,)
        return self.execute_query(query, params, True)


class Templates(BaseModel):
    """
        Отвечает за работу с таблицей Шаблоны
    """

    def __init__(self):
        super().__init__()

    def create_templates(self, file_name, counter, author_id):
        """
            Добавляет новый шаблон
        """
        query = """
                    INSERT INTO templates (name, content, author_id)
                    VALUES(?, ?, ?);
                """
        params = (file_name, counter, author_id)
        return self.execute_query(query, params)

    def get_templates(self):
        """
            Возврашает списак всех шаблонов
        """
        query = """
                SELECT id, name, content, author_id FROM templates;
                """
        return reversed(self.execute_query(query, fetch=True))

    def get_templates_by_name(self, name: str):
        """
            Возврашает списак шаблонов по названиям
        """
        query = """
        SELECT id, name, content, author_id
        FROM templates
        WHERE name LIKE ?
        """
        params = (f"%{name}%",)
        return self.execute_query(query, params, fetch=True)

    def get_templates_by_id(self, id: str):
        """
            Возврашает списак шаблонов по id
        """
        query = """
        SELECT id, name, content, author_id
        FROM templates
        WHERE id = ?
        """
        params = (id,)
        return self.execute_query(query, params, fetch=True)

    def get_templates_remove_by_id(self, id: str):
        """
            Удоляет шаблон по id
        """
        query = """
        DELETE FROM templates WHERE id=?;
        """
        params = (id,)
        return self.execute_query(query, params, fetch=True)
