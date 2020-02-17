from app import app, db
from app.models import User, Task, Quotation
from flask import render_template, request, redirect
import random


@app.route('/tasks')
def index():
    user = User.query.get(1)
    tasks = user.tasks
    quotations = Quotation.query.all()
    random_quotation = random.choice(quotations)
    return render_template('index.html', title='Home', user=user, tasks=tasks, random_quotation=random_quotation)

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

@app.route('/quotations')
def quotations():
    quotations = Quotation.query.all()
    return render_template('quotations.html', title="Quotations", quotations=quotations)

@app.route('/quotations', methods=['POST'])
def create_quotation():
    user = Quotation.query.get(1)
    quotationContents = request.form['contents']
    newQuotation = Quotation(contents=quotationContents)
    db.session.add(newQuotation)
    db.session.commit()
    return redirect('/quotations') 