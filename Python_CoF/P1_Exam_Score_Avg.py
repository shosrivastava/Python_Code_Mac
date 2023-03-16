print("This code calculates the total average scored in all the exams including their credit.\n")

no_of_exams = int(input("Enter the total number of exams: "))
total_credit= int(input("Enter the total credit all the exams cover: "))

average = 0

for i in range(no_of_exams):
    score = int(input("Enter the marks scored in this exam: "))
    credit = int(input("Enter the credit covered by this exam: "))

    average = average + score * credit / total_credit

print(f"You scored {average} as the total average in the exams.")