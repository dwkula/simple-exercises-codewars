import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = {}

        index = 0
        for i in range(0, len(self.collection), self.items_per_page):
            self.pages[index] = self.collection[i: i + self.items_per_page]
            index += 1

    # returns the number of items within the entire collection

    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection)/self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= len(self.pages):
            return -1

        return len(self.pages[page_index])

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if self.collection:
            if item_index < 0 or item_index >= len(self.collection):
                return -1
            for index, page in self.pages.items():
                if self.collection[item_index] in page:
                    return index

        else:
            return -1


collect = ['a', 'b', 'c', 'd']

helper = PaginationHelper(collect, 2)

print(helper.page_index(2))

print('b' in collect)
