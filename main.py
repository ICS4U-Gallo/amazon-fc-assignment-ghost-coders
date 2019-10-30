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
        """
        self.barcode = barcode


    def on_trolly(self, trolly: Trolly):
        """Returns the trolly number
        Places the product on a trolly.
        """
        self.trolly = trolly

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
        self.shelf = shelf
        self.compartment = compartment
    
    def in_bin(self, bin_number: Bin, product: Product):
        """
        Places the products ordered onto the bin
        """
        self.bin_number = bin_number
        self.product = product


class Trolly:
    """Trolly Class
    Carries product from truck to shelf and compartment
    """
    
    def __init__(self):
        self.item = []

    def add(self,item):
        self.item.append(item)

    def remove(self, item):
        self.item.remove(item)

class Shelf:
    """Shelf Class
    Holds the product in a specific shelf and compartment location (number)
    """
    def __init__(self, shelf_num: str, compartment_num: int):
        self.shelf_num = shelf_num
        self.compartment_num = compartment_num


    def add(self, shelf_num, compartment_num, item: Product):
        


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
        self.number = number


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



def main():
    pass


if __name__ == "__main__":
    main()