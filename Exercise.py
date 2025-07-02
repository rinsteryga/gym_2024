class Exercise:
    """Класс упражнений"""
    def __init__(self, name, sets, reps, weight):
        """Инициализация объектов упражнения"""
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight

    def to_string(self):
        """Возвращение строкового представления упражнения"""
        return f"{self.name.replace('_', ' ')}: {self.sets} x {self.reps} \t {self.weight} кг"

    def to_string_to_out(self):
        """Возвращение строки для записи в файл"""
        return f"{self.name}: {self.sets} x {self.reps} {self.weight} кг"

