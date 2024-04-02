import random
import sqlite3
from sqlite3 import Error

Drivers_firstName = ['Виктор', 'Андрей', 'Антон', 'Иосиф', 'Дмитрий', 'Артём', 'Григорий', 'Роман', 'Иван', 'Егор', 'Кирилл']
Drivers_lastName = ['Бубликов', 'Грибной', 'Путин', 'Медведев', 'Антонов', 'Гослинг', 'Морозов', 'Федотов', 'Баранов', 'Орлов', 'Осипов']
Drivers_middleName = ['Александрович', 'Дмитриевич', 'Андреевич', 'Валерьевич', 'Викторович', 'Петрович', 'Максимович', 'Дамирович', 'Давыдович', 'Степанович', 'Евгеньевич']
Drivers_exp = [3, 5, 2, 5, 6, 4]
Drivers_work_exp = [1, 3, 1, 4, 2, 1]

Routes = ['Москва -> Краснодар', 'Воронеж - > Челябинск', 'Уфа -> Екатеринбург', 'Волгоград -> Самара',
          'Саратов -> Тамбов', 'Казань -> Уфа', 'Тольяти -> Москва']

Routes_date = ['12:02-01.12.2024', '11:04-05.02.2011', '14:54-13.03.2009', '10:01-05.09.2020',
               '16:52-05.12.2025', '14:22-09.01.2022', '13:04-05.01.2005']

Car_brands = ['BMW', 'Volvo', 'Lada', 'Mazda', 'KIA', 'Honda']
Car_colors = ['Жетлый', 'Зеленый', 'Синий', 'Белый', 'Черный', 'Фиолетовый']
Car_numbers = ['X000XX', 'X001XX', 'X002XX', 'X003XX', 'X004XX', 'X000X5']
Location_city = ['Москва', 'Краснодар', 'Уфа', 'Сочи', 'Волга']
Location_street = ['Кузнечная', 'Солнечная', 'Цветочная', 'Волжская', 'Ставропольская']


def sql_connection():
    try:
        con = sqlite3.connect("TasksBase.db")
        con.execute("PRAGMA foreign_keys = ON")
        return con
    except Error:
        print("Призошла неожиданная ошибка", Error)


