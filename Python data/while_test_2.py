total=0
for i in range(10):
    grade = input("give me a grade between 1 and 10")
    while not grade.isdigit() or int(grade) <1 or int(grade)>10:
        print("incorrect, give again")
        grade = input(f"give me the {i} grade between 1 and 10")
    total+=int(grade)
print(total/10)

    