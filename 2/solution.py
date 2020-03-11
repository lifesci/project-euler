def main():
  limit_str = input('Enter an integer limit: ')

  try:
    limit = int(limit_str)
  except ValueError:
    print('You must enter a valid integer')
    
  f_n1 = 1
  f_n2 = 2

  total = 2

  if limit <= 1:
    print(0)
    return

  if limit == 2:
    return total

  cur = 3
  while cur <= limit:
    if cur % 2 == 0:
      total += cur
    f_n1 = f_n2
    f_n2 = cur
    cur = f_n1 + f_n2
  
  print(total)

if __name__ == '__main__':
  main()
