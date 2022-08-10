class Set:
    def __init__(self):
        self._theElements = list()
    
    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, elememt):
        if elememt not in self:
            self._theElements.append(elememt)

    def remove(self, element):
        assert element in self, "The element must be in the set"
        self._theElements.remove(item)

    def union (self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def intersect(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElement)

setA = Set()
setA.add(23)
setA.add(64)
setA.add(19)

setB = Set()
setB.add(27)
setB.add(19)
setB.add(25)
