import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", randomized_quicksort(data))