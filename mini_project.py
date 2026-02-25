def calculator(course, marks):
    course = course.strip().lower()

    if course == "ai":
        fee = 40000
    elif course == "bi":
        fee = 50000
    elif course == "ci":
        fee = 60000
    else:
        print("Invalid course")
        return None

    if marks > 90:
        print("Discount applied: 5000")
        fee -= 5000

    return fee


def main():
    course = input("Enter course (AI/BI/CI): ")

    try:
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Please enter marks between 0 and 100")
            return

        total_fee = calculator(course, marks)

        if total_fee is not None:
            print("Final Fee:", total_fee)

    except ValueError:
        print("Please enter valid numeric marks")


main()
