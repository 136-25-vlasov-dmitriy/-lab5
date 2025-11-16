import random
import pytest
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def is_palindrome(s):
    s = str(s).lower().replace(' ', '')
    return s == s[::-1]


def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_max(arr):
    if not arr:
        raise ValueError("Массив не может быть пустым")
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def count_vowels(s):
    vowels = 'aeiouаеёиоуыэюя'
    s = str(s).lower()
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def reverse_string(s):
    return str(s)[::-1]


@pytest.fixture
def sample_array():
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def large_array():
    return [random.randint(1, 1000) for _ in range(100)]


def test_bubble_sort_basic():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([5, 5, 5]) == [5, 5, 5]


def test_selection_sort_basic():
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([5, 5, 5]) == [5, 5, 5]


def test_quick_sort_basic():
    assert quick_sort([3, 1, 2]) == [1, 2, 3]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([5, 5, 5]) == [5, 5, 5]


def test_all_sorts_same_result(sample_array):
    bubble_result = bubble_sort(sample_array.copy())
    selection_result = selection_sort(sample_array.copy())
    quick_result = quick_sort(sample_array.copy())
    assert bubble_result == selection_result == quick_result


def test_sort_large_array(large_array):
    assert bubble_sort(large_array.copy()) == sorted(large_array)
    assert selection_sort(large_array.copy()) == sorted(large_array)
    assert quick_sort(large_array.copy()) == sorted(large_array)


def test_negative_numbers():
    test_array = [3, -1, 0, -5, 2]
    expected = [-5, -1, 0, 2, 3]
    assert bubble_sort(test_array.copy()) == expected
    assert selection_sort(test_array.copy()) == expected
    assert quick_sort(test_array.copy()) == expected


def test_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("А роза упала на лапу Азора") == True
    assert is_palindrome(12321) == True


def test_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    with pytest.raises(ValueError):
        calculate_factorial(-1)


def test_find_max():
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([-1, -5, -3]) == -1
    assert find_max([42]) == 42
    with pytest.raises(ValueError):
        find_max([])


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("Абракадабра") == 5
    assert count_vowels("") == 0
    assert count_vowels(12345) == 0


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string(123) == "321"


def test_performance_comparison():
    large_array = [random.randint(1, 10000) for _ in range(300)]

    start = time.time()
    bubble_sort(large_array.copy())
    bubble_time = time.time() - start

    start = time.time()
    selection_sort(large_array.copy())
    selection_time = time.time() - start

    start = time.time()
    quick_sort(large_array.copy())
    quick_time = time.time() - start

    assert quick_time < bubble_time


@pytest.mark.parametrize("input_arr,expected", [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 5, 5], [5, 5, 5]),
    ([9, 8, 7, 6], [6, 7, 8, 9])
])
def test_parametrized_sorting(input_arr, expected):
    assert bubble_sort(input_arr.copy()) == expected
    assert selection_sort(input_arr.copy()) == expected
    assert quick_sort(input_arr.copy()) == expected


def test_array_length_preserved():
    test_array = [random.randint(1, 100) for _ in range(50)]
    assert len(bubble_sort(test_array.copy())) == len(test_array)
    assert len(selection_sort(test_array.copy())) == len(test_array)
    assert len(quick_sort(test_array.copy())) == len(test_array)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])