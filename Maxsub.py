# function to find max subarray crossing mid point
def crossmax(l,low,high,mid):
	leftsum=-1000000000
	rightsum=-1000000000	
	maxleft=mid
	maxright=mid

	sumtemp=0
	# calculating max leftwards
	for i in range(mid,low-1,-1):
			sumtemp=sumtemp+l[i]
			if sumtemp > leftsum:
				leftsum=sumtemp
				maxleft=i

	sumtemp=0
	# calculating max rightwards
	for i in range(mid+1,high+1):
		sumtemp=sumtemp+l[i]
		if sumtemp > rightsum:
			rightsum=sumtemp
			maxright=i
	# returning tuple		
	return (maxleft,maxright,leftsum+rightsum)

def maxsum(l,low,high):
	# base condition when length of list is 1
	if low==high:
			return (low,high,l[low])
	# calculating mid		
	mid=(low+high)/2
	# divide step
	# recursively solving left and right subarray
	leftlow,lefthigh,leftsum = maxsum(l,low,mid)
	rightlow,righthigh,rightsum = maxsum(l,mid+1,high)
	crosslow,crosshigh,crosssum = crossmax(l,low,high,mid)
	# return max of 3 sums
	if leftsum == max(leftsum,rightsum,crosssum) : 
		return (leftlow,lefthigh,leftsum)
	elif rightsum == max(leftsum,rightsum,crosssum) :
		return (rightlow,righthigh,rightsum)
	else:
		return (crosslow,crosshigh,crosssum)


print 'Enter elements : '
l=[int(i) for i in raw_input().split()]
low,high,tsum = maxsum(l,0,len(l)-1)
print low,high,tsum						
