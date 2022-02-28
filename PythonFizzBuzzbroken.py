Number = 0 #Took away the == and changed it to =
while Number != 100:
 Number = Number + 1
 Buzz = int(Number % 5  == 0) #Took away the == and changed it to =
 Fizz = int(Number % 3 == 0) #Took away the == and changed it to =
 FizzBuzz = int(Number % 15 == 0) #Took away the == and changed it to =

 if FizzBuzz == True:
  print('Fizzbuzz')#added quotes to get the print statements
 else:
  if Fizz == True:
    print('Fizz')#added quotes to get the print statements
  else:
    if Buzz == True:
        print('Buzz')#added quotes to get the print statements
    else:
     print('Number') #added quotes to get the print statements
