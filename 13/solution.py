def read_nums(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    return content

def main():
    nums = read_nums('./nums.txt')
    carry = 0
    total = ''
    index = len(nums[0]) - 1
    while index >= 0:
        cur = carry % 10
        carry = carry // 10
        for num in nums:
            cur += int(num[index])
        carry += cur // 10
        total = str(cur % 10) + total
        index -= 1
    total = str(carry) + total
    print(total)

if __name__ == '__main__':
    main()
