import sqlite3 as sq

db = sq.connect('data.db')
cur = db.cursor()

def init_db():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS "
        "tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "description TEXT NOT NULL,"
        "deadline DATE,"
        "user_id INTEGER NOT NULL,"
        "status BOOLEAN NOT NULL DEFAULT TRUE)"
    )
    db.commit()

def select_all_tasks(user: int):
    cur.execute("SELECT user_id FROM TASK tasks WHERE user_id = ?", (user,) )
    data = cur.fetchall()
    return  data

def insert_task(user: int, task: str):
    cur.execute("INSERT INTO tasks (description, user_id) VALUES (?, ?)",
                (user, task,))
    db.commit()

def delete_task(task, user):
    cur.execute("DELETE FROM tasks WHERE user_id = ? AND id = ?",
                (user, task,))