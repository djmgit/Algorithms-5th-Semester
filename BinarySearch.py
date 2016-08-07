# function to binary search
def binarySearch(l, n):
	lower,upper=0,len(l)-1
	while lower<=upper:
		# calcuating mid
		mid=(lower+upper)/2
		# element is found
		if n==l[mid]:
			return True
		# element is not found so adjust lower and
		# upper bound	
		if n>l[mid]:
			lower=mid+1
		if n<l[mid]:
			upper=mid-1
	# element is not found		
	return False
	
print 'Enter List elements : '
l=[int(i) for i in raw_input().split()]
# sort list
l.sort()
ser=int(raw_input("Enter element to search for : "))
isPresent=binarySearch(l, ser)
if isPresent==False:
	print str(ser)+' is not present in list'
else:
	print str(ser)+' is present in the list'					