def sql_create_tables(con):
    cursorObj = con.cursor()

    cursorObj.execute("Create table if not exists Qualification (id integer Primary key autoincrement,"
                      " driving_exp text, driving_in_company text)")

    cursorObj.execute(
        "CREATE TABLE if not exists Drivers (id integer PRIMARY KEY autoincrement, lastName text,"
        " firstName text, middleName text, qualification integer, FOREIGN KEY(qualification)"
        "REFERENCES Qualification(id) ON DELETE CASCADE)"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Routes (id integer PRIMARY KEY autoincrement, route text)"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Cars (id integer PRIMARY KEY autoincrement, brand text,"
        "color text, number text)"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Routes_History (id integer PRIMARY KEY autoincrement, date text,"
        "car_id integer, driver_id integer,  FOREIGN KEY(id) REFERENCES Routes(id) ON DELETE CASCADE,"
        "FOREIGN KEY(car_id) REFERENCES Cars(id) ON DELETE CASCADE, FOREIGN KEY(driver_id) "
        "REFERENCES Drivers(id) ON DELETE CASCADE)"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Locations (id integer PRIMARY KEY autoincrement, city text, street text)"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Auto_Base_Taxi (id integer PRIMARY KEY autoincrement, id_location integer,"
        "id_car integer, FOREIGN KEY(id_location) REFERENCES Locations(id) ON DELETE CASCADE, "
        "FOREIGN KEY (id_car) REFERENCES Cars(id) ON DELETE CASCADE )"
    )

    cursorObj.execute(
        "CREATE TABLE if not exists Auto_Base_Passenger_Car (id integer PRIMARY KEY autoincrement, id_location integer,"
        "id_car integer, FOREIGN KEY(id_location) REFERENCES Locations(id) ON DELETE CASCADE, "
        "FOREIGN KEY (id_car) REFERENCES Cars(id) ON DELETE CASCADE )"
    )
    cursorObj.execute(
        "CREATE TABLE if not exists Auto_Base_Trucks_Car (id integer PRIMARY KEY autoincrement, id_location integer,"
        "id_car integer, FOREIGN KEY(id_location) REFERENCES Locations(id) ON DELETE CASCADE, "
        "FOREIGN KEY (id_car) REFERENCES Cars(id) ON DELETE CASCADE )"
    )
    cursorObj.execute(
        "CREATE TABLE if not exists Auto_Base_Employee_Cars (id integer PRIMARY KEY autoincrement, id_location integer,"
        "id_car integer, FOREIGN KEY(id_location) REFERENCES Locations(id) ON DELETE CASCADE, "
        "FOREIGN KEY (id_car) REFERENCES Cars(id) ON DELETE CASCADE )"
    )


def insert_into_table_qualifications(con):
    cursorObj = con.cursor()

    qualifications = list(zip(Drivers_exp, Drivers_work_exp))
    for i, qualification in enumerate(qualifications):
        cursorObj.execute("INSERT INTO Qualification (driving_exp, driving_in_company) VALUES (?,?)",
                          (qualification[0], qualification[1]))
    con.commit()


def insert_into_table_drivers(con):
    cursorObj = con.cursor()

    for lastName in Drivers_lastName:
        for firstName in Drivers_firstName:
            for middleName in Drivers_middleName:
                qualification = random.randint(1, 6)
                cursorObj.execute("Insert into Drivers (lastName, firstName, middleName, qualification)"
                                  " VALUES (?,?,?,?)", (lastName, firstName, middleName, qualification))

    con.commit()


def insert_into_table_cars(con):
    cursorObj = con.cursor()
    cars = list(zip(Car_brands, Car_colors, Car_numbers))
    for car in cars:
        cursorObj.execute("Insert into Cars(brand, color, number) VALUES (?,?,?)", car)
    con.commit()


def insert_into_table_routes(con):
    cursorObj = con.cursor()

    for route in Routes:
        cursorObj.execute("Insert into Routes (route) VALUES (?)", (route,))
    con.commit()


def insert_into_table_locations(con):
    cursorObj = con.cursor()
    locations = list(zip(Location_city, Location_street))
    for location in locations:
        cursorObj.execute("Insert into Locations (city, street) VALUES (?,?)", location)
    con.commit()


def insert_into_table_routes_history(con):
    cursorObj = con.cursor()
    route_ent = list(zip(Routes_date))
    for i, routes_ent in enumerate(route_ent):
        cursorObj.execute("Insert into Routes_History (date, car_id, driver_id) VALUES (?,?,?)",
                              (routes_ent[0], random.randint(1, i+1), random.randint(1, i+1)))
    con.commit()


def insert_into_auto_base_taxi_all(con):
    cursorObj = con.cursor()

    # получаем количество записей в таблице Locations и Cars
    cursorObj.execute("SELECT COUNT(*) FROM Locations")
    locations_count = cursorObj.fetchone()[0]

    cursorObj.execute("SELECT COUNT(*) FROM Cars")
    cars_count = cursorObj.fetchone()[0]

    # вставляем в таблицу Auto_Base_Taxi все пары (id_location, id_car)
    for id_location in range(1, locations_count + 1):
        for id_car in range(1, cars_count + 1):
            cursorObj.execute(
                "INSERT INTO Auto_Base_Taxi(id_location, id_car) VALUES (?,?)",
                (id_location, id_car)
            )
    con.commit()


def insert_into_auto_base_passenger_car(con):
    cursorObj = con.cursor()

    # получаем количество записей в таблице Locations и Cars
    cursorObj.execute("SELECT COUNT(*) FROM Locations")
    locations_count = cursorObj.fetchone()[0]

    cursorObj.execute("SELECT COUNT(*) FROM Cars")
    cars_count = cursorObj.fetchone()[0]

    # вставляем в таблицу Auto_Base_Passenger_Car все пары (id_location, id_car)
    for id_location in range(1, locations_count + 1):
        for id_car in range(1, cars_count + 1):
            cursorObj.execute(
                "INSERT INTO Auto_Base_Passenger_Car(id_location, id_car) VALUES (?,?)",
                (id_location, id_car)
            )
    con.commit()


def insert_into_auto_base_trucks_car(con):
    cursorObj = con.cursor()

    # получаем количество записей в таблице Locations и Cars
    cursorObj.execute("SELECT COUNT(*) FROM Locations")
    locations_count = cursorObj.fetchone()[0]

    cursorObj.execute("SELECT COUNT(*) FROM Cars")
    cars_count = cursorObj.fetchone()[0]

    # вставляем в таблицу Auto_Base_Trucks_Car все пары (id_location, id_car)
    for id_location in range(1, locations_count + 1):
        for id_car in range(1, cars_count + 1):
            cursorObj.execute(
                "INSERT INTO Auto_Base_Trucks_Car(id_location, id_car) VALUES (?,?)",
                (id_location, id_car)
            )
    con.commit()


def insert_into_auto_base_employee_car(con):
    cursorObj = con.cursor()

    # получаем количество записей в таблице Locations и Cars
    cursorObj.execute("SELECT COUNT(*) FROM Locations")
    locations_count = cursorObj.fetchone()[0]

    cursorObj.execute("SELECT COUNT(*) FROM Cars")
    cars_count = cursorObj.fetchone()[0]

    # вставляем в таблицу Auto_Base_Employee_Cars все пары (id_location, id_car)
    for id_location in range(1, locations_count + 1):
        for id_car in range(1, cars_count + 1):
            cursorObj.execute(
                "INSERT INTO Auto_Base_Employee_Cars(id_location, id_car) VALUES (?,?)",
                (id_location, id_car)
            )
    con.commit()


def test_select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * from Routes_History where car_id = 6")
    [print(row) for row in cursorObj.fetchall()]
    cursorObj.execute("Delete from Cars where id = 6")
    cursorObj.execute("SELECT * from Routes_History where car_id = 6")
    [print(row) for row in cursorObj.fetchall()]
    con.commit()


def execute_and_print_query(con, query, query_description):
    print(query_description)
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    print(cursor.rowcount, "records affected.")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()

queries = [
    ("SELECT * FROM Cars;", "Выбрать все записи из таблицы 'Cars'"),
    ("UPDATE Cars SET color = 'Red' WHERE id = 3;", "Обновить цвет автомобиля с определенным ID на новое значение"),
    ("SELECT * FROM Cars WHERE color = 'Red';", "Выбрать автомобили с определенным цветом"),
    ("DELETE FROM Cars WHERE id = 12;", "Удалить автомобиль с определенным ID"),
    ("SELECT * FROM Cars ORDER BY brand;", "Выбрать все автомобили, отсортированные по марке"),
    ("SELECT COUNT(*) FROM Cars;", "Подсчитать количество автомобили в таблице"),
    ("SELECT COUNT(*) FROM Cars WHERE brand = 'BMW';", "Подсчитать количество автомобилей марки 'BMW'"),
    ("UPDATE Cars SET color = 'Blue' WHERE brand = 'Lada';", "Обновить цвет всех автомобилей марки 'Lada'"),
    ("DELETE FROM Cars WHERE brand = 'Honda';", "Удалить все автомобили марки 'Honda'"),
    ("SELECT * FROM Cars WHERE color = 'Black' AND brand = 'Volvo';", "Выбрать черные автомобили марки 'Volvo'"),
    ("SELECT DISTINCT brand FROM Cars;", "Вывести уникальные марки автомобилей"),
    ("UPDATE Routes SET route = 'Moscow -> Sochi' WHERE id = 5;", "Обновить определенный маршрут по его ID"),
    ("UPDATE Cars SET brand = 'Volkswagen' WHERE brand = 'Lada';", "Заменить все автомобили марки 'Lada' на 'Volkswagen'"),
    ("SELECT * FROM Routes WHERE route LIKE '%-> Sochi%';", "Выбрать все маршруты ведущие в 'Сочи'"),
    ("DELETE FROM Routes WHERE route LIKE '%-> Tambov%';", "Удалить все маршруты ведущие в 'Тамбов'"),
    ("UPDATE Locations SET city = 'Helsinki' WHERE city = 'Moscow';", "Заменить все 'Москва' на 'Хельсинки' в таблице местоположений"),
    ("SELECT COUNT(*) FROM Drivers WHERE qualification = 3;", "Подсчитать количество водителей с квалификацией 3"),
    ("SELECT * FROM Locations WHERE city = 'Helsinki';", "Выбрать все записи местоположений в 'Хельсинки'"),
    ("SELECT * FROM Drivers WHERE qualification >= 3 AND qualification <= 5;", "Выбрать водителей с квалификациями между 3 и 5"),
    ("DELETE FROM Drivers WHERE qualification = 1;", "Удалить всех водителей с квалификацией 1"),
    ("UPDATE Drivers SET qualification = 4 WHERE lastName = 'Путин';", "Обновить квалификацию водителя с фамилией 'Путин'"),
    ("SELECT * FROM Locations ORDER BY city;", "Выбрать все записи из таблицы 'Locations', отсортированные по городу"),
    ("UPDATE Locations SET street = 'Lenina' WHERE city = 'Sochi';", "Заменить все улицы в городе 'Сочи' на 'Ленина'"),
    ("DELETE FROM Locations WHERE city = 'Helsinki';", "Удалить все записи о местоположении в 'Хельсинки'"),
    ("SELECT * FROM Drivers WHERE lastName = 'Medvedev';", "Выбрать всех водителей с фамилией 'Медведев'"),
    ("UPDATE Locations SET city = 'Samara' WHERE city = 'Krasnodar';", "Заменить все 'Краснодар' на 'Самара' в таблице местоположений"),
    ("UPDATE Cars SET brand = 'Hyundai' WHERE brand = 'KIA';", "Заменить все автомобили марки 'KIA' на 'Hyundai'"),
    ("SELECT * FROM Cars WHERE brand = 'Hyundai';", "Выбрать все автомобили марки 'Hyundai'"),
    ("DELETE FROM Cars WHERE brand = 'Mazda';", "Удалить все автомобили марки 'Mazda'"),
    ("UPDATE Drivers SET qualification = 5 WHERE qualification = 1;", "Апгрейдить всех водителей с квалификацией 1 до квалификации 5"),
    ("DELETE FROM Locations WHERE city = 'Samara';", "Удалить все записи о местоположении в 'Самара'"),
    ("UPDATE Locations SET street = 'Gagarina' WHERE city = 'Kazan';", "Заменить все улицы в городе 'Казань' на 'Гагарина'"),
    ("DELETE FROM Drivers WHERE lastName like 'A%';", "Удалить всех водителей чья фамилия начинается на 'А'"),
    ("UPDATE Cars SET color = 'Green' WHERE id <= 5;", "Обновить цвет всех автомобилей с ID меньше или равно 5 на 'Зеленый'"),
    ("DELETE FROM Cars WHERE brand = 'Hyundai';", "Удалить все автомобили марки 'Hyundai'"),
    ("UPDATE Drivers SET qualification = 2 WHERE firstName like 'V%A';", "Обновить квалификацию всех водителей у которых имя начинается на 'В' и заканчивается на 'А'"),
    ("SELECT * FROM Locations WHERE city like '%a%';", "Выбрать все города в которых содержится 'а'"),
    ("DELETE FROM Locations WHERE city like 'Mos%';", "Удалить все записи о городах начинающихся на 'Мос'")
]

def drop_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("Drop table if exists Qualification")
    cursorObj.execute("Drop table if exists Drivers")
    cursorObj.execute("Drop table if exists Routes")
    cursorObj.execute("Drop table if exists Cars")
    cursorObj.execute("Drop table if exists Locations")
    cursorObj.execute("Drop table if exists Routes_History")


#connection = sql_connection()
#sql_create_tables(connection)

# insert_into_table_qualifications(connection)
# insert_into_table_drivers(connection)
# insert_into_table_routes(connection)
# insert_into_table_cars(connection)
# insert_into_table_locations(connection)
# insert_into_table_routes_history(connection)
# insert_into_auto_base_taxi_all(connection)
# insert_into_auto_base_passenger_car(connection)
# insert_into_auto_base_trucks_car(connection)
# insert_into_auto_base_employee_car(connection)
#for query, description in queries:
  #execute_and_print_query(connection, query, description)



#connection.close()
#test_select(connection)
#drop_table(connection)