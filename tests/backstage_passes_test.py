import unittest
from tests.settings import *


class BackstagePassTest(unittest.TestCase):
    def test_backstage_passes_long_before_sell_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 11)
        self.assertEqual(item.sell_in, 10)

    def test_backstage_passes_long_before_sell_date_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 10)

    def test_backstage_passes_medium_close_to_sell_date_upper_bound(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 12)
        self.assertEqual(item.sell_in, 9)

    def test_backstage_passes_medium_close_to_sell_date_upper_bound_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 9)

    def test_backstage_passes_medium_close_to_sell_date_lower_bound(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 12)
        self.assertEqual(item.sell_in, 5)

    def test_backstage_passes_medium_close_to_sell_date_lower_bound_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 5)

    def test_backstage_passes_very_close_to_sell_date_upper_bound(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 13)
        self.assertEqual(item.sell_in, 4)

    def test_backstage_passes_very_close_to_sell_date_upper_bound_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 4)

    def test_backstage_passes_very_close_to_sell_date_lower_bound(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 13)
        self.assertEqual(item.sell_in, 0)

    def test_backstage_passes_very_close_to_sell_date_lower_bound_max_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 0)

    def test_backstage_passes_on_sell_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)
        self.assertEqual(item.sell_in, -1)

    def test_backstage_passes_after_sell_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)
        self.assertEqual(item.sell_in, -6)


if __name__ == '__main__':
    unittest.main()
