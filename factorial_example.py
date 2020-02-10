def factorial_function(number):
   # Perform a check whether the input number is positive or not, if it is not
   # positive, raise an assert
    assert number >= 0. and type(number) is int, "The input is not recognized"
 
    if number == 0:
        return 1
    else:
      # recursive function to calculate factorial
        return number * factorial_function(number-1)




print(factorial_function(5))