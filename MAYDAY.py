input_string = input().split(' ') 


Code_dict = {"Zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Dash":'-'}


for i in input_string:
    print(Code_dict.get(i,i[0]),end="")


# Question: We have a problem that gives us a string that is all letters and words and we need to decode it.
# The numbers in this string are equal to their English names 
# and the dashes are also equal to their English names like the numbers.
# The rest of the decoded words are equal to the first letter of their word.
