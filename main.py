import json

"""
Product
====
Barcode -> object
Trolly number
Bin number
Shelf number
Compartment number
"""


class Product:
    """
    Product Class

    Attributes:
        barcode = int
    """

    def __init__(self, barcode: str):
        """
        Creates the product (barcode)
        Args:
            barcode: str
        """
        self.barcode = barcode

    def __str__(self):
        return f"{self.barcode}"


class Trolly:
    """
    Placed product onto trolly to be moved onto shelf
    """
    def __init__(self):
        pass

    def add(self, product: Product):
        with open("trolly.json", "r") as f:
            storage = json.load(f)

        storage.append(product.barcode)

        with open("trolly.json", "w") as f:
            json.dump(storage, f)

    def remove(self, product: Product):
        with open("trolly.json", "r") as f:
            storage = json.load(f)

        if product.barcode in storage:
            storage.remove(product.barcode)

        with open("trolly.json", "w") as f:
            json.dump(storage, f)


class Shelf:
    """Shelf Class
    Holds the product in a specific shelf and compartment location (number)
    """
    def __init__(self):
        pass

    def add(self, shelf_num: str, compartment_num: int, product: Product):
        with open("Compartment.json", 'r') as f:
            storage = json.load(f)

        storage[shelf_num][compartment_num].append(product.barcode)

        with open("Compartment.json", "w") as f:
            json.dump(storage, f)

    def remove(self, product: Product):
        with open("Compartment.json", "r") as f:
            storage = json.load(f)

        for value in storage.values():
            for value2 in value.values():
                for barcode in value2:
                    if product.barcode == barcode:
                        value2.remove(product.barcode)

        with open("Compartment.json", "w") as f:
            json.dump(storage, f)


class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self):
        pass

    def add(self, product: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)

        storage.append(product.barcode)

        with open("bin.json", "w") as f:
            json.dump(storage, f)

    def remove(self, product: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)

        storage.clear()

        with open("bin.json", "w") as f:
            json.dump(storage, f)


class Packaging:
    """Packaging Class
    Prepares the products (the order) for shipment to customer
    Attributes:
        box_type = small, medium, large, fragile
        address = where product is sent to
        truck = transportation, license plate
    """

    def __init__(self, box_type: str, address: str, truck: str):
        self.box_type = box_type
        self.address = address
        self.truck = truck

    def __str__(self):
        return "The order has been shipped"
        with open("bin.json", "r") as f:
            storage = json.load(f)

        return f"""The order has been shipped.
        {str(storage)}"""


def main():
    shirt = Product(12345)
    pants = Product(98765)

    the_bin = Bin()
    packaging = Packaging("small", "12 Blue", "H3JO 293")

    the_bin.add(shirt)

    print(shelf)


if __name__ == "__main__":
    main()
