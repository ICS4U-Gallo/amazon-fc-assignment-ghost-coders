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
        pass


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
    
#     def get_shelf_number(self):
#         return self.shelf_number
    
#     def get_shelf_compartment_num(self):
#         return self.shelf.compartment_num

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
        
    
#     def get_bin_number(self):
#         return self.bin_number
    
# class Trolly:
#     """
#     Placed product into a trolly with a trolly number. 
#     """
#     def __init__(self, trolly_num: int):
#         self.trolly_num = trolly_num
#         self.trolly_list = []

    
#     def add_product(self, product: Product):
#         self.trolly_list.append(product)
    
    
#     def delate_product(self, barcod: int):
#         for item.barcode in self.trolly_list:
#             if item.barcode == barcode:
#                 self.trolly_list.remove(item)
    
    
#     def get_trolly(self):
#         return self.trolly_list

# class Shelf:
#     '''
#     Remove product in trolly and placed in a shelf with its own trolly number and compartment number
    
#     '''
    
# class Bin:
#     '''
#     Remove product in shelf and placed in a bin with bin number
#     '''
    
# class Control:
#     '''
#     control the add and remove function
#     '''