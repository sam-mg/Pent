with open('/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-1/Working/file.txt', 'r') as file:
    ascii_numbers = file.read().split()
    text = ''.join(chr(int(num)) for num in ascii_numbers)

print(text)