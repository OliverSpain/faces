from random import randint

class Bar:
    def __init__(self):
        self.base_faces = ["R", "L"]
        self.add_faces = ["F", "I", "D"]

    def generate(self):
        self.final_faces = []
        for i in range(randint(8,12)):
            self.face = "{a}{b}".format(a=self.base_faces[randint(0,1)], b=self.add_faces[randint(0,2)])
            if randint(0,3) == 3: self.face = "AF"
            self.final_faces.append(self.face)
        return self.final_faces

    def formatting(self):
        self.separator = " "
        self.formatted_list = self.separator.join(self.generate())
        return self.formatted_list

foo = Bar()
user_input = "Y"
while user_input == "Y":
    print(foo.formatting())
    user_input = input("run again? (Y/N): ")
