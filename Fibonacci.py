# function to multiplty to matrices
def multi(m1,m2):
	r=[
		[m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0], m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]],
	  	[m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0], m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]]
	  ]
	return r
# function to perform fast power calculation	 
def fastPower(base,power) :
	# base case
	if power==0:
		return [[1,0],[0,1]]
	if power&1==0:
		return fastPower(multi(base,base),power/2)
	else:
		return multi(base,fastPower(multi(base,base),(power-1)/2))

n=int(raw_input("Enter n : "))
# base matrix for nth fibonaccin calulation
base=[[1,1],[1,0]]
result=fastPower(base,n)
fn=result[0][1]
print 'nth fibonacci term is '+str(fn)
