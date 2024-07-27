# Write your solution here
students = int(input("How many students on the course? "))
group = int(input("Desired group size? "))

num_groups = students // group
if students % group > 0:
    num_groups += 1
print(f"Number of groups formed: {num_groups}")
