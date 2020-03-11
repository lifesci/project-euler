def is_palindrome(n):
  if n < 0:
    return False

  n_str = str(n)
  length = len(n_str)
  for i in range(length//2, 0, -1):
    if n_str[i - 1] != n_str[length - i]:
      return False
  return True

def main():
  limit = int(input('Enter an integer: '))
  largest_palindrome = None
  for i in range(1, limit + 1):
    for j in range(1, limit + 1):
      product = i * j
      if is_palindrome(product):
        if largest_palindrome is None or product > largest_palindrome:
          largest_palindrome = product
  print(largest_palindrome)

if __name__ == '__main__':
  main()
