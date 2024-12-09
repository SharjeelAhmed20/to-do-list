from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Routes
@app.route('/')
def index():
    tasks = Task.query.all()  # Get all tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    content = request.form['content']
    if content:
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
    else:
        flash("Task content cannot be empty!", "error")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "success")
    else:
        flash("Task not found!", "error")
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
        flash("Task status updated!", "success")
    else:
        flash("Task not found!", "error")
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database and tables are created
    app.run(debug=True)
