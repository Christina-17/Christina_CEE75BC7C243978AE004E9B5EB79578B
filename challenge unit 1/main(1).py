# 1.1 Implement the recursive function to calculate the factorial of the given number


def factorial(n):
  if (n <= 1):
    return 1
  else:
    return (n * factorial(n - 1))


n = int(input("Enter the number for factorial:"))
print("The factorial of", n, "is", factorial(n))
