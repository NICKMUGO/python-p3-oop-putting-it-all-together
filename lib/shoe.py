class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"
    def size(self):
        return self._size
    def size(self, value):
        if  isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
stan_smith = Shoe("Adidas", 9)
stan_smith.brand

