import datetime

def log_workout():
    exercise = input("What work out did you do: ")
    weight = input("How much pounds did you lift: ")
    reps = input("How much reps: ")
    date = datetime.date.today()

    with open("workout_log.txt", "a") as file:
        file.write(f"{date} | {exercise} | {weight}lb | {reps} reps\n")

    print("NICE!! SAVED")

if __name__ == "__main__":
    log_workout()