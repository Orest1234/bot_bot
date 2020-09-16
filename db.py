import mysql.connector
import random
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='film',
            auth_plugin='mysql_native_password'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "", 'db_name')

def create_database(connection, query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    print("Database created successfully")
  except Error as e:
    print(f"The error '{e}' occurred")



# create_database_query = "CREATE DATABASE films"
# create_database(connection, create_database_query)
connection = create_connection("localhost", "root", "", "films")


def execute_query(connection, query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    connection.commit()
    print("Query executed successfully")
  except Error as e:
    print(f"The error '{e}' occurred")


create_films_table = """
CREATE TABLE IF NOT EXISTS films (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_film` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `desk` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `genre` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `releas_ date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin
"""

execute_query(connection, create_films_table)


# create_film = """
# INSERT INTO `sql7364121`.`films` (`name_film`, `desk`, `genre`, `releas_ date`) VALUES ('pisla', 'film about love', 'roman', '2019');
# """
#
# execute_query(connection, create_film)
# create_film = """
# INSERT INTO `film`.`films`(`name_film`, `desk`, `genre`, `releas_date`) VALUES ('Великий Гетсбі (Великий Гэтсби)', '«Великий Гетсбі» — австралійсько-американський драматичний фільм у форматі 3D, знятий у 2012 році режисером Базом Лурманном на основі роману Френсіса Скотта Фіцджеральда «Великий Гетсбі». У головних ролях — Леонардо Ді Капріо, Тобі Маґвайр та Кері Малліган.', 'Романтика/Драма', '2013.05.13');
# """
#
# execute_query(connection, create_film)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_film = "SELECT id,name_film,desk,genre, releas_date from films"
films = execute_read_query(connection, select_film)
# print(films)
# print('*'*10)
# print(films[1])
# answer =  random.choice(films)
# print('*'*10)
# print(answer[1])