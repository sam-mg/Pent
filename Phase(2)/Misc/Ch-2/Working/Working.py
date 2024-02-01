import subprocess
import base64

executable_path = '/home/dsg/Downloads/script'

def rot(data, ky):
    result = ''
    for char in data:
        if char.isalpha():
            offset = ky if char.islower() else - ky
            decoded_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26) + ord('a' if char.islower() else 'A'))
            result += decoded_char
        else:
            result += char
    return result

def hex(data):
    hex_values = data.split()
    ascii_result = ''.join(chr(int(val, 16)) for val in hex_values)
    return ascii_result

def bs64(data):
    try:
        decoded_bytes = base64.b64decode(data)
        ascii_result = decoded_bytes.decode('utf-8')
        return ascii_result
    except Exception as e:
        return f"Error decoding base64: {str(e)}"

def octal(data):
    octal_values = data.split()
    ascii_result = ''.join(chr(int(val, 8)) for val in octal_values)
    return ascii_result

def decimal(data):
    decimal_values = data.split()
    ascii_result = ''.join(chr(int(val)) for val in decimal_values)
    return ascii_result

try:
    process = subprocess.Popen(executable_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture and print the introductory message
    intro_message = process.stdout.readline().strip()
    print(intro_message)

    # Loop to interact with the executable
    while True:
        # Get the question from the subprocess output
        question = process.stdout.readline().strip()

        # Break the loop if the subprocess has finished
        if not question:
            break

        print(f"{question}")

        if "Good" in question:
            while True:
                # Read the next line only if the subprocess has not finished
                next_line = process.stdout.readline().strip()
                print(next_line)

                if 'Good' in next_line:
                    # while True:
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)

                        process.stdin.write('good\n')
                        print('ok')
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)                    
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        next_question = process.stdout.readline().strip()
                        print(next_question)
                        break

                if "Decode the caeser" in next_line:
                    start_index = next_line.find("Decode the caeser ") + len("Decode the caeser ")
                    end_index_a = next_line.find(" with key ")
                    start_index_b = end_index_a + len(" with key ")

                    a = 'rot'
                    encoded_string = next_line[start_index:end_index_a]
                    key1 = next_line[start_index_b:]

                    if a == 'rot':
                        ans1 = rot(encoded_string, -(int(key1)))
                        process.stdin.write(ans1 + '\n')
                        process.stdin.flush()
                    
                    print(ans1)

                # Check if the subprocess is ready for the next question
                elif "Better luck next time" in next_line:
                    break
                
        else:
            # Extract values of a and b for regular questions
            start_index = question.find("Decode the ") + len("Decode the ")
            end_index_a = question.find(" encoded string: ")
            start_index_b = end_index_a + len(" encoded string: ")

            a = question[start_index:end_index_a]
            b = question[start_index_b:]

            # Decode based on the type specified in a
            if a == 'rot_13':
                ans = rot(b, 13)
            elif a == 'hex':
                ans = hex(b)
            elif a == 'octal':
                ans = octal(b)
            elif a == 'decimal':
                ans = decimal(b)
            elif a == 'base64':
                ans = bs64(b)

            if ans != '':
                process.stdin.write(ans + '\n')
                process.stdin.flush()

            # Print the question and decoded string
            print(ans)

    # Close stdin to signal the subprocess that no more input will be provided
    process.stdin.close()

    # Wait for the subprocess to finish and get the final output and errors
    output, error = process.communicate()

    if error:
        print("Error:", error)

    print("Final Output:", output)

except Exception as e:
    print(f"Error: {e}")
