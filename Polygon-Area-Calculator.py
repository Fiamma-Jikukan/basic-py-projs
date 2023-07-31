

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # print(self.height * self.width)
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = []
        i = 0
        while i < self.height: 
            pic.append("*" * self.width ) 
            i = i + 1

        return "\n".join(pic)
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())
        


class Square(Rectangle):
    def __init__(self, length):
        self.set_height(length)
        self.set_width(length)
    
    def __str__(self):
        return f"Square(side={self.height})"

    def set_width(self, length):
        self.width = length
        self.height = length


    def set_height(self, length):
        self.height = length
        self.width = length
    
    def set_side(self, length):
        self.width = length
        self.height = length
    
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

# rec = Rectangle(4, 10)

# sqr = Square(4)

# print(rec.get_amount_inside(sqr))