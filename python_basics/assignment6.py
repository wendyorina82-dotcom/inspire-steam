#Name:Wendy Orina
#Date:16/02/2026
#Program to draw a shapes using *

n = 5

# Top part
for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for star in range(2 * i - 1):
        print("*", end="")

    print()

# Bottom part
for i in range(n - 1, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    for star in range(2 * i - 1):
        print("*", end="")

    print()


n = 5

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end="")

    for star in range(2*i - 1):
        print("*", end="")

    print()