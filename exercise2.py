def smallMult(num1, num2):
    list1 = [];
    list2 = [];

    for i in range(1, 50):
        res1 = num1 * i;
        res2 = num2 * i;
        list1.append(res1);
        list2.append(res2);

    numbers = set(list1) & set(list2);
    min_number = min(numbers);
    return min_number

print(smallMult(48, 64));
print(smallMult(12, 15));