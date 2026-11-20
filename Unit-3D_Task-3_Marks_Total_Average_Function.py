def total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
m1, m2, m3 = 85, 90, 78
total, average = total_and_average([m1, m2, m3])
print("Total Marks:", total)
print("Average Marks:", average)