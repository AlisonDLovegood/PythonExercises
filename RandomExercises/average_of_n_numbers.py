from audioop import avg
import numbers


num = int(input("How many numbers will you use? "))
total_sum = 0

for n in range(num):
    numbers = float(input("Enter with a number: "))
    total_sum += numbers

avg = total_sum / num

print(f"The average is: {avg:,.2f}")
