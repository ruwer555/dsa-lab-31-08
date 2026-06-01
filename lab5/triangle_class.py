from triangle_func import IncorrectTriangleSides, get_triangle_type


class Triangle:
    """
    Класс, описывающий треугольник.
    """

    def __init__(self, a, b, c):

        # Переиспользование
        get_triangle_type(a, b, c)  
        self.b = b
        self.c = c

    def triangle_type(self):
        """Тип треугольника."""
        return get_triangle_type(self.a, self.b, self.c)

    def perimeter(self):
        """Периметр треугольника."""
        return self.a + self.b + self.c