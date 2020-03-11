def check(n, lim):
  for i in range(2, lim):
    if n % i != 0:
      return False
  return True

def main():
  lim = int(input('Enter an integer: '))
  cur = lim
  while(True):
    if (check(cur, lim)):
      print(cur)
      return
    cur += lim

if __name__ == '__main__':
  main()
