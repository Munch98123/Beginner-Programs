def main():
	sum = 0
	for x in range(1, 1000):
		if(x % 3 == 0):
			sum = sum + x
		if(x % 5 == 0):
			sum = sum + x
		if(x % 5 == 0 and x % 3 == 0):
			sum = sum - x

	print(sum)

if __name__ == "__main__":
	main()

