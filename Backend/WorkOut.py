from enum import Enum

class SplitType(Enum):
    PUSH = 1
    PULL = 2
    LEGS = 3

class AllowedWorkouts(Enum):
    Bench_Press = "Bench Press"
    Push_Up = "Push Up"
    Shoulder_Press = "Shoulder Press"
    Machine_Fly_Push = "Machine Fly Push"
    Machine_Fly_Pull = "Machine Fly Pull"
    Chest_Press = "Chest Press"
    Cable_Lats = "Cable Lat"
    Cable_Rope_Hammer = "Cable Rope Hammer"
    Cable_OverHead = "Cable Overhead"
    Leg_Press = "Leg Press"
    Leg_Extension = "Leg Extension"
    Hip_Abductor = "Hip Abductor"

 
    @classmethod
    def list_names(cls):
        return[w.value for w in cls]
    
WORKOUT_GROUPS = {
SplitType.PUSH.value: [
    AllowedWorkouts.Bench_Press.value, 
    AllowedWorkouts.Push_Up.value, 
    AllowedWorkouts.Shoulder_Press.value,
    AllowedWorkouts.Machine_Fly_Push.value
],
SplitType.PULL.value: [
    AllowedWorkouts.Machine_Fly_Pull.value,
    AllowedWorkouts.Cable_Rope_Hammer.value,
    AllowedWorkouts.Cable_Lats.value,
    AllowedWorkouts.Cable_OverHead.value
], # Add pull movements here later
SplitType.LEGS.value: [
    AllowedWorkouts.Leg_Press.value,
    AllowedWorkouts.Leg_Extension.value,
    AllowedWorkouts.Hip_Abductor.value
]  # Add leg movements here later
}

WORKOUT_DETAILS = {
    AllowedWorkouts.Bench_Press.value: {
        "muscle": "Chest (Pectorals), Shoulders, Triceps",
        "video_id": "hWbUlkb5Ms4"
    },
    AllowedWorkouts.Push_Up.value: {
        "muscle": "Chest, Shoulders, Triceps, Core",
        "video_id": "pKZ-lkKKMws"
    },
    AllowedWorkouts.Shoulder_Press.value: {
        "muscle": "Shoulders (Deltoids), Triceps",
        "video_id": "6v4nrRVySj0"
    },
    AllowedWorkouts.Machine_Fly_Push.value: {
        "muscle": "Chest (Inner Pectorals)",
        "video_id": "a9vQ_hwIksU"
    },
    AllowedWorkouts.Machine_Fly_Pull.value: {
        "muscle": "Rear Deltoids, Upper Back",
        "video_id": "7tgx6QHB0-A"
    },
    AllowedWorkouts.Chest_Press.value: {
        "muscle": "Chest, Triceps",
        "video_id": "2awX3rTGa1k"
    },
    AllowedWorkouts.Cable_Lats.value: {
        "muscle": "Lats (Latissimus Dorsi), Biceps",
        "video_id": "bNmvKpJSWKM"
    },
    AllowedWorkouts.Cable_Rope_Hammer.value: {
        "muscle": "Biceps (Brachialis), Forearms",
        "video_id": "6Dh8sD6aNQE"
    },
    AllowedWorkouts.Cable_OverHead.value: {
        "muscle": "Triceps (Long Head)",
        "video_id": "9Ark9S11uXw"
    },
    AllowedWorkouts.Leg_Press.value: {
        "muscle": "Quads, Glutes, Hamstrings",
        "video_id": "EotSw18oR9w"
    },
    AllowedWorkouts.Leg_Extension.value: {
        "muscle": "Quads (Quadriceps)",
        "video_id": "uM86QE59Tgc"
    },
    AllowedWorkouts.Hip_Abductor.value: {
        "muscle": "Glutes (Medius/Minimus), Outer Thigh",
        "video_id": "tu4o4quPv2k"
    }
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

    
