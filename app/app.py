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

# API-Endpunkt zum Aktualisieren eines Ziels
@app.route('/update_goal/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    data = request.get_json()
    goal = Goal.query.get(goal_id)
    
    if not goal:
        return jsonify({'message': 'Ziel nicht gefunden'}), 404

    # Aktualisiere die Felder des Ziels
    goal.department = data.get('department', goal.department)
    goal.statement = data.get('statement', goal.statement)
    goal.success_criteria = data.get('success_criteria', goal.success_criteria)
    goal.rating = data.get('rating', goal.rating)
    goal.assessment = data.get('assessment', goal.assessment)

    db.session.commit()
    return jsonify({'message': 'Ziel erfolgreich aktualisiert'})


@app.route('/goals/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = Goal.query.get(goal_id)
    
    if not goal:
        return jsonify({'message': 'Ziel nicht gefunden'}), 404

    goal_data = {
        'id': goal.id,
        'department': goal.department,
        'statement': goal.statement,
        'success_criteria': goal.success_criteria,
        'rating': goal.rating,
        'assessment': goal.assessment,
        'last_modified': goal.last_modified
    }
    
    return jsonify({'goal': goal_data})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goal/<int:goal_id>')
def goal_detail(goal_id):
    return render_template('goal_detail.html', goal_id=goal_id)