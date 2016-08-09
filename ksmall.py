import heapq
print 'Enter elements : '

heap=[int(i) for i in raw_input().split()]
#converting list int a min heap takes O(n) time
heapq.heapify(heap)

k=int(raw_input('Enter value of k: '))

ksm=0
for i in range(k):
	#popping elements from heap in non-decreasing order
	ksm=heapq.heappop(heap)
print 'Kth smallest element is : '+str(ksm)
