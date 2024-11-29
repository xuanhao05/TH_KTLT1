print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096)
def primes_below_n(n):
    """Hàm tìm tất cả các số nguyên tố nhỏ hơn n bằng Sàng Eratosthenes."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False  # 0 và 1 không phải số nguyên tố
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return tuple(i for i in range(n) if sieve[i])

P = primes_below_n(1_000_000)

print(f"Tuple P chứa {len(P)} số nguyên tố nhỏ hơn 1 triệu.")

