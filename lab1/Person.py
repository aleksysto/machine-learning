from datetime import datetime
import math
date_format: str = "%Y-%m-%d"

class Person():
    def __init__(self) -> None:
        self.name: str = ""
        self.dob: str = ""
        self.today_date: str = datetime.now()
    def set_dob(self: object, date_str: str) -> None:
        new_date = datetime.strptime(date_str, date_format)
        self.dob = new_date
    def ask_credentials(self: object) -> None:
        print("Enter your name: ")
        self.name: str = input()
        print("Enter your date of birth (yyyy-mm-dd): ")
        date: str = input()
        self.set_dob(date)
    
    def calculate_days(self: object) -> int:
        return (self.today_date - self.dob).days

    def calculate_vitals(self: object, days: int) -> [float]:
        phys_wave: float = math.sin(((math.pi * 2) / 23) * days)
        emotion_wave: float = math.sin(((math.pi * 2) / 28) * days)
        smart_wave: float = math.sin(((math.pi * 2) / 33) * days)
        return [phys_wave, emotion_wave, smart_wave]
    
    def greet(self: object) -> None:
        print("Hello, " + self.name + "!")
        print(f"You have been successfully staying alive for {self.calculate_days()}")
        print("Your vital signs are: ")

        arr: [float] = self.calculate_vitals(self.calculate_days())
        wave_types: [str] = ["Physical", "Emotional", "Intellectual"]

        print(f"Physical wave: {arr[0]} \nEmotional wave: {arr[1]} \nIntellectual wave: {arr[2]}")

        for idx, wave in enumerate(arr):
            if wave > 0.5:
                print(f"Congratulations! Your {wave_types[idx]} wave is high!")
            elif wave < -0.5:
                print(f"Your {wave_types[idx]} wave is low. I'm here if you need to talk. In the meantime I'll see if it gets any better tomorrow")
                tomorrow_vitals = self.calculate_vitals(self.calculate_days() + 1)
                if tomorrow_vitals[idx] > wave:
                    print("Don't worry! It'll get better tomorrow, I promise!")
                elif tomorrow_vitals[idx] < wave:
                    print("It's rope chair time!!! B)")

new_person: object = Person()
new_person.ask_credentials()
new_person.greet()
