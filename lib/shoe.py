class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self._size=None
        self.size = size

    def get_size(self):
        return self._size
    def cobble(self):
        self.condition="New"
        print("Your shoe is as good as new!")


    def set_size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")

    size=property(get_size,set_size)




adidas = Shoe("Adidas", "25")
print(adidas.size)
print(adidas.brand)
adidas.cobble()