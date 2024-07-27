# WRITE YOUR SOLUTION HERE:

class Recording:
    def __init__(self, new_length):
        if new_length >= 0:
            self.__length = new_length
        else:
            raise ValueError("The length must not be below zero")


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, set_length):
        if set_length >= 0:
            self.__length = set_length
        else:
            raise ValueError("The length must not be below zero")

if __name__ == "__main__":
    the_wall = Recording(45)
    print(the_wall.length)
    the_wall.length = -1
    print(the_wall.length)