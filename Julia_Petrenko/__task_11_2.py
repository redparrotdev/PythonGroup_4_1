# Добавьте для класса Color возможность сложения и вычитания с другим цветом (воспользуйтесь встроенными методами).
# Так же добавьте строковое представление для класса вида "R: 213,G: 175,B: 54".
# Учтите, что значение для каждого цвета не может быть больше 255 и меньше 0.
# * дополнительно добавить возможность получения цвета по индексу (0-2).
# ** дополнительно добавить возможность сравнения цветов на равенство и не равенство

class Color:

    def __init__(self, r: int, g: int, b:int):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        r_res: int
        g_res: int
        b_res: int

        if self.r + other.r > 255:
            r_res = 0
        else:
            r_res = self.r + other.r

        if self.g + other.g > 255:
            g_res = 0
        else:
            g_res = self.g + other.g

        if self.b + other.b > 255:
            b_res = 0
        else:
            b_res = self.b + other.b

        return Color(r_res, g_res, b_res)

    def __sub__(self, other):
        r_res: int
        g_res: int
        b_res: int

        if self.r - other.r < 0:
            r_res = 0
        else:
            r_res = self.r - other.r

        if self.g - other.g < 0:
            g_res = 0
        else:
            g_res = self.g - other.g

        if self.b - other.b < 0:
            b_res = 0
        else:
            b_res = self.b - other.b

        return Color(r_res, g_res, b_res)

    def __str__(self):
        return "R: " + str(self.r) + ",G: " + str(self.g) + ",B: " + str(self.b)

    @property
    def color(self):
        return self.r, self.g, self.b

    def __eq__(self, other):
        if self.r == other.r and self.g == other.g and self.b == other.b:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.r != other.r or self.g != other.g or self.b != other.b:
            return True
        else:
            return False


color1 = Color(245, 10, 10)
color2 = Color(20, 20,20)
color3 = color1 + color2

print(color3)
print(color3.color[1])
print(color1 == color2)
print(color1 != color2)






