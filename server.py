from flask import Flask, render_template, redirect, url_for, request, session, flash
import json
import time

app = Flask(__name__)
app.secret_key = "secret"

with open('static/questions.json', 'r') as file:
    questions = json.load(file)

with open('static/users.json',  'r') as file:
    users_data = json.load(file)

with open('static/positions.json',  'r') as file:
    positions_data = json.load(file)

def update_stats(team_name, question):
    with open('static/stats.csv', 'a') as file:
        file.write(f"{team_name}, {str(question)}, {(time.localtime()[3:6])} \n")
    with open('static/positions.json',  'w') as file:
        file.write(json.dumps(positions_data))

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'team_name' in session:
        team_name=session['team_name']
        team_position=positions_data[team_name]
        
        if request.method == 'POST':
            user_answer = (request.form.get('answer'))
            correct_answer = questions[str(team_position)]
            if user_answer == correct_answer.lower():
                print(session)
                team_name = session['team_name']
                update_stats(team_name, 1) # The +1 is for changing the index to question number
                team_position+=1
                positions_data[team_name] += 1
                # if team_position == 7:
                    # return render_template('final.html')
                    # return redirect(url_for('logout'))
                flash('Correct answer')
            else:
                flash('Wrong answer')

        return render_template('index2_real.html', question=questions, team_position=team_position, team_name=team_name)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        password = request.form.get('password')

        if team_name in users_data and password == users_data[team_name]:
            session['team_name'] = team_name
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid team name or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('team_name', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

app.run(host = "0.0.0.0", debug=True)
