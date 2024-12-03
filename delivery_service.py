"""Основной файл, номер с Яндекс Контест: 128966812."""


def check_platform(limit: int, robots_mass: list) -> int:
    """Функция, который возвращает кол-во платформ."""
    count_platform: int = 0  # Счётчик платформ
    left_pointer: int = 0  # Индексы начиная слева
    right_pointer: int = len(robots_mass) - 1   # Индексы начиная справа

    while left_pointer <= right_pointer:
        # Проверяем, могут ли оба робота поместиться на одной платформе
        if robots_mass[left_pointer] + robots_mass[right_pointer] <= limit:
            left_pointer += 1  # Переходим к следующему роботу с левой стороны
        # В любом случае правый робот помещается на платформу
        right_pointer -= 1
        count_platform += 1  # Увеличиваем счётчик платформ

    return count_platform


robot_string: str = input()
limit_string: int = int(input())
robot_split: list = list(map(int, robot_string.split()))

print(check_platform(limit_string, sorted(robot_split)))