import math

#for user input value

a = float(input("Enter a number: "))



#for calculating square root of number

square_root = math.sqrt(a)



# o Natural logarithm (log base e) of the number
# # Handle the case where the number is non-positive for logarithm


if a <= 0:
    natural_log = "Undefined (logarithm of non-positive number)"
else:
    natural_log = math.log(a)


# for sine value of number

sine_value = math.sin(a)


print(f"Square Root: {square_root}")
print(f"Natural Logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")

