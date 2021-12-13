
from math import ceil
from os import close
import sys

#List of items that are exempt from basic tax
TAX_EXEMPTED_ITEMS = ["chocolate", "book", "pill", "chocolates", "books", "pills"] 

#How to run
"""Modify the input variable in main() function to point to the input file and run the sales_tax.py"""

def main():
    """To run the main program"""
    input = "order1.txt" #The name of input file for which the receipt is generated
    itemsOrdered = make_order(input) #A function to extract name, price, quantity and the imported property
    basket = Basket() #Make a basket to put items in

    for item in itemsOrdered: #Add items in basket
        basket.add(item)

    basket.print_receipt() #Print receipt



def make_order(input):
    """This function extracts name, price, quantity and the imported property 
    from the input file, and stores it into a 2D list and returns it"""
    order = []

    try:
        f = open(input, "r") #Reads the input file
    except:
        print("Error: Filename specified not found. Please enter correctly and run the program again.")
        sys.exit(1)
    lines = f.readlines() #Save the text into a list whose every element is a line extracted from input file
    if(len(lines) == 0):
        print("Error: The file cannot be empty! Please run the program again!")
        sys.exit(1)
    for line in lines: #Analyze each line and extract properties
            try:
                words = line.split() #Split line by white space
                quantity = int(words[0]) #First element represents quantity
                imported = "imported" in [x.lower() for x in words] #Check if the word 'imported' appears in line
                price = float(words[words.index("at")+1]) #Price comes after the word 'at'
                name = ""
            except:
                print("Error: Bad formatting! Please ensure the format: [Quantity] [Name] ['at'] [Price], write every item on different line, and run the program again.")
                sys.exit(1)

            #Combine the full name into variable 'name' even if the name contains white spaces
            for i in range(1, words.index("at")):
                if i < words.index("at"):
                    name = name + words[i] + " "
                else:
                    name = name + words[i]
            if name == "":
                print("Error: Bad formatting! Please ensure the format: [Quantity] [Name] ['at'] [Price], write every item on different line, and run the program again.")
                sys.exit(1)
            if quantity < 1:
                print("Error: Please ensure quantity is not less than 1 and run the program again.")
                sys.exit(1)
            if price <= 0:
                print("Error: Please ensure price is greater than 0 and run the program again.")
                sys.exit(1)
            #Add the properties to the list of dictionaries
            order.append({"Name" : name, "Price" : price, "Quantity" : quantity, "Imported" : imported})
    f.close()
    return order

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

main() #Run the main program
