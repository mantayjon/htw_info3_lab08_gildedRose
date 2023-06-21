import unittest
from tests.settings import *


class ConjuredTest(unittest.TestCase):

    @pytest.mark.xfail(xfail_new_features, reason="quality should be 9")
    def test_conjured_item_before_sell_date(self):
        item = Item("Conjured Item", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, 4)

    @pytest.mark.xfail(xfail_new_features, reason="quality should be 8")
    def test_conjured_item_on_sell_date(self):
        item = Item("Conjured Item", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, -1)

    @pytest.mark.xfail(xfail_new_features, reason="quality should be 8")
    def test_conjured_item_after_sell_date(self):
        item = Item("Conjured Item", -5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, -6)


if __name__ == '__main__':
    unittest.main()
