
def fizzbuzz(number):
    if (number > 0 and number < 300):
        counterOfThree = 0
        counterOfFive = 0
        result_message = {"answer": ""}

        for i in range(1, number + 1):
            counterOfFive += 1
            counterOfThree += 1

            if (counterOfThree == 3 and counterOfFive == 5):
                counterOfThree = 0
                counterOfFive = 0
                result_message["answer"] = "fizzbuzz"

            elif counterOfThree == 3:
                counterOfThree = 0
                result_message["answer"] = "fizz"

            elif counterOfFive == 5:
                counterOfFive = 0
                result_message["answer"] = "buzz"

            else:
                result_message["answer"] = ":( {} :(".format(number)
        return result_message["answer"]
    else:
        return 'I dont work with big and negative numbers'


def main():
    number = int(input())
    print(fizzbuzz(number))


if __name__ == '__main__':
    main()
