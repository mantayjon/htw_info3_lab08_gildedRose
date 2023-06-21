import unittest
from tests.settings import *


class SulfurasTest(unittest.TestCase):
    def test_sulfuras_before_sell_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.sell_in, 5)

    def test_sulfuras_on_sell_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.sell_in, 0)

    def test_sulfuras_after_sell_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.sell_in, -5)


if __name__ == '__main__':
    unittest.main()
