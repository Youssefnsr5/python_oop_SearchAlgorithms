# #1
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)
# ****************************************************************************************************
# #2
# num = int(input("Enter a number: "))
# original_num = num
# num = abs(num)
# digit_sum = 0
# while num > 0:
#     digit = num % 10
#     digit_sum += digit
#     num //= 10

# print(f"The sum of the digits of {original_num} is: {digit_sum}")
# ****************************************************************************************************
# #3
# num = int(input("Enter a number: "))
# f = 1
# while num > 0:
#     f *= num
#     num -= 1
# print(f"The factorial of {num} is: {f}")
# ****************************************************************************************************
# #4
# a = int(input("Enter a number : "))
# multe = 0
# for i in range(1, 11):
#     multe = a * i
#     print(f"{a} x {i} = {multe}")
# ****************************************************************************************************
# #5
# x = int(input("Enter a number: "))

# if x <= 1:
#     print(f"{x} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, x):
#         if x % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{x} is a prime number.")
#     else:
#         print(f"{x} is not a prime number.")
# ****************************************************************************************************
# #6
# def reverse_integer(n):
#     reversed_num = 0
    
#     while n > 0:
#         digit = n % 10         
#         reversed_num *= 10 + digit
#         n //= 10                
        
#     return reversed_num

# ****************************************************************************************************
# #7
# str = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for char in str:
#     if char in vowels:
#         vowel_count += 1
# print(f"The number of vowels in the string is: {vowel_count}")

# ****************************************************************************************************
# #8

# def guessing_game():
#     secret_number = random.randint(1, 20)
    
#     while True:
#         guess = int(input("Guess a number between 1 and 20: "))
        
#         if guess < secret_number:
#             print("Too low! Try again.")
#         elif guess > secret_number:
#             print("Too high! Try again.")
#         else:
#             print("Congratulations! You guessed it right")
#             break

# guessing_game()


# ****************************************************************************************************
# #9
# def largest_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b
#         return c
#     else:
#         return "Three numbers are equal."
# print(largest_of_three(7, 9, 5))

# *********************************************************************************************
# #10

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]

#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         next_fib = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_fib)
#     return fib_sequence

# print(fibonacci(10))


# ****************************************************************************************************
# #11
# def is_palindrome(s):
#     return s == s[::-1]


# print(is_palindrome("madam"))
# print(is_palindrome("hello"))
# ***************************************************************************************************
# 12
# def count_even_odd(numbers):
#     odd_count = 0
#     even_count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return even_count, odd_count


# nums = [1, 2, 3, 4, 5, 6]

# even, odd = count_even_odd(nums)

# print("Even:", even)
# print("Odd:", odd)
# ****************************************************************************************************
# 13

# def score(n):
#     if n >= 90:
#         print("A")
#     elif n >= 80 and n <= 89:
#         print("B")
#     elif n >= 70 and n <= 79:
#         print("C")
#     elif n >= 60 and n <= 69:
#         print("D")
#     else:
#         print("F")

# print(score(95))
