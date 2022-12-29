#Check the number is even or not and if the number is even then do the sum of all digits from that no. to 100

n = int(input("Enter a no. : "))

if n%2 == 0:
    s = 0
    for i in range(n,101):
        if i%2 ==0:
            s = s+i
    print(s)

else :
    print("Given number is odd and further operation cannot takes place............")
