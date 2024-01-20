lis = ([ord(i) - 34 for i in 'sup3r_s3cr3t_k3y_1337'])
give = [55,63,47,118,43,98,40,33,52,15,119,98,72,39,117,8,86,106,104,78,104]

for i in range(21):
    for j in range(127):
        if (lis[i] ^ j) == give[i]:
            print(chr(j), end='')
