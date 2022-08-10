class Bag:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)
    
    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)
        return "The item " + str(item) + " added Successfully"

    def remove(self, item):
        assert item in self._theItems, "The Item must be in Bag"
        ndx = self._theItems.index(item)
        return "The item " + str(self._theItems.pop(ndx)) + " removed Successfully"


myBag = Bag()
print(myBag.add(23))
print(myBag.add(33))
print(myBag.add(28))
print(myBag.add(25))
print(myBag.add(83))
print(myBag.__len__())
print(myBag.__contains__(28))
print(myBag.__contains__(29))
print(myBag.remove(83))
print(myBag.__len__())
