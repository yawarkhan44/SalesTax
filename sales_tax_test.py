import unittest
import sales_tax

class TestMiscellaneous(unittest.TestCase):
    
    def test_calculate_rounded_tax(self):
        """Checks the rounding up of taxes i.e.  for a tax rate of n%, a shelf price of p 
        contains (np/100 rounded up to the nearest 0.05) amount of sales tax"""
        taxes = [1.49, 4.75, 2.375, 2.799, 1.3995, 1.899, 0.5625, 2.375] #dummy values to check
        roundedTaxes = [1.5, 4.75, 2.4, 2.8, 1.4, 1.9, 0.6, 2.4] #answers to the values above

        for i in range(0, len(taxes)):
            self.assertEqual(sales_tax.calculate_rounded_tax(taxes[i]), roundedTaxes[i])

    def test_make_order(self):
        """Checks if the properties from the file are extracted correctly"""
        order = sales_tax.make_order("order3.txt") #Input file
        items = [{'Name': 'imported bottle of perfume ', 'Price': 27.99, 'Quantity': 1, 'Imported': True}, 
            {'Name': 'bottle of perfume ', 'Price': 18.99, 'Quantity': 1, 'Imported': False}, 
            {'Name': 'packet of headache pills ', 'Price': 9.75, 'Quantity': 1, 'Imported': False}, 
            {'Name': 'imported box of chocolates ', 'Price': 11.25, 'Quantity': 1, 'Imported': True}] #This should be returned
        self.assertEqual(order, items)


class TestProduct(unittest.TestCase):
    """Checks the product to see if basic and import taxes are calculated correctly."""
    def test_no_tax(self): #For items that are exempt and are not imported, no taxes apply
        item = sales_tax.Product({"Name": "book", "Price": 12.49, "Quantity": 1, "Imported": False})
        self.assertEqual(item.tax, 0)
    def test_basic_tax(self):#For items that are not exempt and are not imported, only basic tax apply
        item = sales_tax.Product({"Name": "music CD", "Price": 14.99, "Quantity": 1, "Imported": False})
        self.assertEqual(item.tax, 1.5)
    def test_basic_and_import_tax(self):#For items that are not exempt and are imported, both taxes apply
        item = sales_tax.Product({"Name": "imported bottle of perfume", "Price": 47.50, "Quantity": 1, "Imported": True})
        self.assertEqual(item.tax, 7.15)

class TestBasket(unittest.TestCase):
    """Checks the basket to see if the total tax, subtotal, and grand total are calculated correctly"""
    def setUp(self):
        #A list of items to be added to basket
        self.basket = sales_tax.Basket()
        items = [{"Name": "imported bottle of perfume", "Price": 27.99, "Quantity": 1, "Imported": True},
                {"Name": "bottle of perfume", "Price": 18.99, "Quantity": 1, "Imported": False},
                {"Name": "packet of headache pills", "Price": 9.75, "Quantity": 1, "Imported": False},
                {"Name": "imported box of chocolates", "Price": 11.25, "Quantity": 1, "Imported": True}]
        for item in items:
            self.basket.add(item)
    def test_tax(self): #To check total tax of basket
        self.assertEqual(float("{0:.2f}".format(self.basket.total_tax())), 6.70)
    def test_subtotal(self):#To check subtotal tax of basket
        self.assertEqual(float("{0:.2f}".format(self.basket.subtotal())), 67.98)
    def test_total(self):#To check grand total of basket
        basketTax, basketTotal = self.basket.total()

        self.assertEqual(float("{0:.2f}".format(basketTax)), 6.70)
        self.assertEqual(float("{0:.2f}".format(basketTotal)), 74.68)
if __name__ == '__main__':
    unittest.main()
