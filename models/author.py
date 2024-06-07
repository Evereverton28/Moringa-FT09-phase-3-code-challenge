from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.save_to_db()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be of type int")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be of type str")
        if len(value) == 0:
            raise ValueError("name must be longer than 0 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the author is instantiated")
        self._name = value

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Author(row['id'], row['name'])
        return None
