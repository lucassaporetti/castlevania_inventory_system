import uuid
from src.model.item_model import Item


uuid
Category
Name
Description (notes)
Type
Attributes/Consume
Statistics/Sell
Found
Picture URL


class Weapon(Item):
    @staticmethod
    def of(values: list):
        return Weapon(
            str(values[0]), str(values[1]), str(values[2]),
            Color[values[3]], int(values[4]), Fuel[values[5]],
            str(values[6]), float(values[7]), YesNo(values[8])
        )

    def __init__(self, item_id: str = None, name: str = None, chassis: str = None, color: Color = None,
                 doors: int = None, fuel: Fuel = None, plate: str = None, price: float = None,
                 available: YesNo = YesNo.YES):
        super().__init__(item_id)
        self.name = name
        self.chassis = chassis
        self.color = color
        self.doors = doors
        self.fuel = fuel
        self.plate = plate
        self.price = price
        self.available = available

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {}".format(
            super().__str__(), self.name, self.chassis,
            self.color.name, self.doors, self.fuel.name, self.plate, self.price,
            self.available.name)

    class Builder:
        def __init__(self):
            self.uuid = str(uuid.uuid4())
            self.name = None
            self.chassis = None
            self.color = None
            self.doors = None
            self.fuel = None
            self.plate = None
            self.price = None
            self.available = YesNo.YES

        def with_name(self, name: str):
            self.name = name
            return self

        def with_chassis(self, chassis: str):
            self.chassis = chassis
            return self

        def with_color(self, color: Color):
            self.color = color
            return self

        def with_doors(self, doors: int):
            self.doors = doors
            return self

        def with_fuel(self, fuel: Fuel):
            self.fuel = fuel
            return self

        def with_plate(self, plate: str):
            self.plate = plate
            return self

        def with_price(self, price: float):
            self.price = price
            return self

        def with_available(self, available: YesNo):
            self.available = available
            return self

        def build(self):
            return Car(
                self.uuid, self.name, self.chassis, self.color, self.doors, self.fuel, self.plate, self.price,
                self.available
            )
