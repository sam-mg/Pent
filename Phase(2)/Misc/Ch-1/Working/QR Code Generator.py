import base64

with open('/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-1/Working/file.txt', 'r') as file:
    ascii_numbers = file.read().split()
    text = ''.join(chr(int(num, 8)) for num in ascii_numbers)
    data = base64.b64decode(text)

with open('/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-1/Working/file.png', 'wb') as file:
    file.write(data)
