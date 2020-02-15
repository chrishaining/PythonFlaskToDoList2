from app import app
from flask import render_template

@app.route('/')
def index():
    user = {'username': 'Chris'}
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': 'Milk, Cheese, Pizza, Fruit',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': 'Learn an awesome new programming language',
            'done': True
        }
    ]  
    return render_template('index.html', title='Home', user=user, tasks=tasks)

@app.route('/add_task')
def add_task():
    return render_template('add_task.html', title='Add Task')
