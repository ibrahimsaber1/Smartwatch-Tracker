# 🏃🏽‍♀️ Smartwatch Workout Tracker

This project simulates how a **smartwatch** tracks and logs various workouts like running, swimming, and general activities. It showcases how wearable devices may internally model and compute information like duration, calories burned, elevation gain, and GPS-based tracking.

---

## 🧠 Purpose

This code was created to provide a simplified yet practical example of how smartwatches log workouts. It demonstrates the use of object-oriented programming (OOP), datetime parsing, and real-world data handling like GPS coordinates and workout intensity.

---

## 🚀 Features

- **Workout Base Class**:  
  - Tracks start/end time, calories, and duration.  
  - Automatically calculates calories burned based on a default rate.

- **RunWorkout Subclass**:  
  - Adds elevation gain and GPS route tracking.  
  - Calculates distance-based calories if route is provided.

- **SwimWorkout Subclass**:  
  - Uses a higher calorie burn rate specific to swimming.  
  - Tracks swimming pace (minutes per 100 yards).

- **Utility Functions**:  
  - `total_calories()`: Sum of calories from all workouts.  
  - `total_elevation()`: Sum of elevation gain from all running workouts.  
  - `total_elapsed_time()`: Sum of time durations from start-end timestamps.

---

## 🧱 OOP Concepts Used

This project uses several important **Object-Oriented Programming (OOP)** principles:

- **Encapsulation**:  
  Each workout is represented as an object (e.g., `Workout`, `RunWorkout`), bundling data and behavior together.

- **Inheritance**:  
  `RunWorkout` and `SwimWorkout` are subclasses of `Workout`. This allows reuse of common functionality while adding or overriding workout-specific behaviors.

- **Polymorphism**:  
  Methods like `get_calories()` behave differently depending on the class, e.g., running may calculate calories via GPS while swimming uses a different burn rate.

- **Abstraction**:  
  The code hides internal details (like how calories are calculated) and provides a simple interface like `get_calories()`.

These OOP concepts make the code **cleaner, modular, and extensible** — allowing easy future enhancements like cycling workouts or heart rate tracking.

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/Ibrahimsaber1/Smartwatch-Tracker.git
cd Smartwatch-Tracker
```
2. Install required packages:

```bash
pip install python-dateutil
```

## 📦 File Structure

```graphql
.
├── Workout.py       # Main codebase
├── Helper.py         # GPS distance calculation helper
└── README.md                # Documentation
```
## 💡 Example Usage

- Here’s a quick example of how to use this code:

```bash
from workout_tracker import Workout, RunWorkout, SwimWorkout, total_calories, total_elapsed_time

# Basic workout (30 mins)
w1 = Workout('1/1/2021 3:30 PM', '1/1/2021 4:00 PM')
print(w1.get_calories())

# Running workout with elevation
r1 = RunWorkout('1/1/2021 1:00 PM', '1/1/2021 2:00 PM', elev=150)
print(r1.get_calories())
print(r1.get_elev())

# Swimming workout (30 mins)
s1 = SwimWorkout('1/1/2021 2:00 PM', '1/1/2021 2:30 PM', pace=2.5)
print(s1.get_calories())

# Total metrics
print(total_calories([w1, r1, s1]))

# Total elapsed time
print(total_elapsed_time([
    ('1/1/2021 2:00 PM', '1/1/2021 2:30 PM'),
    ('1/1/2021 3:00 PM', '1/1/2021 3:45 PM')
]))

```
## 🖨 Sample Output
```bash
Basic workout calories: 100.0
Running workout calories: 200.0
Running workout elevation: 150
Swimming workout calories: 200.0
Total calories for all workouts: 500.0
Total elapsed time: 4500.0 seconds
```

## 📌 Notes

- Calories are computed based on workout duration unless specified manually.

- Running workouts can optionally use GPS routes for more accurate calorie calculation.

- Swimming workouts have their own calorie burn rate and pacing attribute.

- You can easily extend this system to support new types of workouts or data fields.

---

## 🙏 Acknowledgments

This project was inspired by and developed as part of my learning journey through the **[MIT 6.0001 Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)** course.

Special thanks to the MIT OpenCourseWare team and Professor Ana Bell.  
The concepts and structure are based on the lecture series available here:  
📺 [MIT 6.0001 Lecture 20 – Object Oriented Programming](https://www.youtube.com/watch?v=-wyc5FwzkcM&list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB&index=20)

> This code is for educational purposes and reflects my understanding and application of OOP in Python, inspired by MIT's material.
