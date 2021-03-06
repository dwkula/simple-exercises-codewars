# 8 kyu
import string
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


def diamond(n):
    x = 1
    z = int((n-1)/2)
    diamond = ''
    for i in range(n):
        if x <= n:
            diamond += ' ' * z + '*' * x + ' ' * z+'\n'
            x += 2
            z -= 1

    for k in range(n):

        x -= 2
        z += 1
        diamond += ' ' * z + '*' * x + ' ' * z+'\n'
    return diamond


# function for each number 0-9
# function math operations: plus, minus, times, dividedBy
# each calc = 1 operation and 2 numbers
# the most outer - left operand, the most inner - right operand
# division = int div, rounding
def zero(operand=None):
    if operand is None:
        return 0
    if operand[0] == '+':
        return operand[1] + 0
    if operand[0] == '*':
        return operand[1] * 0
    if operand[0] == '//':
        if 0 <= operand[1]:
            return 0 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 0 <= operand[1]:
            return 0 - operand[1]
        else:
            return abs(0 - operand[1])


def one(operand=None):
    if operand is None:
        return 1
    if operand[0] == '+':
        return operand[1] + 1
    if operand[0] == '*':
        return operand[1] * 1
    if operand[0] == '//':
        if 1 <= operand[1]:
            return 1 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 1 <= operand[1]:
            return 1 - operand[1]
        else:
            return abs(1 - operand[1])


def two(operand=None):
    if operand is None:
        return 2
    if operand[0] == '+':
        return operand[1] + 2
    if operand[0] == '*':
        return operand[1] * 2
    if operand[0] == '//':
        if 2 >= operand[1]:
            return 2 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 2 <= operand[1]:
            return 2 - operand[1]
        else:
            return abs(2 - operand[1])


def three(operand=None):
    if operand is None:
        return 3
    if operand[0] == '+':
        return operand[1] + 3
    if operand[0] == '*':
        return operand[1] * 3
    if operand[0] == '//':
        if 3 >= operand[1]:
            return 3 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 3 <= operand[1]:
            return 3 - operand[1]
        else:
            return abs(3 - operand[1])


def four(operand=None):
    if operand is None:
        return 4
    if operand[0] == '+':
        return operand[1] + 4
    if operand[0] == '*':
        return operand[1] * 4
    if operand[0] == '//':
        if 4 >= operand[1]:
            return 4 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 4 <= operand[1]:
            return 4 - operand[1]
        else:
            return abs(4 - operand[1])


def five(operand=None):
    if operand is None:
        return 5
    if operand[0] == '+':
        return operand[1] + 5
    if operand[0] == '*':
        return operand[1] * 5
    if operand[0] == '//':
        if 5 >= operand[1]:
            return 5 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 5 <= operand[1]:
            return 5 - operand[1]
        else:
            return abs(5 - operand[1])


def six(operand=None):
    if operand is None:
        return 6
    if operand[0] == '+':
        return operand[1] + 6
    if operand[0] == '*':
        return operand[1] * 6
    if operand[0] == '//':
        if 6 >= operand[1]:
            return 6 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 6 <= operand[1]:
            return 6 - operand[1]
        else:
            return abs(6 - operand[1])


def seven(operand=None):
    if operand is None:
        return 7
    if operand[0] == '+':
        return operand[1] + 7
    if operand[0] == '*':
        return operand[1] * 7
    if operand[0] == '//':
        if 7 >= operand[1]:
            return 7 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 7 <= operand[1]:
            return 7 - operand[1]
        else:
            return abs(7 - operand[1])


def eight(operand=None):
    if operand is None:
        return 8
    if operand[0] == '+':
        return operand[1] + 8
    if operand[0] == '*':
        return operand[1] * 8
    if operand[0] == '//':
        if 8 >= operand[1]:
            return 8 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 8 <= operand[1]:
            return 8 - operand[1]
        else:
            return abs(8 - operand[1])


def nine(operand=None):
    if operand is None:
        return 9
    if operand[0] == '+':
        return operand[1] + 9
    if operand[0] == '*':
        return operand[1] * 9
    if operand[0] == '//':
        if 9 >= operand[1]:
            return 9 // operand[1]
        else:
            return 0
    if operand[0] == '-':
        if 9 <= operand[1]:
            return 9 - operand[1]
        else:
            return abs(9 - operand[1])


def plus(number):
    return '+', number


def minus(number):
    return '-', number


def times(number):
    return '*', number


def divided_by(number):
    return '//', number


def create_phone_number(n):
    # https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
    return f'({"".join([str(i) for i in n[0:3]])}) {"".join([str(i) for i in n[3:6]])}-{"".join([str(i) for i in n[6:10]])}'


def create_phone_number2(n):
    # https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def pig_it(text):
    # https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
    return ' '.join([word[1:] + word[0] +
                     'ay' if word not in '!?' else word for word in text.split(' ')])


def digital_root(n):
    # https://www.codewars.com/kata/541c8630095125aba6000c00/python
    if len(str(n)) == 1:
        return n

    return digital_root(eval('+'.join(list(str(n)))))


