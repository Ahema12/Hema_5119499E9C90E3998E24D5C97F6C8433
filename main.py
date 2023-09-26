def Fact_rec(n):
 if n==0 or n==1:
  return 1
 else:
       return n* Fact_rec (n-1)
number =int(input("Enter a value:"))
res=Fact_rec( number )
print("The Factorial of {}is{}.".format(number, res))

