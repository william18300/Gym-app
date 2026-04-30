from enum import Enum

class SplitType(Enum):
    PUSH = "Push"
    PULL = "Pull"
    LEGS = "Legs"

class AllowedWorkouts(Enum):
    Bench_Press = "Brench Press"
    Push_Up = "Push Up"
    Shoulder_Press = " Shoulder Press"

    @classmethod
    def list_names(cls):
        return[w.value for w in cls]
    
class WorkOut:

    def __init__(self, workout, sets, reps, weight, workoutType):
        self.workout  = workout
        self.sets = sets
        self.reps = reps 
        self.weight = weight
        self.wrokoutType = workoutType

    
