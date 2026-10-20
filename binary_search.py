def interactive_binary_search():
    size = int(input("Enter the size of the list: "))
    target = int(input("Which number do you want to find? "))

    numbers = list(range(size))

    low = 0
    high = len(numbers) - 1
    attempts = 0

    while low <= high:
        attempts += 1
        middle = (low + high) // 2
        guess = numbers[middle]

        if guess == target:
            print(f"\n✅ Found the number {target}.")
            print(f"📍 Position in the list (index): {middle}")
            print(f"🔢 Total attempts: {attempts}")
            return

        if guess > target:
            high = middle - 1
        else:
            low = middle + 1

    print(f"\n❌ The number {target} is not in the list.")
    print(f"🔢 Total attempts: {attempts}")


if __name__ == "__main__":
    interactive_binary_search()
