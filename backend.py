from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

DATA_LOC = os.path.join(os.path.abspath(os.path.dirname(__file__)), "instance/toDo.db")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toDo.db'
db = SQLAlchemy(app)
print(DATA_LOC)
class DataBase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.conn = None
    def __enter__(self):
        self.conn = sqlite3.connect(self.file_name)
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

class User_DB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    isDone = db.Column(db.Boolean, default =False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    with DataBase(DATA_LOC) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_db")
        records = cursor.fetchall()
    return render_template('index.html', records=records)

@app.route("/add", methods=['POST'])
def add():
    id = request.form['id']
    task = request.form['task']
    with DataBase(DATA_LOC) as conn:
        cursor = conn.cursor()
        if(id==""):
            addValue = True
        else:
            addValue = False
        if(addValue):
            new_task = User_DB(task=task)
            db.session.add(new_task)
            db.session.commit()
        else:
            cursor.execute(f"UPDATE user_db SET task = '{task}' WHERE id={id}")
            conn.commit()
    return redirect(url_for("index"))

@app.route("/changeIsDoneStatus/<int:taskId>", methods=['GET'])
def changeIsDoneStatus(taskId):
    with DataBase(DATA_LOC) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT isDone FROM user_db WHERE id="+str(taskId))
        data = cursor.fetchone()
        print(data[0])
        if(data[0]):
            print("Changing True Value to False")
            cursor.execute(f"UPDATE user_db SET isDone=False WHERE id={taskId}")
        else:
            print("Changing False Value to True")
            cursor.execute(f"UPDATE user_db SET isDone=True WHERE id={taskId}")
        conn.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:taskId>", methods=['GET'])
def delete(taskId):
    with DataBase(DATA_LOC) as conn:
        cursor=conn.cursor()
        cursor.execute("DELETE FROM user_db WHERE id="+str(taskId))
        conn.commit()
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True, port=1000)