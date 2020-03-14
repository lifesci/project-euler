import math

def is_prime(n):
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def largest_prime_factor(n):
  root = int(math.sqrt(n))
  for i in range(root, 1, -1):
    if is_prime(i) and n % i == 0:
      return i
  return None

def main():
  num_str = input('Enter a positive integer: ')
  try:
    num = int(num_str)
  except ValueError:
    print('You must enter a valid integer')
    return

  if num <= 0:
    print('You must enter a positive integer')
    return

  if num == 1:
    print('1 has no prime factors')
    return

  print(largest_prime_factor(num))

if __name__ == '__main__':
  main()
