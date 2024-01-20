def main(argc, argv, envp):
    v6 = [0] * 50

    if argc == 1:
        print("Usage: ./crackme FLAG")
        return 1
    elif len(argv[1]) == 21:
        for i in range(21):
            v6[24 + i] = ord(argv[1][i]) - 34

        v6[0] = 55
        v6[1] = 63
        v6[2] = 47
        v6[3] = 118
        v6[4] = 43
        v6[5] = 98
        v6[6] = 40
        v6[7] = 33
        v6[8] = 52
        v6[9] = 15
        v6[10] = 119
        v6[11] = 98
        v6[12] = 72
        v6[13] = 39
        v6[14] = 117
        v6[15] = 8
        v6[16] = 86
        v6[17] = 106
        v6[18] = 104
        v6[19] = 78
        v6[20] = 104

        for j in range(21):
            if chr(ord(argv[1][j]) ^ v6[24 + j]) != chr(v6[j]):
                print("Wrong flag")
                return 1

        print(f"You found a flag! {argv[1]}")
        return 0
    else:
        print("Wrong flag")
        return 1

# Example usage:
argc = 2  # example value, adjust as needed
argv = ["program_name", "CRACKTHECODEUSINGTHIS"]  # replace "your_flag_here" with the actual flag
envp = []  # example value, adjust as needed
result = main(argc, argv, envp)
print(result)
