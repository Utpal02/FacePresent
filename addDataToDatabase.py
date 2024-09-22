import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://ml-lab-adb0e-default-rtdb.firebaseio.com/'})

ref = db.reference('Students')

data = {
    "12111001":
        {
            "name": "Elon Musk",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111002":
        {
            "name": "Emily Blunt",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111007":
        {
            "name": "Ayush Shukla",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111014":
        {
            "name": "Rishabh Sinha",
            "major": "Machine Learning",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111017":
        {
            "name": "Utpal Tiwari",
            "major": "AI ",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111032":
        {
            "name": "Devvrat Gupta",
            "major": "Development",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111037":
        {
            "name": "Pratik Gupta",
            "major": "Blockchain",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12111051":
        {
            "name": "Aashish Negi",
            "major": "Machine Learning",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)
