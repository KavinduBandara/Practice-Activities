import random


if question_count >= 10:
    x = random.randint(1,10)
    y = random.ranndint(1,10)

    try:
        z = int(input(f"{x}+{y}"))
        k = x + y
        question_count =0

        if x + y == z:
            score = 0
            score = score + 1
            question_count = question_count + 1
            #return to the 1st line

        else:
            print("EEE")
            if repeat_count>=3:
                print(f"{x}+{y}")
                question_count = question_count + 1
                    #reset repet count to 0
                    #return to the 1st line
            else:
                repeat_count= 0
                repeat_count = repeat_count + 1
                #return to the 6th line
    except ValueError:
        pass

else:
    print(f"score:{score}")


