class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"I am a {self.model} model robot.")
        print(f"My purpose is: {self.purpose}.")

    def greet(self):
        print("Nice to meet you! 🤖")


my_robot = Robot("RoboMax", "X69", "helping humans with daily tasks")

my_robot.introduce()
my_robot.greet()
