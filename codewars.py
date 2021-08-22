# 8 kyu
from string import punctuation
import math as m


def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)


def main(verb, noun):
    return verb + noun


def total_goals():
    la_liga_goals, champions_league_goals, copa_del_rey_goals = 43, 10, 5
    return la_liga_goals + champions_league_goals + copa_del_rey_goals


def feast(beast, dish):
    return beast[:1] == dish[:1] and beast[-1:] == dish[-1:]


def to_alternating_case(string):
    return string.swapcase()


def two_sort(array):
    array.sort()
    return str('***'.join(array[0]))
    # return '***'.join(min(array))


def reverse_words(s):
    return ' '.join(s.split(' ')[::-1])


def find_smallest_int(arr):
    return min(arr)

# 7 kyu


def prev_mult_of_three(n):
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
    return '  '.join((s.replace(' ', '').upper()))


def solution(nums):
    return [] if nums == None else sorted(nums)


def reverse_words(text):
    return ' '.join(reversed(text[::-1].split(' ')))


def is_square(n):
    return False if n < 0 else int(m.sqrt(n) + 0.5) ** 2 == n


def is_square2(n):
    if n > 0 and n % m.sqrt(n) == 0:
        return True
    elif n == 0:
        return True
    else:
        return False


def is_prime(n):
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
    return (m.sqrt(n) + 1) ** 2 if m.sqrt(n).is_integer() else -1


def split_in_parts(s, part_length):
    return ' '.join([s[i:i+part_length] for i in range(0, len(s), part_length)])


def vowel_change(txt, vow):
    return txt.replace(
        'a', vow).replace(
        'e', vow).replace(
        'o', vow).replace(
        'u', vow).replace(
        'i', vow)


def vowel_change2(txt, vow):  # to lepsze XDDDDD
    return txt.translate(str.maketrans("aiueo", vow * 5))


def word_splitter(string1):
    result = string1.translate(str.maketrans(
        punctuation, ':' * len(punctuation)))
    return result.split(':') if ':' in result else None


def square_digits(num):
    return int(''.join([str(int(i) ** 2) for i in str(num)]))

# 6 kyu
