class inmate:

    def __init__(self, name, age, how_serious):
        self.name = name
        self.age = int(age)
        self.how_serious = how_serious

#This is object for function
    def on_honour(self):
        if self.age >= 20:
            return True
        else:
            return False


