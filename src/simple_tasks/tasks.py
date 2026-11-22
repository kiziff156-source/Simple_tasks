import math
from collections import Counter
from shlex import split


def isValid(s) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    brackets = {")": "(", "]": "[", "}": "{"}
    b_list = []
    for bracket in s:
        if bracket not in brackets:
            b_list.append(bracket)
            continue
        else:
            if b_list and b_list[-1] == brackets[bracket]:
                b_list.pop()
            else:
                return False
    return not b_list


def add_one(num: list[int]) -> list[int]:
    number = num.copy()
    for i in range(len(number) - 1, -1, -1):
        number[i] = number[i] + 1
        if number[i] > 9:
            number[i] = 0
        else:
            return number

    return [1] + number


def zero_to_end(nums: list[int]) -> list[int]:
    for i, num in enumerate(nums):
        if nums[i] != 0:
            continue
        else:
            for j in range(i, len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
    return nums


def sorted_nums(nums1: list[int], nums2: list[int]) -> list[int]:
    sorted_nums = []
    j = 0
    i = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            sorted_nums.append(nums1[i])
            i += 1
        else:
            sorted_nums.append(nums2[j])
            j += 1
    sorted_nums.extend(nums1[i:])
    sorted_nums.extend(nums2[j:])
    return sorted_nums


def reverse_word(s: str) -> str:
    words = s.split()
    return " ".join(words[::-1])


def words_count(s: str) -> int:
    words_number = len(s.split())
    return words_number


def words_count2(s: str) -> int:
    if not s:  # пустая строка
        return 0
    count = 0
    for i in range(len(s)):
        if s[i] != " ":
            if i == 0 or s[i - 1] == " ":
                count += 1
    return count


def without_duplicates(s: str) -> str:
    return " ".join(dict.fromkeys(s))


def without_duplicates2(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def without_duplicates3(s: str) -> str:
    unique = {char: None for char in s}
    return "".join(unique.keys())


def short_string(s: str) -> str:
    if len(set(s)) * 2 >= len(s):
        return s
    else:
        count = 1
        short_string = ""
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                short_string = short_string + s[i - 1] + str(count)
                count = 1
        short_string = short_string + s[i] + str(count)
    return short_string


def is_palindrome_permutation(s: str) -> bool:
    counts = Counter(s)
    odd = 0
    for key, value in counts.items():
        if value % 2 == 0:
            continue
        else:
            if len(s) % 2 == 0:
                return False
            else:
                odd += 1
    return odd < 2


def is_palindrome_permutation2(s: str) -> bool:
    counts = Counter(s)
    # Считаем, сколько значений в словаре являются нечетными
    odd_count = sum(1 for value in counts.values() if value % 2 != 0)
    return odd_count <= 1


def most_common_char(s: str) -> str:
    if not s:
        return ""
    counts = Counter(s)
    return counts.most_common(1)[0][0]


def most_common_char2(s: str) -> str:
    if not s:
        return ""
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    max_char = ""
    max_count = 0

    for char, count in counts.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char


def most_common_char_short3(s: str) -> str:
    if not s:
        return ""
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # key=counts.get говорит функции max: "сравнивай не сами буквы, а их значения из словаря"
    return max(counts, key=counts.get)


def is_palindrome_clean(s: str) -> bool:
    cleaned = [s.lower() for char in s if char.isalpha()]
    return cleaned == cleaned[::-1]


def is_anagram(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    counts1 = {}
    for char in s1.lower():
        if char not in counts1:
            counts1[char] = counts1.get(char, 0) + 1
    counts2 = {}
    for char in s2.lower():
        if char not in counts2:
            counts2[char] = counts2.get(char, 0) + 1
    return counts1 == counts2


def first_unique_char(s: str) -> int | None:
    if not s:
        return -1
    chars = {}
    for i, char in enumerate(s):
        if char not in chars:
            chars[char] = i
        else:
            chars[char] = -1
    for char, index in chars.items():
        if index != -1:
            return index
    return -1


def is_simple(num: int) -> bool:
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True


def count_vowels(s: str) -> int:
    vow = "aeyuio"
    count = sum(1 for char in s.lower() if char in vow)
    return count


def second_max(nums: list[int]) -> int:
    max1 = max2 = nums[0]
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max2


def count_words(s: str) -> int:
    words = s.split()
    return len(words)


def unique_elements(s: str) -> bool:
    unique = set(s)
    return len(unique) == len(s)


def unique_elements(lst: list) -> bool:
    elements = set()
    for element in lst:
        if element not in elements:
            elements.add(element)
        else:
            return False
    return True


def only_odd(nums: list[int]) -> list[int]:
    odds = [num for num in nums if num % 2 != 0]
    return odds


def join_words(s: list[str]) -> str:
    return " ".join(s)


# Selection Sort
def selection_sort(s: list[str]) -> list[str]:
    n = len(s)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if len(s[j]) < len(s[min_idx]):
                min_idx = j
        if min_idx != i:
            s[i], s[min_idx] = s[min_idx], s[i]
    return s


# InsertionSort
def insertion_sort(s: list[str]) -> list[str]:
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and len(s[j]) > len(key):
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key


# QuickSort
def quick_sort(s: list[str]) -> list[str]:
    if len(s) <= 1:
        return s  # выход из рекурсии

    pivot = s[len(s) // 2]  # Выбираем средний элемент как опорный
    left = [x for x in s if len(x) < len(pivot)]
    middle = [x for x in s if len(x) == len(pivot)]
    right = [x for x in s if len(x) > len(pivot)]

    return quick_sort(left) + middle + quick_sort(right)


# MergeSort
def merge_sort(s: list[str]) -> list[str]:
    # Базовый случай рекурсии: список из 0 или 1 элемента уже отсортирован
    if len(s) <= 1:
        return s

    # 1. Разделение: находим середину и делим список на две части
    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]

    # 2. Рекурсивный вызов: сортируем каждую часть отдельно
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. Слияние: объединяем две отсортированные части в одну
    return merge(left_sorted, right_sorted)


def merge(left: list[str], right: list[str]) -> list[str]:
    result = []
    i = j = 0

    # Сравниваем элементы из левого и правого списков
    while i < len(left) and j < len(right):
        if len(left[i]) <= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы (если один из списков закончился раньше)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def comare_versions(s1: str, s2: str) -> str:
    v1 = list(map(int, s1.split('.')))
    v2 = list(map(int, s2.split('.')))
    if v1 < v2:
        return f"{v2} более новая версия"
    elif v1 > v2:
        return f"{v1} более новая версия"
    else:
        return f"{v1} и {v2} одна и та же версия"


def remove_all_duplicates(s: list[str]) -> list[str]:
    return list(set(s))


def remove_duplicates_loop(nums: list) -> list:
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def compare_arrays(nums1: list[str], nums2: list[str]) -> bool:
    lenth1 = len(nums1)
    lenth2 = len(nums2)
    if lenth1 != lenth2:
        return False
    i = 0
    while i < lenth1:
        if nums1[i] != nums2[i]:
            return False
        i += 1
    return True


def compare_arrays2(nums1: list[str], nums2: list[str]) -> bool:
   if nums1==nums2=='':
        return True
   if len(nums1) != len(nums2):
       return False
   result = (False for i in range(len(nums1)) if nums1[i] != nums2[i])
   return result if result else True

def compare_arrays3(nums1: list[str], nums2: list[str]) -> bool:
    return nums1 == nums2

def minimum (nums: list[int]) ->int:
    return min(nums)

def minimum_2 (nums: list[int]) ->int|None:
    if nums:
        length = len(nums)
        i = 0
        min = nums[0]
        while i<length:
            if nums[i] < min :
                min = nums[i]
            i+=1
    else:
        return None
    return min
