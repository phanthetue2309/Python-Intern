from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapify(data))                      # rearrange the list into heap order
print(heappush(data, -5))                 # add a new entry
x = [heappop(data) for i in range(3)]  # fetch the three smallest entries
print(x)
