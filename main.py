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
    """

    def __init__(self, barcode: int):
        """
        Creates the product (barcode)
        """
        self.barcode = barcode


    def on_cart(self, cart: Cart):
        """Returns the trolly number
        Places the product on a trolly.
        """

    def on_shelf(self, shelf: Shelf, compartment: shelf.compartment):
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
    """
    Cart Class
    """
    
    def __init__(self):
        self.item = []
    def add(self,item):
        self.item.append(item)
    def remove(self, item):
        self.item.remove(item)


class Shelf:
    def __init__(self):
        self.compartment = {
            "B3": []
        }
    def add(self, compartment, item):
        self.compartment[compartment].append(item)
