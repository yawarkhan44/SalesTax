
from math import ceil

TAX_EXEMPTED_ITEMS = ["chocolate", "book", "pill", "chocolates", "books", "pills"]

def calculate_rounded_tax(amount):
    return ceil(round(amount , 2) * 20) / 20
class Product():
    def __init__(self, item):
        self.name = item["Name"]
        self.price = item["Price"]
        self.quantity = item["Quantity"]
        self.imported = item["Imported"]
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        
        exempted = False
        salesTax = 0
        importTax = 0

        name = self.name.split()

        for category in TAX_EXEMPTED_ITEMS:
            if category in [x.lower() for x in name]:
                exempted = True
                break
        if self.imported:
            salesTax = calculate_rounded_tax(float(self.price) * 0.05)
        if not exempted:
            importTax = calculate_rounded_tax(float(self.price) * 0.1)
        totalTax = salesTax + importTax
        return totalTax
