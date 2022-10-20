# To display the Fibonacci

Fiboterms = int(input("Enter the number of Fibo terms? "))

# the ten terms
fib1, fib2, fib3, fib4, fib5, fib6, fib7, fib8, fib9, fib10 = 0,1,1,2,3,5,8,13,21,34
count = 0

if Fiboterms <= 0:
   print("Please enter a positive integer")
# if one return fib1
elif Fiboterms == 1:
   print("Fibonacci sequence upto",Fiboterms,":")
   print(fib1)
# generat fibo sequence
else:
   print("Fibonacci sequence:")
   while count < Fiboterms:
       print(fib1)
       nth = fib1 + fib2
       fib1 = fib2
       fib2 = nth
       count += 1