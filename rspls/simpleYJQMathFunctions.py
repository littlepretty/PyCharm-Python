
def gatherDivisors(num):
	"""gather num's all divisors."""
	divisors=[]
	for i in xrange(1,num/2+1):
		if num%i==0:
			divisors.append(i)
	return divisors

def quickSort(seq):
	"""classic implementation of quick sort"""
	if (len(seq)==0):
		return seq
	front=quickSort([le for le in seq[1:] if le<=seq[0]])
	back=quickSort([gt for gt in seq[1:] if gt>=seq[0]])
	return front+[seq[0]]+back

seq=[8,1,4,7,5,3,6,14,9]
print quickSort(seq)



