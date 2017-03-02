from collections import Counter

def number_of_pairs(a, k):
    """
    Given an array of integers a and a number k, return all distinct
    pairs in a such that a[i] = a[j] but i != j. Also return the counts
    of each of these distinct pairs. Runs in O(n) time, even if there
    are O(n^2) non-distinct pairs.
    """
    pairs = []
    # get counts of all distinct numbers in a
    c = Counter(a)
    # to deal with cases where a[i] = a[j] = k / 2, but i != j, recognize
    # that if there are n distinct places where a[i] = k / 2, then there are
    # n choose 2 such cases, since we're picking 2 distinct elements
    dups = c[k//2]
    if k % 2 == 0 and dups > 1:
        pairs.append(((k//2, k//2), dups * (dups - 1) // 2))
        c[k//2] = 0

    # we now create a "flipped" list
    new = [k - x for x in a]

    for x in new:
        if x in c and x < k - x:
            pairs.append(((x, k - x), c[x]))

    return pairs

# a = [5, 8, 3, 2, 9, 4, 1]
# print(number_of_pairs(a, 10))
# a = [5, 8, 5, 2, 9, 5, 1]
# print(number_of_pairs(a, 10))
