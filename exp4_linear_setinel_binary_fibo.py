def get():
    n = int(input("\nEnter the number of students: "))
    arr = []

    for i in range(n):
        item = int(input(f"Roll no. of Student {i + 1}: "))
        arr.append(item)
    return arr

def linear_search(lst, x):
    for i in range(len(lst)):
        if x == lst[i]:
            return i
    return -1

def sentinel_search(lst, x):
    n = len(lst)
    i = 0
    while i < n and x != lst[i]:
        i += 1

    if i < n:
        return i
    return -1

def binary_search(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def fibonacci_search(arr, key):
    def fibonacci(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return a

    length = len(arr)
    offset = -1

    while fibonacci(length) > 1:
        i = min(offset + fibonacci(length - 2), length - 1)
        if arr[i] < key:
            length = length - 1
            offset = i
        elif arr[i] > key:
            length = length - 2
        else:
            return i

    if (fibonacci(length - 1) == 0) and (offset < length - 1) and (arr[offset + 1] == key):
        return offset + 1

    return -1

if __name__ == "__main__":
    arr = get()

    while True:
        print("\nSelect a search method: ")
        print("1. Linear Search")
        print("2. Sentinel Search")
        print("3. Binary Search")
        print("4. Fibonacci Search")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            key = int(input("Enter the roll number to search for: "))
            result = linear_search(arr, key)
            if result != -1:
                print(f"Roll number {key} attended the event and is found at position {result+1}.")
            else:
                print(f"Roll number {key} did not attend the event.")

        elif choice == '2':
            key = int(input("Enter the roll number to search for: "))
            result = sentinel_search(arr, key)
            if result != -1:
                print(f"Roll number {key} attended the event and is found at position {result+1}.")
            else:
                print(f"Roll number {key} did not attend the event.")

        elif choice == '3':
            key = int(input("Enter the roll number to search for: "))
            result = binary_search(arr, key)
            if result != -1:
                print(f"Roll number {key} attended the event and is found at position {result+1}.")
            else:
                print(f"Roll number {key} did not attend the event.")

        elif choice == '4':
            key = int(input("Enter the roll number to search for: "))
            result = fibonacci_search(arr, key)
            if result != -1:
                print(f"Roll number {key} attended the event and is found at position {result+1}.")
            else:
                print(f"Roll number {key} did not attend the event.")

        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
