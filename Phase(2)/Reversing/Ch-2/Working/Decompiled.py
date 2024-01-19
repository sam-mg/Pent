# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ./chall.py
# Compiled at: 2024-01-18 13:14:06


def modify_string(input_str):
    modified_str = ''
    for i in range(len(input_str)):
        char = input_str[i]
        if i % 2 == 0:
            modified_str += chr(ord(char) - 3)
        else:
            modified_str += chr(ord(char) + 2)

    return modified_str


def main():
    user_input = input('Enter a string: ')
    modified_input = modify_string(user_input)
    target_string = 'cn^ixelomkigaam{qjlp<Az'
    if modified_input == target_string:
        print ('Congratulations! You got the correct modified string.')
    else:
        print ("Sorry, the modified string doesn't match the target.")


if __name__ == '__main__':
    main()