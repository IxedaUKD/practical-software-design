import sqlite3
from contextlib import closing

def create_tables():
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as cursor:
            # Створення таблиці для статей
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')
            connection.commit()

def add_article(title, content):
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO articles (title, content) VALUES (?, ?)
            ''', (title, content))
            connection.commit()

def view_articles():
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('''
                SELECT id, title, content FROM articles
            ''')
            articles = cursor.fetchall()
            for article in articles:
                print(f"ID: {article[0]}, Title: {article[1]}, Content: {article[2]}")

def delete_article(article_id):
    with closing(sqlite3.connect("articles.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('''
                DELETE FROM articles WHERE id = ?
            ''', (article_id,))
            connection.commit()

def main():
    create_tables()
    while True:
        print("1. Add article")
        print("2. View articles")
        print("3. Delete article")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            add_article(title, content)
        elif choice == "2":
            view_articles()
        elif choice == "3":
            article_id = int(input("Enter article ID to delete: "))
            delete_article(article_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()