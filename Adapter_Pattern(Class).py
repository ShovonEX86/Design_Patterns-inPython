# -*- coding: utf-8 -*-
"""Singleton_Pattern.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QUUzAoRpHUE7fZL_B-oy-Naezz8Ngsao
"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def toppings(self):
        pass

    @abstractmethod
    def bun(self):
        pass

class DhakaStylePizza(Pizza):
    def toppings(self):
        print("Dhaka cheese and beef toppings")

    def bun(self):
        print("Dhaka bread bun")

class ChittagongPizza:
    def sausage(self):
        print("Ctg pizza sausage and chicken Toppings")

    def bread(self):
        print("Ctg bread")

class ChittagongClassAdapter(ChittagongPizza, Pizza):
    def toppings(self):
        self.sausage()

    def bun(self):
        self.bread()



#//Driver Code
pizza = ChittagongPizza()                                       #Outpus:
pizza.sausage()                                           #      |   Ctg pizza sausage and chicken Toppings
pizza.bread()                                             #      |   Ctg bread

adapted_pizza = ChittagongClassAdapter()
adapted_pizza.toppings()  # Calls sausage() internally           |   Ctg pizza sausage and chicken Toppings
adapted_pizza.bun()       # Calls bread() internally             |   Ctg bread