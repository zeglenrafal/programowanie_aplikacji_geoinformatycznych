class Licznik_3:
    def __init__(self):
        self.x = 0

    def __call__(self):
        self.x += 1
        return self.x