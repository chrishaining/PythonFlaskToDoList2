from app import app, db
from app.models import User, Task
from flask import render_template, request, redirect


@app.route('/tasks')
def index():
    user = User.query.get(1)
    tasks = user.tasks
    return render_template('index.html', title='Home', user=user, tasks=tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    user = User.query.get(1)
    taskTitle = request.form['title']
    taskDescription = request.form['description']
    newTask = Task(title=taskTitle, description=taskDescription, user=user)
    db.session.add(newTask)
    db.session.commit()
    return redirect('/tasks') 

@app.route('/tasks/<int:task_id>', methods=['POST'])
def update(task_id):
    task = Task.query.get(task_id)
    task.done = True 
    db.session.commit()
    return redirect('/tasks')

