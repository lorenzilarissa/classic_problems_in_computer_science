


# mechanical code of the pi formula

def calculate_pi(n_terms: int) -> float:        # the higher the value of n_terms, the more precise will be the final calculus of pi
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

# result

if __name__ == '__main__':
    print(calculate_pi(1000000))

