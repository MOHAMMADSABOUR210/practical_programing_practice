Three_digit=[]
for i in range(100,1000):
    if i % 3 == 0:
            string_i = str(i)
            if (string_i[0] == string_i[1] ) or (string_i[0] == string_i[2]) or (string_i[1] == string_i[2]):
                if  not (string_i[0] == string_i[1] == string_i[2] ):
                    Three_digit.append(i)
print(Three_digit)

# Question: Finding three-digit numbers divisible by 3 that are made with only two different numbers