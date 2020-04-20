'''
Exercism problem: Nth Prime
Given a number n, determine what the nth prime is.
POSSIBLE TEST INPUTS
6 - 2, 3, 5, 7, 11, 13
10 - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
15 - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
PSEUDO
- Check for instant fail inputs(ex.negative numbers)
- Loop over the number amount of primes
- Devide index value by 2
- Devide again by previous primes appended to ensure its a prime number
- If all checks then append the index value
- return prime nummbers
'''


def nth_prime(number):
    if number < 0:
        raise ValueError('No negative numbers allowed')
    prime_numbers = [2]  # 2  is always in by default
    for index in range(number):
        if index == 0 or index == 1:
            continue
        result = str(index/2)
        if result[len(result)-1:] != "0":
            prime_flag = False
            for index2 in range(len(prime_numbers)):
                check = str(index/prime_numbers[index2])
                print(check, prime_numbers[index2])
                if check[len(result)-1:] == "0":
                    prime_flag = True
            if prime_flag is False:
                prime_numbers.append(index)
    return prime_numbers


print(nth_prime(10))
'''
Exercism problem: Pangram
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter")
is a sentence using every letter of the alphabet at least once.
POSSIBLE TEST INPUTS
FALSE - 'The goat jumped over the goat'
TRUE - 'The five boxing wizards jump quickly'
FALSE - 'The flying flamingoz went to quibo land'
PSEUDO
- Create a dictionary of all letters
- Ensure all letters have been checked at least once
- return True or False
OR
- Create a set of the string
-  check if the size of the letters is greater than 26
'''


def check_pangram(string):
    set_string = set(string.lower().replace(' ', ''))
    if len(set_string) >= 26:
        return True
    return False


test_Case = "abcdefghijklmnopqrstuvwxyz"
edge_Case = 'The flying flamingoz!!@3 went%$! to quibo*& land'
print(check_pangram(test_Case))  # True
print(check_pangram(edge_Case))  # False not because of the non ascii though
