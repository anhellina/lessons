"""
Используя рекурсивную функцию вывести в порядке возрастания все простые числа, расположенные между n и m
(включая сами числа n и m), а также количество x этих чисел.
"""
def prime_numbers(n: int, m: int) -> Tuple[list, int]:


    result = []

    my_count = 0
    for element in range(n, m + 1):
        # Check if this element is the prime number
        is_prime = True
        for divider in range(2, element):
            # If we've found any divider the remainder of which is zero
            # So current element is not the prime number
            if divider > 1 and element % divider == 0:
                is_prime = False
                break


        if is_prime:
            result.append(element)
            my_count += 1
            return(result)

    print(prime_numbers(n, m))