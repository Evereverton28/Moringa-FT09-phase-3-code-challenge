from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    create_tables()

    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    author_id = Author.create(cursor, author_name)
    magazine_id = Magazine.create(cursor, magazine_name, magazine_category)
    article_id = Article.create(cursor, article_title, article_content, author_id, magazine_id)

    conn.commit()

    authors = cursor.execute('SELECT * FROM authors').fetchall()
    magazines = cursor.execute('SELECT * FROM magazines').fetchall()
    articles = cursor.execute('SELECT * FROM articles').fetchall()

    conn.close()

    print("\nAuthors:")
    for author in authors:
        print(Author(author['id'], author['name']))

    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine['id'], magazine['name'], magazine['category']))

    print("\nArticles:")
    for article in articles:
        print(Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']))

if __name__ == "__main__":
    main()
