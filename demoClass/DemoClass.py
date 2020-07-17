class LearningMethods():

    def __init__(self):
        print("I am special method")

    def car(self):
        print("THis is car method ")

    @classmethod
    def bike(cls):
        print("I am class method")

    @staticmethod
    def cycle():
        print("i am static method")

#
# l = LearningMethods()
#
# l.cycle()

# LearningMethods.bike()
# LearningMethods.cycle()