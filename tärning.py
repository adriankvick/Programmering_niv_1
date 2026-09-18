import random

your_rannum = random.randint(1,6)
cpu_rannu = random.randint(1,6)

print(f"You rolled a {your_rannum}")
print(f"Cpu rolled a {cpu_rannu}")

if your_rannum > cpu_rannu:
    print("You won!!")
elif your_rannum == cpu_rannu:
    print("Its a tie!!")
else:
    print("You lost!!")