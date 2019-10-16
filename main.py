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

    def on_trolly(self):
        """Returns the trolly number
        """

    def off_trolly(self, trolly: int):
        """Deletes the trolly attribute
        Args:
            trolly: the trolly number
        Return:
            deletes the trolly number and returns a bin number
        """

    def in_bin(self, shelf: int, compartment: int):
        """Adds the bin into a shelf and compartment
        Args:
            shelf: where the shelf is
            compartment: where the compartment is 
        Return:
            the attribute of the new object
        """