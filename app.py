from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

# This part "Reads" your file to show it on the website
@app.route('/')
def index():
    workouts = []
    try:
        with open("workout_log.txt", "r") as file:
            workouts = file.readlines()
    except FileNotFoundError:
        workouts = ["No workouts logged yet! Go hit the machines!"]
    
    return render_template('index.html', workouts=workouts)

# This part "Writes" to your file when you click the button
@app.route('/add', methods=['POST'])
def add_workout():
    exercise = request.form.get('exercise')
    weight = request.form.get('weight')
    reps = request.form.get('reps')
    date = datetime.date.today()

    with open("workout_log.txt", "a") as file:
        file.write(f"{date} | {exercise} | {weight}lbs | {reps} reps\n")
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)