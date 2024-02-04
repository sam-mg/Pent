from pwn import *
import base64

def rot(data, ky):
    odr = []
    x = list(data.lower())
    for i in range(len(x)):
        if x[i].isalpha():
            odr.append(ord(x[i]) - 97)
        else:
            odr.append(32)

    for j in range(len(odr)):
        if odr[j] == 32:
            continue
        else:
            odr[j] = (odr[j] + ky) % 26
    
    out = ''
    for k in range(len(odr)):
        if odr[k] == 32:
            out += ' '
        else:
            out += chr(odr[k] + 97)
    return out

def hexz(data):
    stg = ''.join(chr(int(i, 16)) for i in data)
    return stg

def bs64(data):
    return base64.b64decode(data).decode()

def octal(data):
    stg = ''.join(chr(int(i, 8)) for i in data)
    return stg

def decimal(data):
    stg = ''.join(chr(int(i)) for i in data)
    return stg

run = process('/home/sam-mg/Desktop/Pent/Phase(2)/Misc/Ch-2/Org File/script')

print(run.recvline().decode())

ctr1 = 10
while ctr1>=1:
    question = run.recvline().decode().strip().split()
    print(question)
    if question[2] == 'rot_13':
        ans = rot(question[-1], 13)
    if question[2] == 'hex':
        ans = hexz(question[5:])
    if question[2] == 'octal':
        ans = octal(question[5:])
    if question[2] == 'base64':
        ans = bs64(question[-1])
    if question[2] == 'decimal':
        ans = decimal(question[5:])
    print(ans)
    run.sendline(ans.encode())
    ctr1 -= 1

print(run.recvline().decode())
print(run.recvline().decode())
print(run.recvline().decode())

ctr2 = 10
while ctr2>=1:
    question = run.recvline().decode().strip().split()
    print(question)
    ans = rot(question[3], -int(question[-1]))
    run.sendline(ans.encode())
    print(ans)
    ctr2 -= 1

print(run.recvline().decode())
print(run.recvline().decode())
print(run.recvline().decode())
print(run.recvline().decode())

run.sendline('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.encode())

print(run.recvline().decode())
print(run.recvline().decode())
print(run.recvline().decode())

letters = run.recvline()
print(letters)

first_letter = 65
letters_dict = {}
for i in range(26):
    letters_dict[letters.decode().strip().split()[i+6]] = (chr(first_letter))
    first_letter += 1

print(run.recvline().decode())
print(run.recvline().decode())
print(run.recvline().decode())

ctr3 = 10
while ctr3 >= 1:
    question = run.recvline().decode().strip().split()
    print(question)
    ans = ''.join([letters_dict[x] for x in question[2:] if x in letters_dict])
    run.sendline(ans.encode())
    print(ans)
    ctr3 -= 1

print(run.recvline().decode())
print(run.recvline().decode())