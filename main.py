"""
Product
====
Barcode -> object
Trolly number 
Bin number
Shelf number
Compartment number
"""

class Product():
    """
    This the class for the products coming in 
    """

    def __init__(self, barcode: int):
        """
        This is the inti function for all the main parts of the code
        """
        self.barcode = barcode
        pass
