student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
counter = 0

for height in student_heights:
    total_height += height
    counter += 1

average_height = total_height/counter

average_height = round(average_height)

print(average_height)
    
