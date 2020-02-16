from app import db
from app.models import User, Task, Quotation


Task.query.delete()
User.query.delete()
Quotation.query.delete()

user = User(username='User')
db.session.add(user)
db.session.commit()


users = User.query.all()

user = User.query.get(1)

task1 = Task(title='Learn Python', description="Learn how to code in Python", done=True, user=user)
db.session.add(task1)
task2 = Task(title='Buy Milk', description="I need milk for my tea!", user=user)
db.session.add(task2)


quotation1 = Quotation(contents="Be happy.")
quotation2 = Quotation(contents="Don't be sad.")
quotation3 = Quotation(contents="Life is good.")
quotation4 = Quotation(contents="Life is not bad.")
quotation5 = Quotation(contents="You're very lucky.")

db.session.add(quotation1)
db.session.add(quotation2)
db.session.add(quotation3)
db.session.add(quotation4)
db.session.add(quotation5)

db.session.commit()

tasks = Task.query.all()
print(tasks)
task_user = Task.query.get(1).user
print(user.username)

# quotations = Quotation.query.all()

