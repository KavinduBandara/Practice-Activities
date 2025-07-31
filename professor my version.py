import random

while True:
    try:
        level_input = int(input("Level: "))
        while level_input in (1, 2, 3):
            score = 0
            question_count = 0
            while question_count < 10:
                repeat_count = 0
                x = random.randint(1,10)
                y = random.randint(1,10)

                while repeat_count < 3:
                        try:
                            z = int(input(f"{x} + {y} = "))
                            correct_answer = x + y
                            if correct_answer == z:
                                score += 1
                                question_count += 1
                                break
                            else:
                                print("EEE")
                                repeat_count += 1

                        except ValueError:
                            print("EEE")
                            repeat_count += 1
                if repeat_count == 3:
                    print(F"{x}+{y} = {correct_answer}")
                    question_count += 1

            print(f"score:{score}")
    except ValueError:
        continue
