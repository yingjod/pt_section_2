number=eval (input("Enter a three-digit integer : "))
reversednumber=(number%10)*100+(number//10%10)*10+(number//100)

if number==reversednumber:
    print(number,'is a palindrome number . ')
else:
    print(number,"is not a palindrome number . ")