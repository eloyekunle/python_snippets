num = input("Enter a number\n=>")
def productOfFactors(n):
	i = 1
	factors = set([])
	factorProd = 1
	while (i < n):
		if(n%i == 0):
			factors.add(i)
		i += 1
	
	for eachFactor in factors:
		factorProd *= eachFactor

	return factorProd

facProd = productOfFactors(num)
print facProd
