
input_string = input().split(' ') 

result = ''

def insert_char(orginal, char , position):
    return orginal[:position] + char + orginal[position:]


print(len(input_string))
for i in range(len(input_string)):
    if i+1 >= len(input_string):
        break
    print(input_string[i][0])
    temp_char = input_string[i][0]
    temp_digit = int(input_string[i][1:])
    result = insert_char(result,temp_char,temp_digit)


print(result)

# Question: We have a string line that contains characters like "T4" and is encoded.
# Write a program that can recognize the codes and output the correct string.