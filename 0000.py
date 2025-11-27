# sum of odd squared numbers

def is_odd(x):
	return x % 2 != 0


def main():
	n = 465000
	answer = sum([x ** 2 for x in range(n + 1) if is_odd(x ** 2)])
	print(answer)


if __name__ == '__main__':
	main()

