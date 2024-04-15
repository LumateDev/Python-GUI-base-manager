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


def init_db(con):
    create_tables(con)
    init_theme(1, con)
    init_type_task(con)


def create_tables(con: sqlite3.Connection):

    """
    :param con: Соединение
    :return: None
    """

    cursor_obj = con.cursor()
    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS type_task(
    id_type_work INTEGER PRIMARY KEY AUTOINCREMENT,
    type_work VARCHAR(200) NOT NULL
    );""")

    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS theme(
    id_theme INTEGER PRIMARY KEY AUTOINCREMENT,
    theme VARCHAR(500)
    );""")

    cursor_obj.execute("""CREATE TABLE IF NOT EXISTS task(
    id_task INTEGER PRIMARY KEY AUTOINCREMENT,
    id_type_work INTEGER,
    id_theme INTEGER,
    task TEXT NOT NULL,
    level INTEGER,
    FOREIGN KEY (id_type_work) REFERENCES type_task(id_type_work) ON DELETE CASCADE,
    FOREIGN KEY (id_theme) REFERENCES Theme(id_theme) ON DELETE CASCADE
    );""")

    con.commit()
    cursor_obj.close()


def init_theme(number_db, con: sqlite3.Connection):
    cur = con.cursor()
    list_theme = []
    if number_db == 1:
        list_theme = ["Простая программа. Условный оператор",
                      "Операторы цикла",
                      "Обработка последовательности чисел, оканчивающейся маркером",
                      "Обработка последовательности чисел, состоящих из заданного количества элементов",
                      "Обработка элементов последовательности со сложными свойствами",
                      "Однотипная обработка одномерных массивов",
                      "Сложная обработка массивов",
                      "Обработка матриц. Диагонали в квадратной матрицы",
                      "Обработка нескольких матриц. Сложные свойства элементов матриц",
                      "Функции"]
    elif number_db == 2:
        list_theme = ["Обработка строк",
                      "Обработка массивов строк",
                      "Работа со структурами",
                      "Передача массива как параметра в функцию",
                      "Обработка числовых файлов",
                      "Обработка текстовых файлов",
                      "Динамические массивы",
                      "Динамические матрицы",
                      "Обработка неориентированных графов (на основе матрицы смежности)",
                      "Обработка ориентированных графов (на основе матрицы смежности)"]
    else:
        list_theme = ["Линейная динамическая структура данных стек",
                      "Линейная динамическая структура данных очередь",
                      "Однонаправленные линейные списки",
                      "Сложная обработка нескольких однонаправленных списков",
                      "Двунаправленные списки",
                      "Сложная обработка двунаправленных списков. ",
                      "Кольцевые списки",
                      "Рекурсивная обработка списков",
                      "Двоичные деревья",
                      "Обработка нескольких структур данных (список+дерево)"]

    for theme in list_theme:
        cur.execute("INSERT INTO theme (theme) VALUES (?)", (theme,))

    con.commit()
    cur.close()


def init_type_task(con: sqlite3.Connection):
    cur = con.cursor()
    list_type_task = ["Домашняя работа", "Самостоятельная работа", "Контрольная работа"]

    for type_work in list_type_task:
        cur.execute("INSERT INTO type_task (type_work) VALUES (?)", (type_work,))

    con.commit()
    cur.close()


def drop_all_tables(con: sqlite3.Connection):
    cursor_obj = con.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS task;")
    cursor_obj.execute("DROP TABLE IF EXISTS type_task;")
    cursor_obj.execute("DROP TABLE IF EXISTS theme;")
    con.commit()
    cursor_obj.close()
    init_db(con)


def get_all_tasks(con: sqlite3.Connection):
     """
     :param con: Соединение
     :return: Список задач
     """
     cursor_obj = con.cursor()
     cursor_obj.execute("""SELECT * FROM task""")
     tasks = []
     for row in cursor_obj.fetchall():
         tasks.append([row[0], row[1], row[2], row[3], row[4]])
     cursor_obj.close()
     for i in tasks:
         print(i)
     return tasks


def get_task_by_id(con: sqlite3.Connection, id_task: int) -> list:
    """
    :param con: Соединение
    :param id_task: Идентификатор задачи
    :return: Задача
    """
    cursor_obj = con.cursor()
    cursor_obj.execute("""SELECT * FROM task WHERE id_task = ?""", (id_task,))
    task = cursor_obj.fetchone()
    cursor_obj.close()
    return [task[0], task[1], task[2], task[3], task[4]]


def add_task(con: sqlite3.Connection, type_work, id_theme, task, difficult):

    level = 0
    id_type_work = 0
    print(type_work)
    match difficult:
        case "Легко":
            level = 1
        case "Средняя":
            level = 2
        case "Сложная":
            level = 3
        case "Хард":
            level = 4

    match type_work:
        case "Домашнee задание":
            id_type_work = 1
        case "Самостоятельная работа":
            id_type_work = 2
        case "Контрольная работа":
            id_type_work = 3

    print(id_type_work, id_theme, task, level)
    cursor_obj = con.cursor()
    cursor_obj.execute("""INSERT INTO task (id_type_work, id_theme, task, level) 
                            VALUES (?, ?, ?, ?)""",
                       (id_type_work, id_theme, task, level))
    con.commit()
    cursor_obj.close()


def delete_task(con: sqlite3.Connection, id_task: int):
    cursor_obj = con.cursor()
    cursor_obj.execute("""DELETE FROM task WHERE id_task = ?""", (id_task,))
    con.commit()
    cursor_obj.close()


def update_task(con: sqlite3.Connection, id_task, type_work, id_theme, task, difficult):
    level = 0
    id_type_work = 0
    print(type_work)
    match difficult:
        case "Легко":
            level = 1
        case "Средняя":
            level = 2
        case "Сложная":
            level = 3
        case "Хард":
            level = 4

    match type_work:
        case "Домашнee задание":
            id_type_work = 1
        case "Самостоятельная работа":
            id_type_work = 2
        case "Контрольная работа":
            id_type_work = 3

    print(id_type_work, id_theme, task, level)

    cursor_obj = con.cursor()
    cursor_obj.execute("""UPDATE task SET id_type_work = ?, id_theme = ?, task = ?, level = ? 
                            WHERE id_task = ?""",
                       (id_type_work, id_theme, task, level, id_task))
    con.commit()
    cursor_obj.close()
