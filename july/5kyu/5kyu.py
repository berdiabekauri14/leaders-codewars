def luck_check(st):
    numbers = [i + 1 for i in range(st)]
    for step in range(2, st // 2):
        count = 0
        for i in range(len(numbers)):
            if numbers[i] != 0:
                count += 1
                if count % step == 0:
                    numbers[i] = 0
    lucky_numbers = [num for num in range if num != 0]
    
    return lucky_numbers