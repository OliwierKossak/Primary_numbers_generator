# Primary number generator
## The goal of the program is optimization of execution time of algorithm that generate primary numbers.
### Operation of the basic algorithm:
1. Takes a range which will be search for primary numbers.
2. Iterate for 1 to the upper range of the number.
3. For each iterated number, check the number of divisors for range (1, iterated_number+1)
4. If divisors number is higher than 2 stop iterate for current number and check next number
5. If divisors number is equal to 2 number is primary number, add number to list.

### Analize of primary numbers.
After analizations of primary numbers I realized that difference between consecutive numbers is always even number (exceptions is 2 and 3 difference is 1).
This avoids checking each subsequent number. instead, starting from 3,program  can check every other number. This saves valuable resources.

### Chart of occurrences for differences between subsequent numbers for range(20000):
![image](https://github.com/OliwierKossak/Primary_numbers_generator/assets/138603416/78f7aec9-102f-4d87-820d-63f474655ae8)

### My algorithm.
My improvement is simple. the algorithm adds the number 2 to the list of prime numbers. Then the loop starts iterating from the number 3 and checks every second value for prime numbers.

### Chart presents of time execution for basic and my algorithm range(20000)::
![image](https://github.com/OliwierKossak/Primary_numbers_generator/assets/138603416/7ef4edc6-8a73-4fbd-9938-dc95fc3d8744)

Execution time shortened by approximately 16%.
