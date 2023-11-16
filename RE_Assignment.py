import re

fn = open("regex_sum_1928027.txt","r")

#There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

total = 0

for line in fn:
    #print(line)

    #read all the numbers in the line and return then as list to num
    num = re.findall('[0-9]+',line)
    for n in num:
        if n.strip() != "":
            total = int(n) + total
            #print(n)
        
    
print(total)
        


    


