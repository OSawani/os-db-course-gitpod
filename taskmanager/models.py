# create db schema by defining models

from taskmanager import db
#file type does not have to be imported explicitly because we use Flask-SQLAlchemy, contained within db

# create two separate tables,
# represented by class based models
# using SQLAlchemy ORM

# 1st table for categories, therefore class called Category, use the declarative base from SQLAlchemy model

class Category(db.Model):
    #schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False) # max characters are 25 mandatory
    tasks = db.relationship('Task', backref='category', cascade="all, delete", lazy=True) # establishes a many to one relationship

    def __repr__(self): # __repr__ to represent itself in the form of a string
        return self.category_name

class Task(db.Model):
    #schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) # once category is deleted all tasks are deleted

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )