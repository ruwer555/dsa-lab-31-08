from triangle_func import IncorrectTriangleSides, get_triangle_type


class Triangle:
    """
    Класс, описывающий треугольник.
    """

    def __init__(self, a, b, c):

        # Переиспользуем проверку из функции
        get_triangle_type(a, b, c)  # выбросит исключение при ошибке
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        """Возвращает тип треугольника."""
        return get_triangle_type(self.a, self.b, self.c)

    def perimeter(self):
        """Возвращает периметр треугольника."""
        return self.a + self.b + self.c