#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a list of percentage marks and calculates the average.

# This function calculates teh average of the entered marks
def calc_average(marks):
    sumnum = 0
    # Checking to ensure the list had items in it
    if len(marks) == 0:
        return -1
    else:
        # Calculating the sum
        for a_num in marks:
            sumnum += a_num
        # calculating the average
        avg = sumnum / len(marks)
        return avg


def main():
    print(
        "Enter your marks as a percentage. When you're ready to calculate "
        + "the average, just enter '-1'. Calculated numbers must be between 0-100"
    )

    u_marks = []
    new_num = None
    end = -1
    # end is the assigned to the value that will be entered to start the calcs
    while new_num != end:
        temp_num = input("Enter a mark: ")
        try:
            new_num = float(temp_num)
            # adding the input to the list
            if (new_num <= 100) and (new_num >= end):
                u_marks.append(new_num)
            else:
                print("That number was not within the valid range")
        except ValueError:
            print("That was an invalid number")
    # Getting rid of the -1
    u_marks.pop()
    average = calc_average(u_marks)

    if average == end:
        print("No marks were entered :/")
    else:
        print("Your average was {:.2f}%".format(average))


if __name__ == "__main__":
    main()
