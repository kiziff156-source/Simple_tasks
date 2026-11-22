import pytest

from src.simple_tasks.tasks import isValid, add_one, zero_to_end, sorted_nums, reverse_word, words_count, \
    words_count2


@pytest.mark.parametrize("input_brackets, exp_response", [
    ("[]{}()", True),
    ("({[]})", True),
    (")[]{}", False),
    ("([]{}", False)
])
def test_isValid(input_brackets, exp_response):
    assert exp_response == isValid(input_brackets)


@pytest.mark.parametrize("input_number, e_list, lenght", [
    ([1, 2, 3], [1, 2, 4], 3),
    ([9, 5, 9], [9, 6, 0], 3),
    ([9, 9, 9], [1, 0, 0, 0], 4)
])
def test_add_one(input_number, e_list, lenght):
    assert add_one(input_number) == e_list
    assert len(add_one(input_number)) == lenght


@pytest.mark.parametrize("nums, nums_zero", [
    ([1, 2, 0, 3], [1, 2, 3, 0]),
    ([0, 0, 0, 1, 2, 3], [1, 2, 3, 0, 0, 0]),
    ([0, 1, 2, 0, 3], [1, 2, 3, 0, 0])
]
                         )
def test_zero_to_end(nums: list[int], nums_zero: list[int]):
    assert zero_to_end(nums) == nums_zero


@pytest.mark.parametrize("nums1, nums2, nums_sorted", [
    ([1, 2, 3], [2, 3, 4, 5], [1, 2, 2, 3, 3, 4, 5]),
    ([0, 0, 1, 2, 3], [4, 5, 6], [0, 0, 1, 2, 3, 4, 5, 6]),
    ([0, 1, 2, 3], [1, 2, 3, ], [0, 1, 1, 2, 2, 3, 3])
]
                         )
def test_sorted_nums(nums1: list[int], nums2: list[int], nums_sorted: list[int]):
    assert sorted_nums(nums1, nums2) == nums_sorted


@pytest.mark.parametrize("s, reversed_s", [
    ("world", "dlrow"),
    ("ABC", "CBA")
])
def test_reverse_word(s: str, reversed_s: str):
    assert reversed_s == reverse_word(s)


@pytest.mark.parametrize("s, quantity", [
    ("world", 1),
    ("AA BB CC", 3)
])
def test_words_count(s: str, quantity: int):
    assert words_count(s) == quantity


@pytest.mark.parametrize("s, quantity", [
    (" ", 0),
    ("world", 1),
    ("AA BB CC", 3)
])
def test_words_count2(s: str, quantity: int):
    assert words_count2(s) == quantity
