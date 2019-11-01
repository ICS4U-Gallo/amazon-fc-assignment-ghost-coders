from main import *
import unittest

"""
Product
"""


def test_can_create_product():
  Toothbrash = Product(1)
  assert Toothbrash.barcode == 1

  Fork = Product(2)
  assert Fork.barcode == 2

  Bag = Product(35)
  assert Bag.barcode == 35

"""
Trolly
"""


def test_can_puton_trolly():
  Toothbrash = Product(1)
  trolly = Trolly()
  trolly.add(Toothbrash)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == [1]

  Fork = Product(2)
  trolly = Trolly()
  trolly.add(Fork)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == [1, 2]

  Bag = Product(35)
  trolly = Trolly()
  trolly.add(Bag)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == [1, 2, 35]


def test_can_takeoff_trolly():
  Toothbrash = Product(1)
  trolly = Trolly()
  trolly.remove(Toothbrash)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == [2, 35]

  Fork = Product(2)
  trolly = Trolly()
  trolly.remove(Fork)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == [35]

  Bag = Product(35)
  trolly = Trolly()
  trolly.remove(Bag)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == []

"""
Shelf
"""


def test_can_puton_shelf():
  Toothbrash = Product(1)
  Shelf_A = Shelf()
  Shelf_A.add("A", "1", Toothbrash)
  with open("Compartment.json", 'r') as f:
    storage = json.load(f)
  assert storage["A"]["1"] == [1]

  Fork = Product(2)
  Shelf_B = Shelf()
  Shelf_B.add("B", "4", Fork)
  with open("Compartment.json", 'r') as f:
    storage = json.load(f)
  assert storage["B"]["4"] == [2]

  Bag = Product(35)
  Shelf_C = Shelf()
  Shelf_C.add("C", "6", Bag)
  with open("Compartment.json", 'r') as f:
    storage = json.load(f)
  assert storage["C"]["6"] == [35]


def test_can_takeoff_shelf():
  Toothbrash = Product(1)
  Shelf_A = Shelf()
  Shelf_A.remove(Toothbrash)
  with open("Compartment.json", "r") as f:
    storage = json.load(f)
  assert storage["A"]["1"] == []

  Fork = Product(2)
  Shelf_B = Shelf()
  Shelf_B.remove(Fork)
  with open("Compartment.json", "r") as f:
    storage = json.load(f)
  assert storage["B"]["4"] == []

  Bag = Product(35)
  Shelf_C = Shelf()
  Shelf_C.remove(Bag)
  with open("Compartment.json", "r") as f:
    storage = json.load(f)
  assert storage["C"]["6"] == []

"""
Bin
"""


def test_can_puton_bin():
  Toothbrash = Product(1)
  bin = Bin()
  bin.add(Toothbrash)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == [1]

  Fork = Product(2)
  bin = Bin()
  bin.add(Fork)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == [1, 2]

  Bag = Product(35)
  bin = Bin()
  bin.add(Bag)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == [1, 2, 35]


def test_can_takeoff_bin():
  Toothbrash = Product(1)
  bin = Bin()
  bin.remove(Toothbrash)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == []

  Fork = Product(2)
  bin = Bin()
  bin.remove(Fork)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == []

  Bag = Product(35)
  bin = Bin()
  bin.remove(Bag)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == []

  """
  Packaging
  """


def test_can_create_package():
  package_01 = Packaging("small", "123 Street", "Truck 01")
  assert package_01.box_type == "small"
  assert package_01.address == "123 Street"
  assert package_01.truck == "Truck 01"

  package_02 = Packaging("medium", "9090 Street", "Truck 02")
  assert package_02.box_type == "medium"
  assert package_02.address == "9090 Street"
  assert package_02.truck == "Truck 02"

  package_03 = Packaging("big", "487 Street", "Truck 03")
  assert package_03.box_type == "big"
  assert package_03.address == "487 Street"
  assert package_03.truck == "Truck 03"
