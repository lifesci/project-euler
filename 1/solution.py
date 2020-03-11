def main():
  limit_str = input('Enter an integer limit: ')

  try:
    limit = int(limit_str)
  except ValueError as e:
    print('You must enter a valid integer')
    return

  sum = 0
  for i in range(limit):
    if (i % 3 == 0) or (i % 5 == 0):
      sum += i
  print(sum)

if __name__ == '__main__':
  main()
