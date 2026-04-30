import os
import Backend.WorkOut as bw
from flask import Flask
from supabase import create_client, Client
from dotenv import load_dotenv
from flask import Flask, render_template

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

    if name not in bw.AllowedWorkouts.list_names():
        print(f"DEBUG: Received workout '{name}' with {sets} sets")
        return "Error: This workout isn't anitmated yet ", 400


    # 2. Add your Database logic here (SQLAlchemy or Supabase)
    # new_workout = WorkOut(name=name, sets=sets, reps=reps)
    # session.add(new_workout)
    # session.commit()

    # 3. Send the user back to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)