import random
import sqlite3
from sqlite3 import Error


def sql_connection() -> sqlite3.Connection | ConnectionError:

    try:
        con = sqlite3.connect("TasksBase.db")
        con.execute("PRAGMA foreign_keys = ON")
        return con
    except Error:
        print("Произошла неожиданная ошибка", Error)


def create_tables(con: sqlite3.Connection, table_name: str, column_names: list, data_types: list) -> None:

    """
    :param con: Соединение
    :param table_name: Имя таблицы
    :param column_names: Столбцы
    :param data_types: Типы
    :return: None
    """
    cursor_obj = con.cursor()
    column_definitions = ', '.join([f"{column_name} {data_type}" for column_name, data_type in zip(column_names, data_types)])
    cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY AUTOINCREMENT, {column_definitions})")