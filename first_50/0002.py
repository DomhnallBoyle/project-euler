# even fibonacci numbers

def is_even(x):
	return x % 2 == 0


def main():
	n = 4_000_000
	answer = 0
	prev_prev, prev, next = 0, 1, 0
	
	while next <= n:
		next = prev_prev + prev
		if is_even(next):
			answer += next
		prev_prev = prev
		prev = next

	print(answer)


if __name__ == '__main__':
	main()

