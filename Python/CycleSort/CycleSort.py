import unittest

# source: https://sr.wikipedia.org/wiki/Cikli%C4%8Dno_sortiranje#Algoritam
# Sort an array in place and return the sorted array
def cycleSort(array):
  writes = 0
  
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
    
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
    
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
    
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
    
    # Rotate the rest of the cycle.
    while pos != cycleStart:
      
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
      
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
  
  return array



# Test For the CycleSort
class TestSuite(unittest.TestCase):
  def test_cycleSort(self):
    arr = [2, 5, 8, 6, 35, 1, 2, 545, 6, 2, 3, 12, 4]
    self.assertEqual([1, 2, 2, 2, 3, 4, 5, 6, 6, 8, 12, 35, 545], cycleSort(arr))

if __name__ == "__main__":
  unittest.main()