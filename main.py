# Declare Variables
# -----------------

x = []
val = []

# Sieve of Eratosthenes till n-th prime number
# -------------------------------------------

def eratosthenes(n):
	
	global x
	global val

	x = [True]*n
	x[0] = False
	val = [0]*n
	
	for i in range(n):
		val[i]=i+1
	print(val)
	p = 2
	for i in range(p,n):
		for j in range(i,n):
			if val[j] % i ==0:
				x[j] = False;
	print(x)

# Sieve of Eratosthenes - find prime number
# -----------------------------------------------

def find_prime(p):

	global x
	global val
	total_prime=0
	found=False
	found_prime=0

	for i in range(len(val)):
		if x[i] is True:
			total_prime = total_prime+1
			if total_prime == p:
				found=True;
				found_prime=val[i]
	if found is True:
		print("Prime number #{} = {}".format(p,found_prime))
	else:
		print("The prime number you were looking for didn't exist, generate more prime numbers with the Eratosthenes function")

if __name__ == '__main__':
		
	# Generate the first 10 000 prime numbers
	# -----------------
	eratosthenes(10000)
	
	# What is the 327th prime number?
	# -----------------
	find_prime(327)
