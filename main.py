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


    def on_trolly(self, trolly: Trolly):
        """Returns the trolly number
        Places the product on a trolly.
        """
        pass

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
        self.shelf.number = shelf
        self.shelf.compartment_num = compartment
        
        pass
    
    def in_bin(self, bin: Bin, product: Product):
        """
        Places the products ordered onto the bin
        """
        pass


class Trolly:
    """Trolly Class
    Carries product from truck to shelf and compartment
    """
    
    def __init__(self):
        self.item = []

    def add(self,item: Product):
        self.item.append(item.barcode)

    def remove(self, item: Product):
        self.item.remove(item.barcode)

class Shelf:
    """Shelf Class
    Holds the product in a specific shelf and compartment location (number)
    """
    def __init__(self):
        self.compartment = {
            "B3": []
        }
    def add(self, compartment, item):
        self.compartment[compartment].append(item)


class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self, number: int):
        pasself.bin_number = number




# class Product:
#     """
#     This the class for the products coming in 
#     """


#     def __init__(self, barcode: int):
#         """
#         Creates the product (barcode)
#         """
#         self.barcode = barcode

    
#     def on_shelf(self, shelf: int, compartment: int):
#         """Returns the shelf number
#         Places the product on a bin.
#         """
#         self.shelf.number = shelf
        
#         self.shelf.compartment_num = compartment


#     def in_bin(self, bin_number: int):
#         """Removes product from trolly and places it into a bin, with a shelf
#         and compartment number
#         Args:
#             bin: bin number, location
#             shelf: shelf number, location
#             compartment: compartment number, location
#         Return:
#             New location of product
#         """
#         self.bin_number = bin_number
        
