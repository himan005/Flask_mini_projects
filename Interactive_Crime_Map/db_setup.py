import pymysql
import dbConfig

connection = pymysql.connect(host = dbConfig.db_host,
                             port = dbConfig.db_port,
                             user = dbConfig.db_user,
                             password = dbConfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "create database if not exists crimemap"
        cursor.execute(sql)
        sql = """create table if not exists crimemap.crimes
        (
            id int not null auto_increment,
            latitude float(10, 6),
            longitude float(10, 6),
            date datetime,
            category varchar(50),
            description varchar(1000),
            updated_at timestamp,
            primary key (id)
        )"""
        cursor.execute(sql);
    connection.commit()
finally:
    cursor.close()
    connection.close()