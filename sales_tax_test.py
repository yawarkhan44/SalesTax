import unittest
import sales_tax

class TestMiscellaneous(unittest.TestCase):
    def test_calculate_rounded_tax(self):

        taxes = [1.49, 4.75, 2.375, 2.799, 1.3995, 1.899, 0.5625, 2.375]
        roundedTaxes = [1.5, 4.75, 2.4, 2.8, 1.4, 1.9, 0.6, 2.4]

        for i in range(0, len(taxes)):
            self.assertEqual(sales_tax.calculate_rounded_tax(taxes[i]), roundedTaxes[i])
            
class TestProduct(unittest.TestCase):
    def test_no_tax(self):
        item = sales_tax.Product({"Name": "book", "Price": 12.49, "Quantity": 1, "Imported": False})
        self.assertEqual(item.tax, 0)
    def test_basic_tax(self):
        item = sales_tax.Product({"Name": "music CD", "Price": 14.99, "Quantity": 1, "Imported": False})
        self.assertEqual(item.tax, 1.5)
    def test_basic_and_import_tax(self):
        item = sales_tax.Product({"Name": "imported bottle of perfume", "Price": 47.50, "Quantity": 1, "Imported": True})
        self.assertEqual(item.tax, 7.15)

if __name__ == '__main__':
    unittest.main()
