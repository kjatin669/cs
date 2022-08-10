class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value= value

class Map:
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None
    
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True
    
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "invalid map key"
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid Map Key"

    def __iter__(self):
        return iter(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    
myMap = Map()
myMap.add(12, 24)
myMap.add(13, 26)
myMap.add(14, 28)
print(myMap.valueOf(13))
myMap.remove(13)
value = myMap.__iter__()
print(next(value))
print(next(value))
print(next(value))
