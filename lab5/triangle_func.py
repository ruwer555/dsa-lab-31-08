class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    Возвращает тип треугольника:
    - 'equilateral' (равносторонний)
    - 'isosceles' (равнобедренный)
    - 'nonequilateral' (разносторонний)

    Если стороны некорректны, выбрасывает IncorrectTriangleSides.
    """
    # Проверка типов 
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        raise IncorrectTriangleSides("Стороны должны быть числами")

    # Проверка на положительность
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными")

    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника")

    # Определение типа
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"