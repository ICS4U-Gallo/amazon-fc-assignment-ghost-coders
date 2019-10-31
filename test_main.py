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
def test_can_create_trolly():
  Trolly_num1 = Trolly(1)
  assert Trolly_num1.trolly_num == 1

def test_can_puton_trolly():
  Toothbrash = Product(1)
  Trolly_num1 = Trolly(1)
  Trolly_num1.add_product(Toothbrash)
  assert Trolly.trolly_list == [1]

def test_can_takeoff_trolly():
  Toothbrash = Product(1)
  Trolly_num1 = Trolly(1)
  Trolly_num1.add_product(Toothbrash)
  Trolly_num1.delate_product(1, Toothbrash)
  assert Trolly.trolly_list == []

"""
Shelf
"""
def test_can_create_shelf():
  Shelf_num1 = Shelf(1, "A1")
  assert Shelf_num1.shelf_num == 1
  assert Shelf_num1.compartment_num == "A1"

def test_can_puton_shelf():
  Toothbrash = Product(1)
  Shelf_num1 = Shelf(1, "A1")
  Shelf_num1.add(1, "A1", Toothbrash)


"""
Bin
"""
def test_can_create_bin():
  Bin_num1 = Bin(1)
  assert Bin_num1.bin_num == 1

def test_can_puton_bin():
  Toothbrash = Product(1)
  Bin_num1 = Bin(1)

