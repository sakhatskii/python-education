from dataclasses import dataclass

class Cars:
    def __init__(self, brand, model, vin, horsepower):
        self.brand = brand
        self.model = model
        self.vin = vin
        self.horsepower = horsepower

ford = Cars("Ford", "Focus", "Z6F5XXEEC5FY02163", 125)
print(f"Модель машины: {ford.brand}, мощность: {ford.horsepower} л.с.")


@dataclass
class DataCars:
    brand: str
    model: str
    vin: str
    horsepower: int

bmw = DataCars(brand="BMW", model="X3", vin="VF3WCKFUC33681468", horsepower=260)
print(f"Модель машины: {bmw.brand}, мощность: {bmw.horsepower} л.с.")
