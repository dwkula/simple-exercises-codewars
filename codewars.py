# 8 kyu
import itertools
from collections import Counter
from fractions import Fraction
from re import X
from string import printable, punctuation
import math
from typing import Dict


def greet(name):
    # https://www.codewars.com/kata/55225023e1be1ec8bc000390
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)


def main(verb, noun):
    # https://www.codewars.com/kata/56dae9dc54c0acd29d00109a
    return verb + noun


def total_goals():
    # https://www.codewars.com/kata/55ca77fa094a2af31f00002a
    la_liga_goals, champions_league_goals, copa_del_rey_goals = 43, 10, 5
    return la_liga_goals + champions_league_goals + copa_del_rey_goals


def feast(beast, dish):
    # https://www.codewars.com/kata/5aa736a455f906981800360d
    return beast[:1] == dish[:1] and beast[-1:] == dish[-1:]


def to_alternating_case(string):
    # https://www.codewars.com/kata/56efc695740d30f963000557
    return string.swapcase()


def two_sort(array):
    # https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
    array.sort()
    return str('***'.join(array[0]))
    # return '***'.join(min(array))


def reverse_words(s):
    # https://www.codewars.com/kata/51c8991dee245d7ddf00000e
    return ' '.join(s.split(' ')[::-1])


def find_smallest_int(arr):
    # https://www.codewars.com/kata/55a2d7ebe362935a210000b2
    return min(arr)

# 7 kyu


def prev_mult_of_three(n):
    # https://www.codewars.com/kata/61123a6f2446320021db987d
    solution = list(str(n))
    i = 0
    while i < len(solution):
        if int(''.join(solution)) % 3 == 0:
            return int(''.join(solution))
        else:
            solution.pop()


def prev_mult_of_three2(n):
    while n % 3:
        n //= 10
    return n or None


def vaporcode(s):
    # https://www.codewars.com/kata/5966eeb31b229e44eb00007a
    return '  '.join((s.replace(' ', '').upper()))


def solution(nums):
    # https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
    return [] if nums == None else sorted(nums)


def reverse_words(text):
    # https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
    return ' '.join(reversed(text[::-1].split(' ')))


def is_square(n):
    # https://www.codewars.com/kata/54c27a33fb7da0db0100040e
    return False if n < 0 else int(math.sqrt(n) + 0.5) ** 2 == n


def is_square2(n):
    if n > 0 and n % math.sqrt(n) == 0:
        return True
    elif n == 0:
        return True
    else:
        return False


def is_prime(n):
    # https://www.codewars.com/kata/53daa9e5af55c184db00025f
    dividors = 0
    if n <= 1:
        return False
    for i in range(n):
        if n % (i+1) == 0:
            dividors += 1
            if dividors > 2:
                return False
    return True


def is_prime2(n):
    return n > 1 and all(n % i for i in range(2, n))


def find_next_square(n):
    # https://www.codewars.com/kata/56269eb78ad2e4ced1000013
    return (math.sqrt(n) + 1) ** 2 if math.sqrt(n).is_integer() else -1


def split_in_parts(s, part_length):
    # https://www.codewars.com/kata/5650ab06d11d675371000003
    return ' '.join([s[i:i+part_length] for i in range(0, len(s), part_length)])


def vowel_change(txt, vow):
    # https://www.codewars.com/kata/597754ba62f8a19c98000030
    return txt.replace(
        'a', vow).replace(
        'e', vow).replace(
        'o', vow).replace(
        'u', vow).replace(
        'i', vow)


def vowel_change2(txt, vow):
    return txt.translate(str.maketrans("aiueo", vow * 5))


def word_splitter(string1):
    # https://www.codewars.com/kata/584d88622609c8bda30000cf
    result = string1.translate(str.maketrans(
        punctuation, ':' * len(punctuation)))
    return result.split(':') if ':' in result else None


def square_digits(num):
    # https://www.codewars.com/kata/546e2562b03326a88e000020
    return int(''.join([str(int(i) ** 2) for i in str(num)]))


def is_isogram(string):
    # https://www.codewars.com/kata/54ba84be607a92aa900000f1/
    return len(string.lower()) == len(set(string.lower()))
# 6 kyu


def comp(array1, array2):
    # https://www.codewars.com/kata/550498447451fbbd7600041c
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False


def get_gcd(num1, num2):
    # greatest common divisor
    while (num2):
        num1, num2 = num2, num1 % num2
    return num1


def get_lcm(num1, num2):
    # least common multiple
    return (num1*num2) / get_gcd(num1, num2)


def sum_fracts(lst):
    # https://www.codewars.com/kata/5517fcb0236c8826940003c9
    if lst == [] or None:
        return None

    divisors = []
    numerators = []

    for i in lst:
        divisors.append(i[1])
        numerators.append(i[0])

    def divisor(divisors):
        result = 1
        for x in divisors:
            result = result * x
        return result

    multiplied_divisors = divisor(divisors)

    def numerator(numerators, divisors):
        num_multipliers = []
        for j in divisors:
            num_multipliers.append(multiplied_divisors/j)
        multiplied_numerators = [n * multi for n,
                                 multi in zip(numerators, num_multipliers)]
        return int(sum(multiplied_numerators))

    num = numerator(numerators, divisors)
    div = divisor(divisors)

    num_div_gcd = math.gcd(num, div)

    if div/num_div_gcd == 1:
        final = int(num/num_div_gcd)
        return final
    else:
        final = []
        final.append(int(num/num_div_gcd))
        final.append(int(div/num_div_gcd))
        return final


def sum_fracts2(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]


def backwards_prime(start, stop):
    # https://www.codewars.com/kata/5539fecef69c483c5a000015
    primes = []
    backward_primes = []

    for x in range(start, stop):
        if all(x % i for i in range(2, x)):
            primes.append(x)

    for a in primes:
        reversed_x = int(str(a)[::-1])
        if reversed_x > 10 and all(reversed_x % i for i in range(2, reversed_x)):
            backward_primes.append(a)

    return backward_primes


def find_it(seq):
    # https://www.codewars.com/kata/54da5a58ea159efa38000836
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


def solution(number):
    # https://www.codewars.com/kata/514b92a657cdc65150000006
    return sum([i for i in range(2, number) if i % 3 == 0 or i % 5 == 0])


def array_diff(a, b):
    # https://www.codewars.com/kata/523f5d21c841566fde000009
    return [item for item in a if item not in b]


def longest_repetition(chars):
    # https://www.codewars.com/kata/586d6cefbcc21eed7a001155
    max_count = 0
    previous = None
    max = None

    if chars == '':
        return ('', 0)

    for char in chars:
        if previous == char:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max = char
        previous = char
    return (max, max_count)


def high(x):
    # https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
    pass


# 5 kyu


def move_zeros(array):
    # https://www.codewars.com/kata/52597aa56021e91c93000cb0
    zeros = array.count(0)
    final = [number for number in array if number != 0]

    for i in range(zeros):
        final.append(0)

    return final
