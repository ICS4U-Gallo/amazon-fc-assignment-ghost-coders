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
    
    def __str__(self):
        return f"{self.barcode}"


class Trolly:
    """
    Placed product onto trolly to be moved onto shelf
    """
    trolly_list = []

    def add(self, product: Product):
        trolly_list.append(Product)
     
    def delate_product(self, items: Product):
        for code in Trolly.trolly_list:
            if code == items.barcode:
                Trolly.trolly_list.remove(code)
    

<<<<<<< HEAD

# class Shelf:
#     """Shelf Class
#     Holds the product in a specific shelf and compartment location (number)
#     """
#     def __init__(self, shelf_num: str, compartment_num: int):
#         self.shelf_num = shelf_num
#         self.compartment_num = compartment_num

=======
        storage.append(product.barcode)

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
    def __init__(self):#, shelf_num: str, compartment_num: int):
        # self.shelf_num = shelf_num
        # self.compartment_num = compartment_num
        pass
>>>>>>> 08148575024c1d804af10506507dbf9dc03cdaea

#     def add(self, shelf_num: str, compartment_num: int, item: Product):
#         with open("Compartment.json", 'r') as f:
#             storage = json.load(f)
        
#         storage[shelf_num][compartment_num].append(item.barcode)

#         with open("Compartment.json", "w")  f:
#             json.dump(storage, f)as

#     def remove(self, item: Product):
#         with open("Compartment.json", "w") as f:
#             storage = json.load(f)
        
        for key, value in storage.items():
            for key, value in value.items():
                for barcode in value:
                    if item.barcode in value:
                        value.remove(item.barcode)



class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self):
        pass

<<<<<<< HEAD
    def add(self, bin_num: int, item: Product):
        if bin_num not in Bin.bin_dict.keys():
            Bin.bin_dict[bin_num] = item
        else:
            Bin.bin_dict[bin_num] = item

    def remove(self, item: Product):
        for value in Bin.bin_dict.values():
            if value == item:
                value = ""


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
    package_1 = Product("AMZ001")
    package_2 = Product("AMZ002")
    
    trolly.add_product(package_1)
    trolly.add_product(package_2)
    print(Trolly.trolly_list)
    trolly.delate_product(package_1)
    print(Trolly.trolly_list)
    
        for key, value in storage.items():
            for key, value in value.items():
                for barcode in value:
                    if item.barcode in value:
                        value.remove(item.barcode)


class Bin:
    """Bin Class
    Collects the products ordered and carries it to the packaging station
    """
    def __init__(self, bin_num: int):
        self.bin_num = bin_num

    def add(self, bin_num: int, item: Product):
        if bin_num not in Bin.bin_dict.keys():
            Bin.bin_dict[bin_num] = item
        else:
            Bin.bin_dict[bin_num] = item

    def remove(self, item: Product):
        for value in Bin.bin_dict.values():
            if value == item:
                value = ""
=======
    def add(self, product: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)
        
        storage.append(product.barcode)

        with open("bin.json", "w") as f:
            json.dump(storage, f)

    def remove(self, product: Product):
        with open("bin.json", "r") as f:
            storage = json.load(f)
        
        storage.clear()

        with open("bin.json", "w") as f:
            json.dump(storage, f)
>>>>>>> 08148575024c1d804af10506507dbf9dc03cdaea


class Packaging:
    """Packaging Class
    Prepares the products (the order) for shipment to customer
    Attributes:
        box_type = small, medium, large, fragile
        address = where product is sent to
        truck = transportation, license plate
    """

    order = Bin

    def __init__(self, box_type: str, address: str, truck: str):
        self.box_type = box_type
        self.address = address
        self.truck = truck
    
    def __str__(self):
        return f"""The product(s) has been shipped.
        {order}"""

    
def main():
    shirt = Product(12345)
    pants = Product(98765)

    trolly = Trolly()
    shelf = Shelf()
    bin = Bin()
    # packaging = Packaging()

    trolly.add(shirt)
    shelf.add("A", 1, shirt)

    print(shirt)
    print(pants)
    print(trolly)

>>>>>>> Stashed changes

    
if __name__ == "__main__":
    main()
