n=2
m=10
def check_prime(k):
	for i in range(2,k-1//2):
		if k%i==0:
			return False
	return True

def prime_number(n,m):
	non_prime_list=[]
	prime_list=[]
	for num in range(n,m+1):
		if check_prime(num):
			prime_list.append(num)
		else:
			non_prime_list.append(num)
	print("Prime numbers are",prime_list)
	print("Non prime number list are",non_prime_list)
	return prime_list,non_prime_list

print(prime_number(n,m))
