import random

class FitnessRoutineCreator:
    def __init__(self):
        self.activity_list = {
            'upper_section': [
                ('Push-ups', 'reps'),
                ('Diamond Push-ups', 'reps'),
                ('Tricep Dips', 'reps'),
                ('Pike Push-ups', 'reps'),
                ('Pull-ups', 'reps'),
                ('Chin-ups', 'reps')
            ],
            'lower_section': [
                ('Squats', 'reps'),
                ('Lunges', 'reps'),
                ('Jump Squats', 'reps'),
                ('Calf Raises', 'reps'),
                ('Mountain Climbers', 'time'),
                ('High Knees', 'time')
            ],
            'core_section': [
                ('Crunches', 'reps'),
                ('Plank', 'time'),
                ('Russian Twists', 'reps'),
                ('Leg Raises', 'reps'),
                ('Bicycle Crunches', 'reps'),
                ('Superman Hold', 'time')
            ]
        }

    def create_routine(self, challenge_level='medium', length='medium'):
        # Set parameters based on challenge level
        challenge_params = {
            'easy': {'rounds': 2, 'exercises_per_section': 2},
            'medium': {'rounds': 3, 'exercises_per_section': 3},
            'hard': {'rounds': 4, 'exercises_per_section': 4}
        }

        # Length multipliers
        length_multiplier = {
            'short': 0.7,
            'medium': 1.0,
            'long': 1.3
        }

        params = challenge_params[challenge_level]
        multiplier = length_multiplier[length]

        routine = []
        
        # Generate routine for each section
        for section, activities in self.activity_list.items():
            chosen = random.sample(activities, params['exercises_per_section'])
            
            for activity, measurement in chosen:
                if measurement == 'reps':
                    base_reps = random.randint(8, 15)
                    reps = int(base_reps * multiplier)
                    routine.append(f"{activity}: {params['rounds']} sets of {reps} reps")
                else:  # time-based activity
                    base_time = random.randint(30, 45)
                    time = int(base_time * multiplier)
                    routine.append(f"{activity}: {params['rounds']} sets of {time} seconds")

        return routine

    def display_routine(self, routine):
        print("\n=== Your Fitness Routine Today ===")
        for index, activity in enumerate(routine, 1):
            print(f"{index}. {activity}")
        print("\nRest between sets: 30-60 seconds")
        print("Rest between exercises: 60-90 seconds")

# Example usage
if __name__ == "__main__":
    creator = FitnessRoutineCreator()
    
    # Generate routines of different challenge levels and lengths
    challenge_levels = ['easy', 'medium', 'hard']
    lengths = ['short', 'medium', 'long']
    
    challenge_level = random.choice(challenge_levels)
    length = random.choice(lengths)
    
    print(f"\nChallenge Level: {challenge_level.upper()}")
    print(f"Length: {length.upper()}")
    
    routine = creator.create_routine(challenge_level, length)
    creator.display_routine(routine)