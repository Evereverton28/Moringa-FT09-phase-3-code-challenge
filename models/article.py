class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __str__(self):
        return self.title
    
    @staticmethod
    def create(cursor, title, content, author_id, magazine_id):
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (title, content, author_id, magazine_id))
        return cursor.lastrowid

    @staticmethod
    def get_by_id(cursor, id):
        cursor.execute('SELECT * FROM articles WHERE id = ?', (id,))
        row = cursor.fetchone()
        return Article(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) if row else None
