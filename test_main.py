from main import *
import unittest

"""
Product
"""
def test_can_create_product():
  Toothbrash = Product(1)
  assert Toothbrash.barcode == 1

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

def test_can_takeoff_trolly():
  Toothbrash = Product(1)
  trolly = Trolly()
  trolly.remove(Toothbrash)
  with open("trolly.json", "r") as f:
    storage = json.load(f)
  assert storage == []

"""
Shelf
"""
def test_can_create_shelf():
  Shelf_A = Shelf("A", 1)
  assert Shelf_A.shelf_num == "A"
  assert Shelf_A.compartment_num == 1

def test_can_puton_shelf():
  Toothbrash = Product(1)
  Shelf_A = Shelf("A", 1)
  Shelf_A.add("A", 1, Toothbrash)
  with open("Compartment.json", 'r') as f:
    storage = json.load(f)
  assert storage[shelf_num][compartment_num] == [1]

def test_can_takeoff_shelf():
  Toothbrash = Product(1)
  Shelf_A = Shelf("A", 1)
  Shelf_A.remove(Toothbrash)
  with open("Compartment.json", "r") as f:
    storage = json.load(f)
  assert storage[shelf_num][compartment_num] == []

"""
Bin
"""
def test_can_puton_bin():
  Toothbrash = Product(1)
  bin = Bin()
  bin.add(Toothbrash)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert  storage == [1]

def test_can_takeoff_bin():
  Toothbrash = Product(1)
  bin = Bin()
  bin.remove(Toothbrash)
  with open("bin.json", "r") as f:
    storage = json.load(f)
  assert storage == []

  """
  Packaging
  """
  def test_can_create_package():
    package_01 = Packaging("Plastic", "123 Street", "Truck 01")
    assert package_01.box_type == "Plastic"
    assert package_01.address == "123 Street"
    assert package_01.truck == "Truck 01"