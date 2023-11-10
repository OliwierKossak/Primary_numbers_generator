from collections import Counter
import time


class PrimeNumberAlogrithm:

    def __init__(self, range_of_numbers):
        """
        Parameters:
            range_of_numbers (int): Upper bound for finding prime numbers.
        """
        self.range_of_numbers = range_of_numbers

    def create_prime_numbers(self):
        """
        The function that search for prime numbers.

        Returns:
            list: List with prime numbers.
        """
        numbers_upper_range = self.range_of_numbers
        prime_numbers = []
        prime_numbers.append(2)

        for i in range(3, numbers_upper_range, 2):
            number_of_divisors = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    number_of_divisors += 1
                if number_of_divisors > 2:
                    break
            if number_of_divisors == 2:
                prime_numbers.append(i)

        return prime_numbers

    def calculate_difference_between_consecutive_numbers(self, prime_numbers):
        """
        The function that calculate difference between consecutive prime numbers.

        Parameters:
            prime_numbers (list): List with prime numbers.

        Returns:
            list: Differences consecutive prime numbers.
        """
        differences_numbers = []
        amount_of_numbers = len(prime_numbers) - 1
        for i in range(amount_of_numbers):
            number_difference = int(abs(prime_numbers[i] - prime_numbers[i + 1]))
            differences_numbers.append(number_difference)
        return differences_numbers

    def count_differences_beteewen_prime_numbers(self, differences_numbers):
        """
        The function that count occurrences of same differences between  prime numbers.

        Parameters:
            differences_numbers (list): Differences consecutive prime numbers.

        Returns:
            dictionary: Counted number of occurrences of differences.
        """
        count_dict = Counter(differences_numbers)
        sorted_count_dict = dict(sorted(count_dict.items(), key=lambda s: s[1]))
        return sorted_count_dict

    def measure_time(self):
        """
        The function that measure time of algorithm execution.

        Returns:
            float: Time of execution.
        """
        start_time = time.time()
        self.create_prime_numbers()
        end_time = time.time() - start_time
        return end_time
