# day 111
# arithmetic sequence

def find_term(a1, d, n):
    return a1 + (n - 1) * d


def add_sequence(a1, d, n):
    return (n / 2) * (2 * a1 + (n - 1) * d)
