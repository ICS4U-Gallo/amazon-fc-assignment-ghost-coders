import json
from typing import List

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

    def __init__(self, barcode: int):
        """
        Creates the product (barcode)
        Args:
            barcode: int
        """
        self.barcode = barcode


class Trolly:
    """
    Placed product onto trolly to be moved onto shelf
    """
    def __init__(self):
        pass

    def add(self, product: Product):
        with open("trolly.json", "r") as f:
            storage = json.load(f)

        storage.append(product)

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
    def __init__(self, shelf_num: str, compartment_num: int):
        self.shelf_num = shelf_num
        self.compartment_num = compartment_num


    def add(self, shelf_num: str, compartment_num: int, product: Product):
        with open("Compartment.json", 'r') as f:
            storage = json.load(f)
        
        storage[shelf_num][compartment_num].append(product.barcode)

        with open("Compartment.json", "w") as f:
            json.dump(storage, f)

    def remove(self, product: Product):
        with open("Compartment.json", "r") as f:
            storage = json.load(f)
        
        for key, value in storage.items():
            for key, value in value.items():
                for barcode in value:
                    if product.barcode in value:
                        value.remove(product.barcode)
        
        with open("trolly.json", "w") as f:
            json.dump(storage, f)


class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self, bin_num: int):
        self.bin_num = bin_num

    def add(self, bin: Bin, product: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)
        
        storage[bin_num].append(product.barcode)

        with open("bin.json", "w") as f:
            json.dump(storage, f)

    def remove(self, item: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)
        
        for key, value in storage.items():
            for bin_list in value:
                bin_list.clear()


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
        return "The product(s) has been shipped"

    
def main():
    shirt = Product(12345)
    pants = Product(98765)

    trolly = Trolly()

    trolly.add(shirt)



if __name__ == "__main__":
    main()
