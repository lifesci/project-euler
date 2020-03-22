ones = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

words=''
for i in range(1, 1001):
    if i == 1000:
        words += 'onethousand'
    else:
        word = ''
        hundreds = i // 100
        num_ones = i % 100
        if hundreds > 0:
            word += f'{ones[hundreds - 1]}hundred'
        if hundreds > 0 and num_ones > 0:
            word += 'and'
        if num_ones > 0 and num_ones < 20:
            word += ones[num_ones - 1]
        else:
            num_tens = num_ones // 10
            if num_tens > 0:
                word += tens[num_tens - 2]
            num_ones = num_ones % 10
            if num_ones > 0:
                word += ones[num_ones - 1]
        words += word

print(len(words))
