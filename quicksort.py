def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", quicksort(data))