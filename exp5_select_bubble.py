def get():
    n = int(input("Enter the number of students: "))
    percentages = []
    print("Enter the percentage of each student:")
    for i in range(n):
        percentage = float(input(f"Student {i + 1}: "))
        percentages.append(percentage)

    return percentages
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



if __name__ == "__main__":
    percentages = get()

    while True:
        print("\nSelect a sorting method:")
        print("1. Selection Sort")
        print("2. Bubble Sort")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            selection_sort(percentages)
            print("Sorted Array : ",percentages)
            print("\nTop five scores after Selection Sort:")
            for score in percentages[-5:]:
                print(score)
        elif choice == '2':
            bubble_sort(percentages)
            print("Sorted Array : ",percentages)
            print("\nTop five scores after Bubble Sort:")
            for score in percentages[-5:]:
                print(score)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
