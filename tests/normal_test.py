from tests.settings import *

# create tests for normal items here...

def test_something():
    item = Item("name item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

import unittest

class NormalTest(unittest.TestCase):

    def test_normal_item_before_sell_date(self):
        item = Item("Normal Item", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 4)

    def test_normal_item_on_sell_date(self):
        item = Item("Normal Item", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -1)

    def test_normal_item_after_sell_date(self):
        item = Item("Normal Item", -5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -6)

    def test_normal_item_quality_zero(self):
        item = Item("Normal Item", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)
        self.assertEqual(item.sell_in, 4)

if __name__ == '__main__':
    unittest.main()

