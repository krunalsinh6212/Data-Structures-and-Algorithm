class MinHeap:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.array = [0] * capacity

  def swap(self, a, b):
    self.array[a], self.array[b] = self.array[b], self.array[a]

  def minHeapify(self, idx):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < self.size and self.array[left] < self.array[smallest]:
      smallest = left

    if right < self.size and self.array[right] < self.array[smallest]:
      smallest = right

    if smallest != idx:
      self.swap(idx, smallest)
      self.minHeapify(smallest)

  def insert(self, value):
    if self.size == self.capacity:
      print("OVERFLOW: Could not insert key.")
      return
    
    self.size += 1
    i = self.size - 1
    self.array[i] = value

    while i != 0 and self.array[(i - 1) // 2] > self.array[i]:
      self.swap(i, (i - 1) // 2)
      i = (i - 1) // 2

  def extractMin(self):
    if self.size <= 0:
      return float("inf")
    if self.size == 1:
      self.size -= 1
      return self.array[0]
    
    root = self.array[0]
    self.array[0] = self.array[self.size - 1]
    self.size -= 1
    self.minHeapify(0)
    return root
  
  def printHeap(self):
    for i in range(self.size):
      print(self.array[i], end = " ")
    print()

minHeap = MinHeap(10)
minHeap.insert(3)
minHeap.insert(2)
minHeap.insert(1)
minHeap.insert(15)
minHeap.insert(5)
minHeap.insert(4)
minHeap.insert(45)
minHeap.insert(12)
minHeap.insert(7)
minHeap.insert(9)

print("Min Heap :", end = " ")
minHeap.printHeap()

print("Extract Min :", minHeap.extractMin())

print("Min Heap after Extraction : ", end = " ")
minHeap.printHeap()