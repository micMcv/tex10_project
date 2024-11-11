from flask import Flask, request, jsonify, render_template
from config import Config
from models import db, Goal

app = Flask(__name__)
app.config.from_object(Config)

# Datenbank initialisieren
db.init_app(app)

# Route 1: Alle Ziele abrufen
@app.route('/goals', methods=['GET'])
def get_goals():
    goals = Goal.query.all()
    goals_list = [goal.to_dict() for goal in goals]
    return jsonify({"goals": goals_list}), 200

# Route 2: Ein neues Ziel hinzufügen
@app.route('/add_goal', methods=['POST'])
def add_goal():
    data = request.get_json()
    
    new_goal = Goal(
        department=data.get('department'),
        statement=data.get('statement'),
        success_criteria=data.get('success_criteria'),
        rating=data.get('rating'),
        assessment=data.get('assessment')
    )

    try:
        db.session.add(new_goal)
        db.session.commit()
        return jsonify({"message": "Goal added successfully!", "goal": new_goal.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goal/<int:goal_id>')
def goal_detail(goal_id):
    return render_template('goal_detail.html', goal_id=goal_id)