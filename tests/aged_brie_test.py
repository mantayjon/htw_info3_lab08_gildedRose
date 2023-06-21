import unittest

from tests.settings import *


class AgedBrie(unittest.TestCase):
    def test_aged_brie_before_sell_date(self):
        item = Item("Aged Brie", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 11)
        self.assertEqual(item.sell_in, 4)

    def test_aged_brie_before_sell_date_max_quality(self):
        item = Item("Aged Brie", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 4)

    def test_aged_brie_on_sell_date(self):
        item = Item("Aged Brie", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 12)
        self.assertEqual(item.sell_in, -1)

    def test_aged_brie_on_sell_date_max_quality(self):
        item = Item("Aged Brie", 0, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, -1)

    def test_aged_brie_after_sell_date(self):
        item = Item("Aged Brie", -5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 12)
        self.assertEqual(item.sell_in, -6)

    def test_aged_brie_after_sell_date_max_quality(self):
        item = Item("Aged Brie", -5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, -6)



if __name__ == '__main__':
    unittest.main()
