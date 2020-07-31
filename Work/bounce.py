# bounce.py
#
#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the
#height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.
# Exercise 1.5

height = 100
for _ in range(10):
    height *= 0.6
    print(round(height, 4))

print("The final height is: ", round(height, 4))
