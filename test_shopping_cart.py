import unittest
from shopping_cart import calculate_total


class TestShoppingCart(unittest.TestCase):

    def test_calculate_total(self):
        cart_items = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        self.assertEqual(calculate_total(cart_items), 25.47)


if __name__ == "__main__":
    unittest.main()
