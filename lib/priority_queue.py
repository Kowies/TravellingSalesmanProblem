# import heapq


# class PQueue(object):
#     def __init__(self, key, data=()):
#         self.key = key
#         self.heap = [(self.key(d), d) for d in data]
#         heapq.heapify(self.heap)

#     def push(self, item):
#         decorated = self.key(item), item
#         heapq.heappush(self.heap, decorated)

#     def extend(self, iterable):
#         for item in iterable:
#             self.push(item)

#     def pop(self):
#         decorated = heapq.heappop(self.heap)
#         return decorated[1]

#     def is_empty(self):
#         return len(self.heap) == 0
