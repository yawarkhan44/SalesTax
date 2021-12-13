import unittest
import sales_tax

class TestMiscellaneous(unittest.TestCase):
    """Checks the rounding up of taxes i.e.  for a tax rate of n%, a shelf price of p 
    contains (np/100 rounded up to the nearest 0.05) amount of sales tax"""
    def test_calculate_rounded_tax(self):

        taxes = [1.49, 4.75, 2.375, 2.799, 1.3995, 1.899, 0.5625, 2.375] #dummy values to check
        roundedTaxes = [1.5, 4.75, 2.4, 2.8, 1.4, 1.9, 0.6, 2.4] #answers to the values above to ensure correct functionality

        for i in range(0, len(taxes)):
            self.assertEqual(sales_tax.calculate_rounded_tax(taxes[i]), roundedTaxes[i])

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

if __name__ == '__main__':
    unittest.main()
