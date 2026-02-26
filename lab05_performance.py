import time
import random

def exponential_counter(n: int) -> None:
    """Sums up all numbers from 1 to 2^n."""
    counter = 1
    for i in range(2**n):
        counter += 1


def generate_random_integers(n: int) -> list[int]:
    """Generates a list of n random integers, with each number
    being between 0 and 1 billion."""

    return [random.randint(0, 1000000000) for _ in range(n)]


def main() -> None:
    pass


# DO NOT MODIFY ANYTHING BELOW THIS LINE

if __name__ == "__main__":
    main()