# CodeWars challenge
# Euler project
# Function that returns the sum of all the multiples of 3 or 5 below the number passed in.\

# solution 1
def sm35(num):
    sum = 0

    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


# solution 2 - improved


def ssm35(num):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)


print(sm35(10))
print(ssm35(10))
