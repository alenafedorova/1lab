numbers = [2, -93, -2, 8, None , -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = 0
for num in numbers:
    if num is not None:
        total_sum += num

count = len(numbers)

average = total_sum / count
numbers[4] = average

print("Измененный список:", numbers)
