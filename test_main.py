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
  Storage = json.load(f)
  assert Storage[shelf_num][compartment_num] == [1]

"""
Bin
"""
def test_can_create_bin():
  Bin_num1 = Bin(1)
  assert Bin_num1.bin_num == 1

def test_can_puton_bin():
  Toothbrash = Product(1)
  Bin_num1 = Bin(1)
  Bin_num1.add(1, Toothbrash)
  assert Bin_num1.bin_dict == {1: 1}

def test_can_takeoff_bin():
  Toothbrash = Product(1)
  Bin_num1 = Bin(1)
  Bin_num1.add(1, Toothbrash)
  Bin_num1.remove(Toothbrash)
  assert Bin_num1.bin_dict == {1: 1}