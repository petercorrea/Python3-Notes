# Numbers and Operations
2 + 3
3 - 2
3 * 2
40 / 2  # division
40 // 2  # integer division
2 ** 2  # exponent
9 % 3  # modulus
abs(-23)  # Absolute value
len("Peter")  # counts total elements
max([1, 2, 3])
min([4, 5, 6])
pow(5, 2)
divmod(8, 5)
round(5.32)
sum([1, 2, 3])

# Integer values between (-5, 256) always referenced the same object, Python preloads these values for optimization purposes
a = 4
b = 232
print(id(a))
print(id(b))  # Both variables reference the same objects