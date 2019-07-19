import requests

def getUser(uid):
    """
    Input: User ID (String)
    Output: Workouts for User (API Response -> Dict)
    """
    response = requests.post('https://deltaband.herokuapp.com/getUser', data = {'user_id': uid})
    data = response.json()
    return data

def getWorkouts(uid):
    """
    Input: User ID (String)
    Output: Workouts for User (API Response -> Dict)
    """
    response = requests.post('https://deltaband.herokuapp.com/getWorkouts', data = {'user_id': uid})
    data = response.json()
    return data

def updateWorkout(uid, workout):
    """
    Input: User ID (String), Workout (?)
    Output: Workouts for User (API Response -> Dict)
    """
    response = requests.post('https://deltaband.herokuapp.com/updateWorkout', data = {'user_id': uid, 'workout' : workout})
    data = response.json()
    return data

def newOnboarding(uid, info):
    """
    Input: User ID (String), User Info (Dict)
    Output: Workouts for User (API Response -> Dict)
    """
    response = requests.post('https://deltaband.herokuapp.com/newOnboarding', data = {'user_id': uid, 'data': info})
    data = response.json()
    return data

def getAllUsers():
    pass

def main():
    #print(getWorkouts("deltabandappreview@gmail.com"))
    pass

if __name__ == "__main__":
    main()


"""
        {'docs': [{
        '_id': '5d16e56ee62b0000178b5dcf',
        'user_id': 'deltabandappreview@gmail.com',
        'first_name': 'Delta',
        'last_name': 'Band',
        'full_name': 'Delta Band',
        'email': 'deltabandappreview@gmail.com',
        'is_trainer': False, 'clients': None,
        'has_completed_survey': True,
        'trainer_id': 'matt@deltaband.fit',
        'orms_estimated': {'Incline Bench Press': 179.23414937295345,
                   'Burpee': 376.0470138863182,
                   'Calf Raise': 294.28548026536976,
                   'Chest Press': 195.7459135630559,
                   'Chin Up': 257.28805930833664,
                   'Dip': 288.2686561547665,
                   'Face Pull': 108.85900874815033,
                   'Machine Fly': 184.3378152108913,
                   'Hip Abduction': 228.51495584061797,
                   'Hip Adduction': 243.50497225144346,
                   'Hip Thrust': 289.58266868226286,
                   'Leg Curl': 175.59606389135942,
                   'Leg Extension': 213.57747073451972,
                   'Leg Press': 473.3532797590278,
                   'Leg Raise': 494.8059684642998,
                   'Push Up': 401.8641779250099,
                   'Russian Twist': 494.8059684642998,
                   'Dumbbell Shoulder Press': 69.07065847545252,
                   'Dumbbell Shrug': 105.30438859480688,
                   'Thruster': 161.64378803623129},
                   'orms_known': {'Bulgarian Split Squat': 160,
                   'Squat': 315.3333333333333,
                   'Overhead Press': 131.5,
                   'Arnold Press': 54.66666666666667,
                   'Dumbbell Lunge': 60,
                   'Bench Press': 215.83333333333334,
                   'Bent Over Row': 178.83333333333334,
                   'Lat Pulldown': 168,
                   'Dumbbell Front Raise': 42,
                   'Dumbbell Lateral Raise': 35,
                   'Rope Tricep Pushdown': 105,
                   'Deadlift': 373.66666666666663,
                   'Pull Up': 229.33333333333331,
                   'Cable Row': 190,
                   'Dumbbell Hammer Curl': 50.166666666666664,
                   'Sit Up': 499.50000000000006,
                   'Dumbbell Curl': 50.666666666666664},
           'example_sets': [],
           'account_creation_date': '2019-06-29T04:13:34.140Z',
           'device_token': '45ee96e42f80a767876ed09d0ff7c755d6ddcdc8bae31e49fc99bbb4aa3d0f89',
           'age': 21,
           'birthday': '1997-12-30T00:00:00.000Z',
           'experience': 30,
           'gender': 'Male',
           'goal': 'Lose weight',
           'height': 72,
           'motivation': 'Competitions ',
           'trainer_first_name': 'Kelly',
           'trainer_gender': "Don't care",
           'trainer_style': 'Strict but nice',
           'weight': 185,
           'workout_duration': '75 mins',
           'workouts_per_week': 6,
           'room_id': '19895148',
           'last_read_message_time': 1562555127,
           'last_workout_date': '2019-07-13T22:51:16.195Z',
           'owned_module_ids': ['e3260c61-0e05-4937-a696-e4dd49bfebdd',
                                '6d3f6b99-3739-41a9-af21-d91f640a2936',
                                '499e5ca1-8b2e-4f2b-b92e-2ae51e4c80a1',
                                'bf272ef9-cb8b-4497-a912-0252ce9b0d3a'],
            'current_module_id': '6d3f6b99-3739-41a9-af21-d91f640a2936',
            'last_reminder_date': '2019-07-18T23:18:03.766Z',
            'last_login_date': '2019-07-18T18:22:42.400Z'}]}
"""
