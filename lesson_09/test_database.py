from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = (
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres")
db = create_engine(db_connection_string)


# фикстура для создания таблицы
def prepare_clean_table():
    with db.connect() as connection:
        connection.execute(text(
            "CREATE TABLE IF NOT EXISTS students ("
            "id SERIAL PRIMARY KEY, name VARCHAR(50));"))
        connection.execute(text("TRUNCATE TABLE students RESTART IDENTITY;"))
        connection.commit()  # Обязательно сохраняем изменения


# добавление студента
def test_add_student():
    prepare_clean_table()

    with db.connect() as connection:
        connection.execute(text(
            "INSERT INTO students (name) VALUES ('Сидоров Иван')"))
        connection.commit()

        result = connection.execute(text(
            "SELECT name FROM students WHERE id = 1")).fetchone()

        assert result is not None
        assert result[0] == 'Сидоров Иван'


# Изменение студента
def test_update_student():
    prepare_clean_table()

    with db.connect() as connection:
        connection.execute(text(
            "INSERT INTO students (name) VALUES ('Сидоров Иван')"))
        connection.commit()

        connection.execute(text(
            "UPDATE students SET name = 'Сидоров Иван Петрович' WHERE id = 1"))

        result = connection.execute(text(
            "SELECT name FROM students WHERE id = 1")).fetchone()

        assert result is not None
        assert result[0] == 'Сидоров Иван Петрович'


# удаление студента
def test_delete_student():
    prepare_clean_table()

    with db.connect() as connection:
        connection.execute(text(
            "INSERT INTO students (name) VALUES ('Сидоров Иван')"))
        connection.commit()

        connection.execute(text("DELETE FROM students WHERE id = 1"))
        connection.commit()

        connection.execute(text("SELECT name FROM students WHERE id = 1"))

        result = connection.execute(text(
            "SELECT name FROM students WHERE id = 1")).fetchone()

        assert result is None
