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
    This the class for the products coming in 
    """


    def __init__(self, barcode: int):
        """
        Creates the product (barcode)
        """
        self.barcode = barcode


    def on_trolly(self, trolly: int):
        """Returns the trolly number
        Places the product on a trolly.
        """

    def in_bin(self, bin: int, shelf: int, compartment: int):
        """Removes product from trolly and places it into a bin, with a shelf
        and compartment number
        Args:
            bin: bin number, location
            shelf: shelf number, location
            compartment: compartment number, location
        Return:
            New location of product
        """
class Cart:
    
    def __init__(self):
        self.item = []
    def add(self,item):
        self.item.append(item)
    def remove(self, item):
        self.item.remove(item)

class Item:
    """
    Should hold the item
    """
    def __init__(self, name: str, barcode: int):
        self.name = name
        self.barcode = barcode

class Shelf:
    def __init__(self):
        self.compartment = {
            "B3": []
        }
    def add(self, compartment, item):
        self.compartment[compartment].append(item)
