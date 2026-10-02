import time
import random

def exponential_counter(n: int) -> None:
    """Sums up all numbers from 1 to 2^n."""
    counter = 1
    for i in range(2**n):
        counter += 1

def test_empty_list_contains_no_duplicates() -> None:
	result = contains_duplicates([])
	assert result == False

def test_full_list_contains_no_duplicates() -> None:
	result = contains_duplicates([1,2,3,4,5])
	assert result == False

def test_contains_front_duplicates() -> None:
	result = contains_duplicates([1,1,3,4,5])
	assert result == True

def test_contains_back_duplicates() -> None:
	result = contains_duplicates([1,2,3,4,4])
	assert result == True

def test_contains_two_duplicates() -> None:
	result = contains_duplicates([1,3,3,5,5])
	assert result == True


def contains_duplicates(l: list[int]) -> bool:
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                return True
    return False


def generate_random_integers(n: int) -> list[int]:
    """Generates a list of n random integers, with each number
    being between 0 and 1 billion."""

    return [random.randint(0, 1000000000) for _ in range(n)]


def main() -> None:
    num = int(input("gimmie a number"))
    start = time.time()
    exponential_counter(num)
    end = time.time()

    print(f"\n{end-start}")



# DO NOT MODIFY ANYTHING BELOW THIS LINE

if __name__ == "__main__":
    main()