def is_prime_number(x):
  # 2부터 (x - 1)까지의 모든 수를 확인
  for i in range(2, x):
  	# x가 해당 수로 나누어떨어지면
    if x % i == 0:
    	return "NO"
  return "YES"
  
print(is_prime_number(4))