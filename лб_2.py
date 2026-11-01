print("Завдання 1")
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        return "Транспортний засіб рухається."

    def __str__(self):
        return f"Марка: {self.brand}, швидкість: {self.speed} км/год"


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def move(self):
        return f"Автомобіль {self.brand} їде дорогою зі швидкістю {self.speed} км/год."


class Motorcycle(Vehicle):
    def __init__(self, brand, speed, engine_volume):
        super().__init__(brand, speed)
        self.engine_volume = engine_volume

    def move(self):
        return f"Мотоцикл {self.brand} рухається зі швидкістю {self.speed} км/год."


class Truck(Vehicle):
    def __init__(self, brand, speed, load_capacity):
        super().__init__(brand, speed)
        self.load_capacity = load_capacity

    def move(self):
        return f"Вантажівка {self.brand} перевозить вантаж до {self.load_capacity} тонн."

vehicles = [
    Car("Toyota", 120, 4),
    Motorcycle("Honda", 150, 600),
    Truck("Volvo", 90, 20)
]

print("Поліморфна демонстрація:")
for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle)

print("Перевірка типів:")
print(isinstance(vehicles[0], Car))
print(isinstance(vehicles[0], Vehicle))
print(issubclass(Car, Vehicle))
print(issubclass(Truck, Motorcycle))

print("\nЗавдання 2")
class TemperatureSensor:
    def __init__(self, temperature, location):
        self.__temperature = 0
        self._location = location
        self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Температура повинна бути числом.")

        if not -50 <= value <= 100:
            raise ValueError("Температура повинна бути від -50 до 100 °C.")

        self.__temperature = value

    @property
    def temperature_fahrenheit(self):
        return self.__temperature * 9 / 5 + 32

    def __str__(self):
        return (
            f"Датчик: {self._location}, "
            f"температура: {self.temperature} °C"
        )

sensor = TemperatureSensor(25, "Кімната 101")

print("Початкові дані:")
print(sensor)
print("Температура у Фаренгейтах:", sensor.temperature_fahrenheit)

sensor.temperature = 30
print("Після зміни температури:")
print(sensor)
print("Температура у Фаренгейтах:", sensor.temperature_fahrenheit)

print("Перевірка помилкових значень:")

try:
    sensor.temperature = "гаряче"
except TypeError as error:
    print("Помилка:", error)

try:
    sensor.temperature = 150
except ValueError as error:
    print("Помилка:", error)

print("Перевірка приватного атрибута:")

try:
    print(sensor.__temperature)
except AttributeError as error:
    print("Помилка доступу:", error)

print("Доступ через name mangling:",
      sensor._TemperatureSensor__temperature)

print("Місце встановлення:", sensor._location)

print("\nЗавдання 3")
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Вектор ({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Vector2D(self.x * number, self.y * number)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return abs(self) < abs(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Індекс повинен бути 0 або 1")

    def __len__(self):
        return 2

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("Представлення:")
print(str(v1))
print(repr(v1))

print("Арифметичні операції:")
print("Додавання:", v1 + v2)
print("Віднімання:", v1 - v2)
print("Множення на число:", v1 * 2)

print("Порівняння:")
print("Вектори рівні:", v1 == v2)
print("Перший вектор коротший:", v1 < v2)

print("Інші операції:")
print("Довжина першого вектора:", abs(v1))
print("Координата X:", v1[0])
print("Координата Y:", v1[1])
print("Кількість координат:", len(v1))

print("\nЗавдання 4")
from abc import ABC, abstractmethod
class PaymentMethod(ABC):

    @property
    @abstractmethod
    def provider(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def get_receipt(self, amount):
        return f"Квитанція: {amount:.2f} грн, спосіб: {self.provider}"


class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    @property
    def provider(self):
        return "Банківська картка"

    def pay(self, amount):
        return f"Оплачено {amount:.2f} грн карткою ****{self.card_number[-4:]}."

    def refund(self, amount):
        return f"Повернено {amount:.2f} грн на банківську картку."


class MobilePayment(PaymentMethod):
    def __init__(self, phone):
        self.phone = phone

    @property
    def provider(self):
        return "Мобільний платіж"

    def pay(self, amount):
        return f"Оплачено {amount:.2f} грн через номер {self.phone}."

    def refund(self, amount):
        return f"Повернено {amount:.2f} грн на мобільний рахунок."


class Logger:
    def log(self, message):
        print("[Журнал]", message)


class PaymentValidator:
    def __init__(self, limit):
        self.limit = limit

    def check(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Сума повинна бути числом.")

        if amount <= 0 or amount > self.limit:
            raise ValueError("Некоректна сума платежу.")

        return True


class PaymentService:
    def __init__(self, payment_method, logger, validator):
        self.payment_method = payment_method
        self.logger = logger
        self.validator = validator

    def process_payment(self, amount):
        self.validator.check(amount)
        result = self.payment_method.pay(amount)
        self.logger.log(result)
        return result

    def process_refund(self, amount):
        self.validator.check(amount)
        result = self.payment_method.refund(amount)
        self.logger.log(result)
        return result


print("Перевірка абстрактного класу:")
try:
    payment = PaymentMethod()
except TypeError as error:
    print("Помилка:", error)


logger = Logger()
validator = PaymentValidator(10000)

card = CardPayment("1234567812345678")
mobile = MobilePayment("+380501234567")

payment_methods = [card, mobile]

print("Поліморфна демонстрація:")
for method in payment_methods:
    print("Спосіб оплати:", method.provider)
    print(method.pay(500))
    print(method.get_receipt(500))

print("Робота системи з карткою:")
card_service = PaymentService(card, logger, validator)
card_service.process_payment(1500)
card_service.process_refund(300)

print("Робота системи з мобільним платежем:")
mobile_service = PaymentService(mobile, logger, validator)
mobile_service.process_payment(700)

print("\nЗавдання 5")
class SecurityMonitor:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

    def detect_event(self, event):
        print("[СИСТЕМА] Виявлено подію:", event)
        self.notify(event)


class EmailAlert:
    def update(self, event):
        print("[EMAIL] Надіслано повідомлення про:", event)


class SecurityLogger:
    def update(self, event):
        print("[LOG] Записано подію:", event)


class IncidentCounter:
    def __init__(self):
        self.count = 0

    def update(self, event):
        self.count += 1
        print("[ЛІЧИЛЬНИК] Кількість інцидентів:", self.count)


class ThreatBlocker:
    def update(self, event):
        print("[ЗАХИСТ] Перевірка та блокування загрози:", event)


monitor = SecurityMonitor()

email = EmailAlert()
logger = SecurityLogger()
counter = IncidentCounter()

monitor.subscribe(email)
monitor.subscribe(logger)
monitor.subscribe(counter)

monitor.detect_event("Виявлено багаторазові невдалі спроби входу")
monitor.detect_event("Підозріле мережеве з'єднання")

print("Додавання нового підписника:")

blocker = ThreatBlocker()
monitor.subscribe(blocker)

monitor.detect_event("Виявлено спробу несанкціонованого доступу")

print("Видалення підписника EmailAlert:")
monitor.unsubscribe(email)

monitor.detect_event("Виявлено підозрілу активність")
