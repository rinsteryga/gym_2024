class Workout:
    """Класс тренировок"""

    def __init__(self, date, weight, height, exercises=None):
        """Инициализация объектов тренировки"""
        if exercises is None:
            exercises = []
        self.date = date
        self.weight = float(weight)
        self.height = float(height)
        self.exercises = exercises

    def add_exercise(self, exercise):
        """Добавление упражнения в тренировку"""
        self.exercises.append(exercise)

    def date_to_last(self):
        """Возврат данных последней тренировки"""
        return f"Последняя тренировка датирована {self.date} \n\n" \
               f"Вес - {self.weight}, Рост - {self.height}, ИМТ - {round(self.weight / (self.height / 100) ** 2, 2)}" \
               f"\n\nУпражнение: подходы, повторения, вес\n\n"

    def date_to_all(self):
        """Возврат данных для сохранения всех тренировок"""
        return f"{'-' * 30}\nТренировка {self.date}\n{'-' * 30}\n\n" \
               f"Вес - {self.weight}, Рост - {self.height}, ИМТ - {round(self.weight / (self.height / 100) ** 2, 2)}" \
               f"\n\nУпражнение: подходы, повторения, вес\n\n"

    def to_out_exercises(self):
        """Возврат всех упражнений для сохранения"""
        result = ""
        for exercise in self.exercises:
            result += exercise.to_string_to_out() + "\n"
        return result + '\n'

