from enum import Enum

class SplitType(Enum):
    PUSH = 1
    PULL = 2
    LEGS = 3

class AllowedWorkouts(Enum):
    Bench_Press = "Bench Press"
    Push_Up = "Push Up"
    Shoulder_Press = "Shoulder Press"

    @classmethod
    def list_names(cls):
        return[w.value for w in cls]
    
WORKOUT_GROUPS = {
SplitType.PUSH.value: [
    AllowedWorkouts.Bench_Press.value, 
    AllowedWorkouts.Push_Up.value, 
    AllowedWorkouts.Shoulder_Press.value
],
SplitType.PULL.value: [], # Add pull movements here later
SplitType.LEGS.value: []  # Add leg movements here later
}
    
class WorkOut:

    def __init__(self, workout, sets, reps, weight):
        self.workout  = workout
        self.sets = sets
        self.reps = reps 
        self.weight = weight
        self.workoutType = next((key for key, value in WORKOUT_GROUPS.items() if workout in value), "Unknown")

    def to_dict(self):
        return {
            "workout": self.workout,
            "sets": self.sets,
            "reps": self.reps,
            "weight": self.weight,
            "workout_type_id": self.workoutType  # Automatically computed!
        }

    
