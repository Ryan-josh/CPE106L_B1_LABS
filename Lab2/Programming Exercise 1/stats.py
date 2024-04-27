# stats.py

def median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[length // 2]


def mode(numbers):
    from collections import Counter

    counter = Counter(numbers)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]


def mean(numbers):
    return sum(numbers) / len(numbers)
