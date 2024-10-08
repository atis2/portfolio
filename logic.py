import sqlite3
import config 

status = [(1, 'Проектирование'),(2, 'В процессе разработки'),(3, 'Разработан'),(4, 'Обновлен'), (5, 'Завершен/Не поддерживается')]
project = [('Subnatica','https://hub.kodland.org/ru/my-projects','Subnatica это крутая игра', 5),('Другой мир','https://hub.kodland.org/ru/my-projects', 'ты попал в другой мир и уже живешь 1 год ты уже силон и ты встретил девочку', 5),('The Forest', 'https://hub.kodland.org/ru/my-projects', 'The Forest это игра про что как выживать в лесу с соседами',2),('ХАЯО МИЯДЗАКИ','https://hub.kodland.org/ru/my-projects', 'нажми на картинки и они будут двыгатся',3)]
class DB_Manager:
    
        
    def create_tables(self):
        db = sqlite3.connect(config.database)
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS status(id INTEGER PRIMARY KEY, status_name TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS projects(id INTEGER PRIMARY KEY, name TEXT, url TEXT, info TEXT, status INTEGER, FOREIGN KEY(status) REFERENCES status(id))")
        db.commit()
        db.close()

    def __executemany(self, sql, data):
        db = sqlite3.connect(config.database)
        with db:
            db.executemany(sql, data)
            db.commit()

    def update_table(self):
        db = sqlite3.connect(config.database)
        cur = db.cursor()
        cur.execute("UPDATE projects SET foto=subnatica.jpeg WHERE name='Subnatica'")
        cur.execute("UPDATE projects SET foto=the forest.jpg WHERE name='The Forest'")
        cur.execute("UPDATE projects SET foto=portal.jpg WHERE name='Другой мир'")
        cur.execute("UPDATE projects SET foto=ХАЯО МИЯДЗАКИ.jpeg WHERE name='ХАЯО МИЯДЗАКИ'")
        # with db:
        #     sql = 'INSERT INTO status (id, status_name) VALUES(?, ?)'
        #     db.executemany(sql, status )
        #     db.executemany('INSERT INTO projects(name, url, info, status) VALUES(?, ?, ? ,?)', project)
        #     table_name = 'projects'
           
        #     # Название нового столбца и его тип данных
        #     new_column_name = 'foto'
        #     new_column_type = 'IMG'

        #     # Выполнение запроса на добавление столбца
        #     alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_type}"
        #     db.execute(alter_query)

            
        db.commit()
        db.close()
    def delete_status(self, status_id):
        db = sqlite3.connect(config.database)
        cur = db.cursor()
        cur.execute('DELETE FROM projects WHERE status = ?', (status_id,))
        db.commit()
        db.close()

    def update_status(self):
        db = sqlite3.connect(config.database)
        cur = db.cursor()
        cur.execute('UPDATE projects SET status=4 WHERE title="https://hub.kodland.org/ru/my-projects"')
        db.commit()
        db.close()

    def get_projects(self, user_id):
        db = sqlite3.connect(config.database)
        
        with db:
            result = db.execute('SELECT id , id, name,  info,  url, status FROM projects ' ).fetchall()
            print(result)
            db.commit()
        db.close()
        return(result)
    




    def get_project_info(self, user_id, name_projects):
        db = sqlite3.connect(config.database)
        with db:
            result = db.execute('SELECT name,  info,  url, status_name FROM projects JOIN status ON status.id = projects.status WHERE name = ?' ,(name_projects,)).fetchall()
            print(result)
            db.commit()
        db.close()
        return(result)
    
    def update_projects(self, param, data):
        self.__executemany(f"UPDATE projects SET {param} = ? WHERE project_name = ? AND user_id = ?", [data]) # data ('atr', 'mew', 'name', 'user_id')

            






    def get_statuses(self, user_id, name_status):
        db = sqlite3.connect(config.database)
        with db:
            result = db.execute('UPDATE projects SET status = ? WHERE ' ,(name_status,)).fetchall()
            print(result)
            db.commit()
        db.close()
        return(result)

    def get_project_skills(self, project_name):
        return("")
    

    