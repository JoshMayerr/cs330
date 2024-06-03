def unique_nums_in_seq(a, b, m):
    pairs = set()  # a set to store pairs in the sequence
    pairs.add((a, b))

    unique_terms = set()  # initial set to save uniuq nums
    # add a and b to the set
    unique_terms.add(a)
    unique_terms.add(b)

    one, two = a, b
    while True:
        next_num = (one + two) % m
        if (two, next_num) in pairs:  # if seq repeats, stop
            break

        unique_terms.add(next_num)
        pairs.add((two, next_num))
        one, two = two, next_num  # move on to the next numbers

    return len(unique_terms)


A, B, M = map(int, input().split())
print(unique_nums_in_seq(A, B, M))
