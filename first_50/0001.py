# multiples of 3 or 5

def is_multiple_of(x, m):
	a = x / m

	return a == int(a)


def main():
	n = 1000
	answer = sum([x for x in range(n) if is_multiple_of(x, 3) or is_multiple_of(x, 5)])
	print(answer)


if __name__ == '__main__':
	main()

