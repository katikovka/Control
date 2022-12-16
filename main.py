# 16
"""
Суперкласс сотрудник с методом повышения оклада (округляет до копеек)
метод str для вывода в формате "Атрибут:объект.атрибут" по оодной записи на каждой строке
Подкласс Менеджер, наследубщий Сотрудник, переопределяет метод повышения оклада так, что увеличивается ещё плюс с его доп бонусами

Иван_менеджер с начальный окладом 1700
повысить оклад на стандартной 0.335 и бонусом за менеджера 0.25
Вывести инфу мотрудника
"""


class Assistant:
    def __init__(self, name, post=None, salary=0):
        self.salary = salary
        self.post = post
        self.name = name

    def add_salary(self, add):   # повышение оклада
        self.salary *= add
        print(f"Оклад сотрудника {self.name} повышен на 30%, составляет {self.salary}")

    def __str__(self):  # метод стр для вывода "Атрибут:объект.атрибут"
        res = f"Сотрудник: {self.name}\n"
        res += f"Должность: {self.post}\n"
        res += f"Оклад: {self.salary}\n"
        print(res)


class Manager(Assistant):
    def __init__(self, name, post=None, salary=0, bonus=0):
        super().__init__(name, post, salary)
        self.bonus = bonus

    def add_salary(self, add):
        super().add_salary(add)
        # добавляем боннус
        self.salary += self.bonus
        print(f"Сотрудники дали бонус, оклад составил {self.salary}")

    def __str__(self):
        print(super().__str__()+f"Бонус: {self.bonus}\n")


ivan_manager = Manager("Иван", "Менеджер", 1700)
ivan_manager.add_salary(0.335)
print(ivan_manager)
