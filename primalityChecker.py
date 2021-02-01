import time
import matplotlib.pyplot as plt


# starting conditions
# assert LowerBound/UpperBound > 3 (2 and 3 are special primes)
def f_assert_value(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, value MUST be Non-Negative Integer.")
            continue

        if value < 4:
            print("Sorry, Integer value MUST be grater than 3.")
            continue
        else:
            break
    return value


LowerBound = f_assert_value("Enter lower range value:   ")
UpperBound = f_assert_value("Enter upper range value:    ")



# use of iterations instead of system time to compute complexity

# step1: create and open composite/prime csv files.
csv_composite = open('composite.csv', 'w')
csv_composite.write('Composite,Complexity\n')
csv_prime = open('prime.csv', 'w')
csv_prime.write('Prime,Complexity\n')

if LowerBound % 2 == 0:  # if LowerBound is even
    # step2: write all even no.s from LowerBound to UpperBound to composite.csv.
    for even in range(LowerBound, UpperBound + 1, 2):
        # composite csv file is still open, so
        # write to composite csv file on newline
        csv_composite.write('{},1\n'.format(even))

    # step3: test only odd no.s for primality - skipping multiples
    for odd in range(LowerBound + 1, UpperBound + 1, 2):
        complexity = 0
        for i in range(3, int(odd ** 0.5) + 1, 2):
            complexity += 1
            if (odd % i) == 0:
                # composite csv file is still open, so
                # write to composite csv file on newline
                csv_composite.write('{},{}\n'.format(odd, complexity))
                break
        else:
            # prime csv file is still open, so
            # write to prime csv file on newline
            complexity += 1
            csv_prime.write('{},{}\n'.format(odd, complexity))


else:  # if LowerBound is odd
    # step2: write all even no.s from LowerBound to UpperBound to composite.csv.
    for even in range(LowerBound + 1, UpperBound + 1, 2):
        # write to composite csv file on newline
        csv_composite.write('{},1\n'.format(even))

    # step3: test only odd no.s for primality - skipping multiples
    for odd in range(LowerBound, UpperBound + 1, 2):
        complexity = 0
        for i in range(3, int(odd ** 0.5) + 1, 2):
            complexity += 1
            if (odd % i) == 0:
                # composite csv file is still open, so
                # write to composite csv file on newline
                csv_composite.write('{},{}\n'.format(odd, complexity))
                break
        else:
            # prime csv file is still open, so
            # write to prime csv file on newline
            complexity += 1
            csv_prime.write('{},{}\n'.format(odd, complexity))


# step4: close opened files
csv_composite.close()
csv_prime.close()
