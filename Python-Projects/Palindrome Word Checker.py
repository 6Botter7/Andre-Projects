isWord = input("Please enter a word :  ")

for i in range(1):
    palindrome = isWord[::-1]
    if palindrome == isWord:
        print("The word is a Palindrome")
    elif not palindrome == isWord:
        print("The word is not a Palindrome")
# --------------------------------------------------

student = "@student.college.edu"
prof = "@prof.college.edu"
student_E = 0
prof_E = 0

no_emails = int(input("How many emails do you want to enter"))

for i in range(no_emails):
    entered_emails = input("Enter a email")

    print(entered_emails)
    if entered_emails == student:
        print("This is a student email")
        student_E = student_E + 1

    elif entered_emails == prof:
        print("This is a Proffesor email")
        prof_E = prof_E + 1

print(f"There are {student_E} student emails")
print(f"There are {prof_E} professor emails")
