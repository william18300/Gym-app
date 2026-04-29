from enum import Enum

class SplitType(Enum):
    PUSH = "Push"
    PULL = "Pull"
    LEGS = "Legs"

class WorkOut:

    def __init__(self, workout, sets, reps, weight, workoutType):
        self.workout  = workout
        self.sets = sets
        self.reps = reps 
        self.weight = weight
        self.wrokoutType = workoutType

    
