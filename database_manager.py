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


def create_tables(con: sqlite3.Connection) -> None:

    """
    :param con: Соединение
    :return: None
    """

    cursor_obj = con.cursor()
