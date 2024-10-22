def num_divisors(x):
	i = 0
	n = 0
	while i < x:
		i = i + 1
		if x % i == 0:
			n = n + 1
	return(n)

## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x):
	## YOU CODE SHOULD START HERE AT THE SAME
	## IDENTATION AS THIS COMMENT

	# 1. Find the divisors of x and count them
	divisors_x = num_divisors(x)

	# 2. Find the divisors of all the smaller positive integrers of x and count them
	i = 0
	n = 0
	
	while i < x-1:
		i = i + 1
		divisors_i = num_divisors(i)
		if divisors_i >= divisors_x:
			n = n + 1

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

	if n == 0:
		return("anti-prime")
	else:
		return("not anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT

	import sys
	x = int(sys.argv[1])
	print(main(x))
