# from https://www.codewars.com/kata/55143152820d22cdf00001bb/train
# Prompt: Write a function count_nines(num) such that...
#   Given a positive integer `num`,
#   count the occurrences of the digit 9 in ALL intermediary numbers.
#   example: count_nines(9) == 1 because the number digit nine shows up in the number 9 once
#   example: count_nines(99) == 20
#   9, 19, 29...89 all add ONE occurence of 9
#   90 - 98 all add ONE occurence of 9
#   99 adds TWO occurences of 9

# spec: count_nines(num: integer): integer

def count_nines(num):
    # Your code here!
    return None


def run_tests():
    fixed_tests = [
        (1, 8, 0, "No nines before nine"),
        (2, 9, 1, "Nine itself is the first occurrence of the digit 9"),
        (3, 10, 1, ""),
        (4, 99, 20, "Should consider numbers where 9 is not only in the ones place"),
        (5, 200, 40, ""),
        (6, 908, 189, ""),
        (7, 909, 191, ""),
        (8, 99999, 50000, "Should enjoy big numbers!")
    ]
    print("Testing...\n")
    for tst, ipt, opt, rsn in fixed_tests:
        result = count_nines(ipt)
        print(f"Test number {tst}: count_nines({ipt}) == {result}. Expect {opt}.")
        try:
            assert count_nines(ipt) == opt, rsn
            print("Test passed!\n")
        except:
            print(f"Test failed! Expected {opt}, got {result}\n")

run_tests()
