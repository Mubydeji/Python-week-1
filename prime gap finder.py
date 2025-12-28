# ----------------------------------
# Prime Gap Finder (Loop Practice)
# ----------------------------------

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Generate primes up to 10,000
primes = []

for num in range(2, 10001):
    if is_prime(num):
        primes.append(num)


# Find consecutive prime gaps >= 20
prime_gaps = []

for i in range(len(primes) - 1):
    p1 = primes[i]
    p2 = primes[i + 1]
    gap = p2 - p1

    if gap >= 20:
        prime_gaps.append((p1, p2, gap))


# Save results to file
with open("prime_gaps_20_plus.txt", "w") as f:
    f.write("Consecutive Prime Gaps ≥ 20 (≤ 10,000)\n")
    f.write("Prime1\tPrime2\tGap\n")

    for p1, p2, gap in prime_gaps:
        f.write(f"{p1}\t{p2}\t{gap}\n")


# Summary output
print(f"Total prime gap pairs found: {len(prime_gaps)}")
print("Results saved to prime_gaps_20_plus.txt")
