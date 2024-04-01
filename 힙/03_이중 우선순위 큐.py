import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for o in operations:
        cmd, value = o.split(" ")

        if (cmd == "I"):
            heapq.heappush(min_heap, int(value))
            heapq.heappush(max_heap, -int(value))
        else:
            if (value == "-1" and len(min_heap) != 0):
                val = heapq.heappop(min_heap)
                max_heap.remove(-val)
            elif (value == "1" and len(max_heap) != 0):
                val = heapq.heappop(max_heap)
                min_heap.remove(-val)

    if (len(min_heap) >= 2):
        answer = [int(-heapq.heappop(max_heap)), int(heapq.heappop(min_heap))]
    else:
        answer = [0, 0]

    return answer
