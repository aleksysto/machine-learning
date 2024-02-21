import math
from datetime import datetime
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def calculate_days_passed(self):
        # Calculate the days that have passed from the user's birth date to today
        # You can use a library like datetime to perform this calculation
        # For example:
        # from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        self.days_passed = (today - birth_date).days

    def calculate_vital_signs(self):
        # Calculate the physical, emotional, and intellectual waves
        self.physical_wave = math.sin((2*math.pi/23)*self.days_passed)
        self.emotional_wave = math.sin((2*math.pi/28)*self.days_passed)
        self.intellectual_wave = math.sin((2*math.pi/33)*self.days_passed)

    def greet_and_inform(self):
        # Greet the person and inform them of their vital signs
        print(f"Hello, {self.name}! Here are your vital signs:")
        print(f"Physical wave: {self.physical_wave}")
        print(f"Emotional wave: {self.emotional_wave}")
        print(f"Intellectual wave: {self.intellectual_wave}")

    def check_physical_wave(self):
        if self.physical_wave < -0.5:
            print("Something uplifting message related to physical wellbeing...")
            # Calculate tomorrow's physical wave
            tomorrow_physical_wave = math.sin((2*math.pi/23)*(self.days_passed+1))
            # Check if tomorrow's physical wave is higher than today's
            if tomorrow_physical_wave > self.physical_wave:
                print("Don't worry, tomorrow's physical wellbeing will be better!")
        elif self.physical_wave > 0.5:
            print("Congratulations on physical wellbeing...")
    def check_emotional_wave(self):
        if self.emotional_wave < -0.5:
            print("Something uplifting message related to emotional wellbeing...")
            # Calculate tomorrow's emotional wave
            tomorrow_emotional_wave = math.sin((2*math.pi/28)*(self.days_passed+1))
            # Check if tomorrow's emotional wave is higher than today's
            if tomorrow_emotional_wave > self.emotional_wave:
                print("Don't worry, tomorrow's emotional wellbeing will be better!")
        elif self.emotional_wave > 0.5:
            print("Congratulations on emotional wellbeing...")
    def check_intellectual_wave(self):
        if self.intellectual_wave < -0.5:
            print("Something uplifting message related to intellectual wellbeing...")
            # Calculate tomorrow's intellectual wave
            tomorrow_intellectual_wave = math.sin((2*math.pi/33)*(self.days_passed+1))
            # Check if tomorrow's intellectual wave is higher than today's
            if tomorrow_intellectual_wave > self.intellectual_wave:
                print("Don't worry, tomorrow's intellectual wellbeing will be better!")
        elif self.intellectual_wave > 0.5:
            print("Congratulations on intellectual wellbeing...")
# Create a Person object and use it to calculate vital signs and check wellbeing
name = input("What is your name? ")
dob = input("What is your date of birth (YYYY-MM-DD)? ")
person = Person(name, dob)
person.calculate_days_passed()
person.calculate_vital_signs()
person.greet_and_inform()
person.check_physical_wave()
person.check_emotional_wave()
person.check_intellectual_wave()