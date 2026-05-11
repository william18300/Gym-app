import os
import Backend.WorkOut as bw
from supabase import create_client, Client
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request, redirect, url_for

load_dotenv()

app = Flask(__name__)

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

@app.route('/')
def index():
    user_name = "William"

    return render_template('index.html',name = user_name, workout_options= bw.AllowedWorkouts.list_names())

from flask import Flask, render_template, request, redirect

@app.route('/add_workout', methods=['POST'])
def add_workout():
    # 1. Get data from the form
    name = request.form.get('workout_name')
    sets = request.form.get('sets')
    reps = request.form.get('reps')
    weight = request.form.get('weight')

    if name not in bw.AllowedWorkouts.list_names():
        print(f"DEBUG: Received workout '{name}' with {sets} sets")
        return "Error: This workout isn't anitmated yet ", 400
    
    new_workout = bw.WorkOut(
    workout= name,
    sets=sets,
    reps=reps,
    weight=weight
    )

    print(new_workout.to_dict())
    data, count = supabase.table("workouts").insert(new_workout.to_dict()).execute()

    return redirect(url_for('index'))


@app.route('/calendar')
def show_calendar():
    return render_template('calendar.html')

@app.route('/api/workouts')
def get_workouts():
    # 1. Fetch from Supabase
    response = supabase.table("workouts").select("*").execute()
    
    # 2. Format for FullCalendar
    events = []
    for row in response.data:

        clean_date = str(row['created_at'])[:10]

        events.append({
            'title': f"{row['workout']} ({row['reps']} reps) ({row['weight']} pounds)",
            'start': clean_date, 
            'color': '#2e5bff' # Your electric blue!
        })
    return jsonify(events)


    # 2. Add your Database logic here (SQLAlchemy or Supabase)
    # new_workout = WorkOut(name=name, sets=sets, reps=reps)
    # session.add(new_workout)
    # session.commit()

    # 3. Send the user back to the home page
    return redirect('/')

@app.route('/library')
def workout_library():
    return render_template('library.html', library=bw.WORKOUT_DETAILS)

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)