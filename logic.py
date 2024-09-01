import sqlite3
import config

status = [(1, 'Проектирование'),(2, 'В процессе разработки'),(3, 'Разработан'),(4, 'Обновлен'), (5, 'Завершен/Не поддерживается')]
project = [('Subnatica','https://hub.kodland.org/ru/my-projects','Subnatica это крутая игра', 5),('Другой мир','https://hub.kodland.org/ru/my-projects', 'ты попал в другой мир и уже живешь 1 год ты уже силон и ты встретил девочку', 5),('The Forest', 'https://hub.kodland.org/ru/my-projects', 'The Forest это игра про что как выживать в лесу с соседами',2),('ХАЯО МИЯДЗАКИ','https://hub.kodland.org/ru/my-projects', 'нажми на картинки и они будут двыгатся',3)]
class DB_Manager:
    
        
    def create_tables(self):
        db = sqlite3.connect(config.database)
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS status(id INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS projects(id INTEGER PRIMARY KEY, name TEXT, url TEXT, info TEXT, status INTEGER, FOREIGN KEY(status) REFERENCES status(id))")
        db.commit()
        db.close()


    def update_table(self):
        db = sqlite3.connect(config.database)
        with db:
            sql = 'INSERT INTO status (id, name) VALUES(?, ?)'
            db.executemany(sql, status )
            db.executemany('INSERT INTO projects(name, url, info, status) VALUES(?, ?, ? ,?)', project)



        db.close()
    