l=raw_input('Enter elements separated by space : ').split()
# Insertion Sort
for i in range(1,len(l)):
	# key will be inserted into the correct position
	key=l[i]				
	j=i-1
	# this loop is used to shift elements to make space for key
	while j>=0 and l[j]>key :
		# shifting elements 
		l[j+1]=l[j]	
		j=j-1
	# inserting key in the right position	
	l[j+1]=key
# printing the final sorted array
print l		
