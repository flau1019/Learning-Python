class Student:

    

    def __init__(self, name, major, gpa):
        self.classname = name
        self.classmajor = major
        self.classgpa = gpa

    def on_honor_roll(self):
        if self.classgpa >= 3.5:
            return True
        else:
            return False
    
    def goodGPA(self):
        if self.classgpa >= 3:
            return True
        else:
            return False