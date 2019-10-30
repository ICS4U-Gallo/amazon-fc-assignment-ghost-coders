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
    Placed product into a trolly with a trolly number. 
    """
    trolly_list = []
    def __init__(self, trolly_num: int):
        self.trolly_num = trolly_num

    def add_product(self, product: Product):
        Trolly.trolly_list.append(product)
     
    def delate_product(self, barcode: int, item: Product):
        for item.barcode in Trolly.trolly_list:
            if item.barcode == barcode:
                Trolly.trolly_list.remove(item)
    
    def __init__(self):
        self.trolly = []

    def add(self,item: Product):
        self.trolly.append(item.barcode)

    def remove(self, item: Product):
        self.trolly.remove(item.barcode)


class Shelf:
    """Shelf Class
    Holds the product in a specific shelf and compartment location (number)
    """
    def __init__(self, shelf_num: str, compartment_num: int):
        self.shelf_num = shelf_num
        self.compartment_num = compartment_num


    def add(self, shelf_num: str, compartment_num: int, item: Product):
        with open("Compartment.json", 'r') as f:
            storage = json.load(f)
        
        storage[shelf_num][compartment_num].append(item.barcode)

        with open("Compartment.json", "w") as f:
            json.dump(storage, f)

    def remove(self, item: Product):
        with open("Compartment.json", "w") as f:
            storage = json.load(f)
        
        for key in storage.values():
            # for key


class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self, number: int):
        self.number = number

    def add(self, bin_num: int, item: Product):
        pass

    def remove(self, item: Product):
        pass


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
    
    def shipment(self):
        return "Product has been shipped."
    
def main():
    pass

if __name__ == "__main__":
    main()
