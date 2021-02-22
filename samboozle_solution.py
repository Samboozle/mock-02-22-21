from functools import reduce

def count_nines(num):
    digits = [int(rune) for rune in f"{num}"[::-1]]
    initializer = 0, 0, 0, 0

    def process_digit(accumulator, digit):
        running_total, iteration, add_per_order, original_number = accumulator
        power_of_ten = 10 ** iteration
        lead_nine = digit // 9 # 0 or 1
        new_total = running_total + lead_nine + lead_nine * \
            original_number + digit * add_per_order
        return new_total, iteration + 1, (add_per_order * 10) + power_of_ten, original_number + power_of_ten * digit

    answer, *_ = reduce(process_digit, digits, initializer)
    return answer

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
        print(
            f"Test number {tst}: count_nines({ipt}) == {result}. Expect {opt}.")
        try:
            assert count_nines(ipt) == opt, rsn
            print("Test passed!\n")
        except:
            print(f"Test failed! Expected {opt}, got {result}\n")


run_tests()
