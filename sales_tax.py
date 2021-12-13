
from math import ceil

#List of items that are exempt from basic tax
TAX_EXEMPTED_ITEMS = ["chocolate", "book", "pill", "chocolates", "books", "pills"] 

def calculate_rounded_tax(amount):
    """Function for rounding up tax"""
    #multiply and divide by 20 because 1/0.05 = 20 as the values are rounded up to the nearest 0.05
    return ceil(round(amount , 2) * 20) / 20 

class Product():
    """Class for item"""
    def __init__(self, item):
        self.name = item["Name"]
        self.price = item["Price"]
        self.quantity = item["Quantity"]
        self.imported = item["Imported"]
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        """To calculate tax"""
        exempted = False
        salesTax = 0
        importTax = 0

        name = self.name.split()

        for category in TAX_EXEMPTED_ITEMS:
            if category in [x.lower() for x in name]:
                exempted = True
                break
        if self.imported: #Check if item is exempt
            salesTax = calculate_rounded_tax(float(self.price) * 0.05)
        if not exempted: #Check if item is imported
            importTax = calculate_rounded_tax(float(self.price) * 0.1)
        totalTax = salesTax + importTax #Add both taxes to totalTax 
        return totalTax

class Basket():
    """Class to add the products"""
    def __init__(self):
        self.basket = [] #Empty basket initially
    def add(self, item):
        self.basket.append(item)

    def total_tax(self): #For calculating total tax of basket
        basketTax = 0
        for item in self.basket:
            currentItem = Product(item)
            basketTax = basketTax + calculate_rounded_tax(currentItem.tax * currentItem.quantity)
        return basketTax

    def subtotal(self): #For calculating subtotal of basket
        basketSubtotal = 0
        for item in self.basket:
            currentItem = Product(item)
            basketSubtotal = basketSubtotal + currentItem.price * currentItem.quantity
        return basketSubtotal

    def total(self): #For calculating grand total of basket
        basketTax = self.total_tax()
        basketSubtotal = self.subtotal()
        basketTotal = basketTax + basketSubtotal
        return basketTax, basketTotal

    def print_receipt(self):#Printing the receipt
        for item in self.basket:
            currentItem = Product(item)
            total = round(float(currentItem.price) + currentItem.tax, 2)
            print(currentItem.quantity, currentItem.name, "\b\b: {:.2f}".format(total))
            basketTax, basketTotal = self.total()
        print("Sales Taxes: {0:.2f}".format( basketTax))
        print("Total:  {0:.2f}".format(basketTotal))
