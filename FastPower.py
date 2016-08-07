# function for fast power calculation
def fastPower(base, power):
	# base case
	if power==0:
		return 1
	# checking if power is even	
	if power&1==0:
		return fastPower(base*base,power/2)
	# if power is odd	
	else:
		return base*fastPower(base*base,(power-1)/2)		 



base=int(raw_input("Enter base : "))
power=int(raw_input("Enter power : "))

result=fastPower(base,power)

print result

