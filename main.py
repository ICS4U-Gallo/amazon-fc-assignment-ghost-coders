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
        pass
    
    def in_bin(self, bin: Bin, : Product):product
        """
        Places the products ordered onto the bin
        """
        pass


class Trolly:
    """
    Placed product into a trolly with a trolly number. 
    """
    trolly_list = []
    def __init__(self, trolly_num: int):
        self.trolly_num = trolly_num

    def add_product(self, product: Product):
        Trolly.trolly_list.append(product)
     
    def delate_product(self, barcod: int):
        for item.barcode in Trolly.trolly_list:
            if item.barcode == barcode:
                Trolly.trolly_list.remove(item)
    
    def get_trolly(self):
        return Trolly.trolly_list


class Shelf:
    """Shelf Class
    Holds the product in a specific shelf and compartment location (number)
    """
    def __init__(self):
        self.compartment = {}


    def add(self, compartment_num, item):
        if compartment_num in self.compartment.keys():
            self.compartment[compartment_num].append(item)
        else:
            self.compartment[compartment_num] = []
            self.compartment[compartment_num].append(item)

class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self, number: int):
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
        



