from dateutil import parser
from lec20_helpers import gpsDistance

# =============================================================================
# Base Workout Class
# =============================================================================
class Workout:
    """A class to keep track of workouts"""

    # Class variable to compute calories burned from workout time
    cal_per_hr = 200
    
    def __init__(self, start, end, calories=None):
        """Creates a workout class;  start and end are strings representing
        the start and end time (e.g., "1/1/2021 1:23 PM");  
        calories is an optional float specifying the calories burned 
        in the workout"""
        self.start = parser.parse(start)  
        self.end = parser.parse(end)
        self.icon = '😓'
        self.kind = 'Workout'
        self.calories = calories

    def get_calories(self):
        """Return the total calories burned in the workout"""
        if self.calories is None:
            # Calculate calories based on workout duration and cal_per_hr
            return Workout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories

    def get_duration(self):
        """Return the duration of the workout, as a datetime.interval object"""
        return self.end - self.start

    def get_start(self):
        """Return the start time of the workout, as a datetime.datetime object"""
        return self.start

    def get_end(self):
        """Return the end time of the workout, as a datetime.datetime object"""
        return self.end

    def set_calories(self, calories):
        """Set the calories of the workout to calories"""
        self.calories = calories

    def set_start(self, start):
        """Set the start time of the workout to the supplied start string"""
        self.start = parser.parse(start)

    def set_end(self, end):
        """Set the end time of the workout to the supplied end string"""
        self.end = parser.parse(end)

    def get_kind(self):
        """Return the kind of the workout as a string"""
        return self.kind

    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false otherwise"""
        return (type(self) == type(other) and 
                self.start == other.start and 
                self.end == other.end and 
                self.kind == other.kind and 
                self.get_calories() == other.get_calories())

    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr =  f"|{'–'*width}|\n"
        retstr += f"|{' '*width}|\n"
        retstr += f"| {self.icon}{' '*(width-3)}|\n"
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"|{' '*width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"{round(self.get_calories(),1)}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"
        retstr += f"|{' '*width}|\n"
        retstr += f"|{'_'*width}|\n"
        return retstr


# =============================================================================
# Running Workout Subclass
# =============================================================================
class RunWorkout(Workout):
    """Subclass of workout to represent a running workout"""
    
    # Class variable for calorie calculation based on distance
    cals_per_km = 100
    
    def __init__(self, start, end, elev=0, calories=None, route_gps_points=None):
        """Create a new instance of a running workout, where start and
        end are strings representing the start and end time of the workout,
        elev is the total elevation gain in the workout in feet,
        calories is an optional number representing the calories 
        burned in the run, and route_gps_points is an optional array 
        of (lat,lon) pairs representing the route of the run"""
        super().__init__(start, end, calories)
        self.icon = '🏃🏽‍'
        self.kind = 'Running'
        self.elev = elev
        self.route_gps_points = route_gps_points

    def get_elev(self):
        """Return the elevation gain of the workout in feet"""
        return self.elev

    def set_elev(self, e):
        """Sets the elevation gain of the workout in feet, to e"""
        self.elev = e

    def get_calories(self):
        """Return the total calories consumed by the workout, derived
        using 1) the GPS points if supplied, 2) calories, if supplied,
        or 3) an estimate of the calories based on the duration"""
        if self.route_gps_points is not None:
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1:]:
                dist += gpsDistance(lastP, p)
                lastP = p
            return dist * RunWorkout.cals_per_km
        else:
            return super().get_calories()

    def __eq__(self, other):
        """Returns true if this workout is equal to another workout, false otherwise"""
        return super().__eq__(other) and self.elev == other.elev


# =============================================================================
# Swimming Workout Subclass
# =============================================================================
class SwimWorkout(Workout):
    """Subclass of workout to represent a swimming workout"""
    
    # Swimming has a higher calorie burn rate
    cal_per_hr = 400
    
    def __init__(self, start, end, pace, calories=None):
        """Create a new instance of a swimming workout, where start and
        end are strings representing the start and end time of the workout,
        pace is the pace of the workout in min/100yd, and calories
        is an optional parameter specifying the calories burned in the workout
        """
        super().__init__(start, end, calories)
        self.icon = '🏊‍'
        self.kind = 'Swimming'
        self.pace = pace
        
    def get_pace(self):
        """Return the pace of the workout"""
        return self.pace
        
    def get_calories(self):
        """Return the total calories burned in the swim workout
           using the SwimWorkout cal_per_hr class variable"""
        if self.calories is None:
            # Calculate calories based on duration and swim-specific cal_per_hr
            return SwimWorkout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories


# =============================================================================
# Utility functions for workout collections
# =============================================================================
def total_calories(workouts):
    """Calculate total calories from a list of workouts"""
    cals = 0
    for w in workouts:
        cals += w.get_calories()
    return cals

def total_elevation(run_workouts):
    """Calculate total elevation gain from a list of running workouts"""
    elev = 0
    for w in run_workouts:
        elev += w.get_elev()
    return elev

def total_elapsed_time(time_tuples):
    """Calculate total elapsed time from a list of time tuples
    
    Args:
        time_tuples: List of tuples (start_time, end_time) where each time is a string
        
    Returns:
        Total elapsed time in seconds
    """
    total = 0
    for start, end in time_tuples:
        start_time = parser.parse(start)
        end_time = parser.parse(end)
        total += (end_time - start_time).total_seconds()
    return total


# =============================================================================
# Example usage
# =============================================================================
if __name__ == "__main__":
    # Create a basic workout
    w_one = Workout('1/1/2021 3:30 PM', '1/1/2021 4:00 PM')
    print(f"Basic workout calories: {w_one.get_calories()}")
    
    # Create a workout with specified calories
    w_two = Workout('1/1/2021 3:35 PM', '1/1/2021 4:00 PM', 300)
    print(f"Specified calorie workout: {w_two.get_calories()}")
    
    # Create a running workout with elevation data
    rw = RunWorkout('1/1/2021 1:00 PM', '1/1/2021 2:00 PM', 200)
    print(f"Running workout calories: {rw.get_calories()}")
    print(f"Running workout elevation: {rw.get_elev()}")
    
    # Create a running workout with GPS route data
    points = [(42.3601, -71.0589), (42.3370, -71.2092)]  # Boston to Newton
    run_with_gps = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 3:57 PM', 100, route_gps_points=points)
    print(f"Running workout with GPS calories: {run_with_gps.get_calories()}")
    
    # Create a swimming workout
    swim = SwimWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM', 2.5)
    print(f"Swimming workout calories: {swim.get_calories()}")
    
    # Calculate totals for a collection of workouts
    workouts = [w_one, w_two, rw, swim]
    print(f"Total calories for all workouts: {total_calories(workouts)}")
    
    # Calculate total time from a list of time ranges
    t1 = '1/1/2021 2:00 PM'
    t2 = '1/1/2021 2:05 PM'
    t3 = '3/12/2021 1:22 PM'
    t4 = '3/12/2021 1:32 PM'
    time_list = [(t1, t2), (t3, t4)]
    print(f"Total elapsed time: {total_elapsed_time(time_list)} seconds")
