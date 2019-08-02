import string
import random


class Robot(object):
    robot_names = []

    def __init__(self):
        # Name is generated when instance is created
        self.name = self.generate_robot_name()

    def generate_robot_name(self):
        # Pulling uppercase letters from String library
        # Name is generated and added to list if not there
        letters = string.ascii_uppercase
        generated_name = "{0}{1}{2}".format(
            random.choice(letters),
            random.choice(letters),
            random.randint(100, 999)
        )

        if generated_name not in Robot.robot_names:
            Robot.robot_names.append(generated_name)
            return generated_name

    def reset(self):
        self.name = self.generate_robot_name()
