def main():
	sumOfEven = 0

	f1 = 0
	f2 = 1
	nthTerm = 0
	max = 4000000
	while(nthTerm < max):
		nthTerm = f1 + f2
		if(nthTerm % 2 == 0):
			sumOfEven = sumOfEven + nthTerm
		f1 = f2
		f2 = nthTerm

	print(sumOfEven)

if __name__ == "__main__":
	main()