def digital_root2(n):
    # https://www.codewars.com/kata/541c8630095125aba6000c00/python
    return n if n < 10 else digital_root(sum(map(int, str(n))))


class PaginationHelper:
    # https://www.codewars.com/kata/515bb423de843ea99400000a
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = {}

        index = 0
        for i in range(0, len(self.collection), self.items_per_page):
            self.pages[index] = self.collection[i: i + self.items_per_page]
            index += 1

    # returns the number of items within the entire collection

    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection)/self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= len(self.pages):
            return -1

        return len(self.pages[page_index])

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if self.collection:
            if item_index < 0 or item_index >= len(self.collection):
                return -1
            for index, page in self.pages.items():
                if self.collection[item_index] in page:
                    return index

        else:
            return -1


def rgb(r, g, b):
    # https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
    rh, gh, bh = hex(r)[2:], hex(g)[2:], hex(b)[2:]
    if r < 0:
        rh = '0'
    if g < 0:
        gh = '0'
    if b < 0:
        bh = '0'

    if r > 255:
        rh = 'FF'

    if g > 255:
        gh = 'FF'

    if b > 255:
        bh = 'FF'

    if r < 10:
        rh = '0' + rh
    if g < 10:
        gh = '0' + gh
    if b < 10:
        bh = '0' + bh

    return f'{rh}{gh}{bh}'.upper()


def rgb2(r, g, b):
    # https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


def high(x):
    # https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/
    letters = {c: i+1 for i, c in enumerate(string.ascii_lowercase)}
    x_splt = x.split(' ')

    best_score = 0
    best_word = ''
    for word in x_splt:
        current_score = 0
        for c in word:
            current_score += letters[c]

        if best_score < current_score:
            best_score = current_score
            best_word = word

    return best_word


def high2(x):
    # https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def to_camel_case(text):
    # https://www.codewars.com/kata/517abf86da9663f1d2000003
    if not text:
        return ''
    first_letter = text[0]
    if '_' in text or '-' in text:
        result = first_letter + text.title().replace(' ', '')[1:]

        if '-' in result:
            result = result.replace('-', '')

        if '_' in result:
            result = result.replace('_', '')

    return result


def to_camel_case2(s):
    # https://www.codewars.com/kata/517abf86da9663f1d2000003
    return s[0] + s.title().translate({45:  None, 95: None})[1:] if s else s


def roman_numerals_encoder(n):
    # https://www.codewars.com/kata/51b62bf6a9c58071c600001b/solutions/python/me/best_practice
    values = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
              'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    roman = ''
    for key, value in reversed(values.items()):
        for _ in range(3):
            if n >= value:
                roman += key
                n -= value

    return roman


def fibonacci_it(n):
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a + b
        yield a


def perimeter(n):
    # https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python
    genfib = fibonacci_it(n)
    squares = 0

    for i in genfib:
        squares += i

    perimeters = squares * 4

    return perimeters


def find_outlier(integers):
    # https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
    evens = False
    count = 0
    for i in integers:
        if i % 2 == 0:
            count += 1
        if count >= 2:
            evens = True

    if evens:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i


def find_outlier(int):
    # https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


def nb_year(p0, percent, aug, p):
    # https://www.codewars.com/kata/563b662a59afc2b5120000c6
    years = 0

    while p0 < p:
        p0 = int(p0 + (p0 * (percent / 100.0)) + aug)
        years += 1

    return years


def find_even_index(arr):
    # https://www.codewars.com/kata/5679aa472b8f57fb8c000047
    found = False
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            found = True
            return index

    if not found:
        return -1


def narcissistic(value):
    # https://www.codewars.com/kata/5287e858c6b5a9678200083c/
    strvalue = str(value)
    csum = 0
    for c in strvalue:
        csum += int(c) ** len(strvalue)

    return csum == value


def tribonacci(signature, n):
    # https://www.codewars.com/kata/556deca17c58da83c00002db/
    if n > 0:
        for i in range(n - 3):
            signature.append(sum(signature[-3:]))

        if n < 3:
            return signature[:n]

        return signature

    return []


def anagrams(word, words):
    # https://www.codewars.com/kata/523a86aa4230ebb5420001e1/
    anagrams = []
    word = Counter(word)
    candidates = words
    for candidate in candidates:
        candidate_val = Counter(candidate)
        if word == candidate_val:
            anagrams.append(candidate)

    return anagrams


def longest(a1, a2):
    # https://www.codewars.com/kata/5656b6906de340bd1b0000ac/
    return ''.join(sorted(set(a1 + a2)))


def is_prime_optimized(n):
   # https://www.codewars.com/kata/5262119038c0985a5b00029f/solutions/python
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True


def printer_error(s):
    # https://www.codewars.com/kata/56541980fa08ab47a0000040/

    numerator = 0
    denumerator = 0
    for k, v in Counter(s).items():
        if k in 'abcdefghijklm':
            denumerator += v
        else:
            numerator += v

    return f'{numerator}/{denumerator + numerator}'
