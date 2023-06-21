# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self.update_item_quality(item)
            item.sell_in -= 1

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif item.name.startswith("Conjured"):
            self.update_conjured_item(item)
        else:
            self.update_normal_item(item)

    def update_normal_item(self, item):
        decrease_factor = 2 if item.sell_in <= 0 else 1
        item.quality = max(0, min(49, item.quality - decrease_factor))

    def update_aged_brie(self, item):
        increase_factor = 2 if item.sell_in <= 0 else 1
        item.quality = min(50, item.quality + increase_factor)

    def update_backstage_pass(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

        item.quality = min(50, item.quality)

    def update_conjured_item(self, item):
        decrease_factor = 4 if item.sell_in <= 0 else 2
        item.quality = max(0, item.quality - decrease_factor)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)