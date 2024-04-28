def count_long_subarray(A):
    """
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """
    count = 0
    prev_a = 0
    current_subarray_size = 0
    max_subarray_size = 0

    for a in A:
        print(a)

        if a > prev_a:  # while increasing
            # keep track of length of increasing-subarray
            current_subarray_size += 1
            print("size =", current_subarray_size)
            prev_a = a

            if current_subarray_size > max_subarray_size:
                max_subarray_size = current_subarray_size
                count = 1
                print(
                    "update max_subarray_size =",
                    max_subarray_size,
                    "reset count =",
                    count,
                )
            elif current_subarray_size == max_subarray_size:
                count += 1
                print("increment count =", count)

            continue

        # if not inreasing anymore, end of subarray
        prev_a = a  # the update inside the first if-case won't be executed, so perform the update here
        current_subarray_size = 1  # 1 because current_subarray = [ prev_a ]
        print("reset current_subarray_size=", 1)

    print("COUNT =", count)
    return count


if __name__ == "__main__":
    count = count_long_subarray((1, 3, 4, 2, 7, 5, 6, 9, 8))
