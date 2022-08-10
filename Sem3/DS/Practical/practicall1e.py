class Set :    
    # Creates an empty set instance.
    def __init__( self, *initElements ):
        self._theElements = list()
        for i in range(len(initElements)) :
            self._theElements.add( initElements )

   # Returns the number of items in the set.
    def __len__( self ):
        return len( self._theElements )

   # Determines if an element is in the set.
    def __contains__( self, element ):
        return element in self._theElements   

   # Determines if the set is empty.
    def isEmpty( self ):
        return len(self._theElements) == 0

   # Adds a new unique element to the set. 
    def add( self, element ):                  
        if element not in self :
            self._theElements.append( element )   

   # Removes an element from the set.
    def remove( self, element ):
        assert element in self, "The element must be in the set."
        self._theElements.remove( element )

   # Determines if this set is equal to setB.
    def __eq__( self, setB ):                 
        if len( self ) != len( setB ) :
            return False
        else :
            return self.isSubsetOf( setB )                  

   # Determines if this set is a subset of setB.
    def isSubsetOf( self, setB ):           
        for element in self :
            if element not in setB :
                return False
        return True 

  # Determines if this set is a proper subset of setB.
    def isProperSubset( self, setB ):
        for element in self :
            if self != setB :
                return True
        return False

   # Creates a new set from the union of this set and setB.
    def union( self, setB ):                 
        newSet = Set()  
        newSet._theElements.extend( self._theElements )
        for element in setB :
            if element not in self :
                newSet._theElements.append( element )
        return newSet                           

   # Creates a new set from the intersection: self set and setB.
    def intersect( self, setB ):
        newSet = Set()
        for element in setB :
            if element in self :
                newSet._theElements.append( element )
        return newSet 

# Creates a new set from the difference: self set and setB.
    def difference( self, setB ):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in setB :
            if element in self :
                newSet._theElements.remove( element )
        return newSet

 # Creates the iterator for the self
    def __iter__( self ):
        return iter(self._theElements)


    def display(self):
        return self._theElements



setA = Set()

setA.add(34)
setA.add(84)
setA.add(20)

setB = Set()

setB.add(28)
setB.add(20)
setB.add(13)

print(setA.display())
print(setB.display())

setC = setA.union(setB)
print(setC.display())

setD = setA.intersect(setB)
print(setD.display())

newSetA = setA
newSetA.remove(84)
print(newSetA.display())
