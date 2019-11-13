#include <rembenchmark.hpp>

ACTION rembenchmark::cpu() {
  // Only let us run this
  require_auth(_self);

  int p;

  //eosio::print_f("Mersenne primes:\n");
  for (p = 2; p <= CPU_PRIME_MAX; p += 1) {
      if (is_prime(p) && is_mersenne_prime(p)) {
          // We need to keep an eye on this to make sure it doesn't get optimized out. So far so good.
          //eosio::print_f(" %u", p);
      }
  }
}

BOOL rembenchmark::is_prime(int p) {
    if (p == 2) {
        return TRUE;
    } else if (p <= 1 || p % 2 == 0) {
        return FALSE;
    }

    BOOL prime = TRUE;
    const int to = sqrt(p);
    int i;
    for (i = 3; i <= to; i += 2) {
        if (!((prime = BOOL(p)) % i)) break;
    }
    return prime;
}

BOOL rembenchmark::is_mersenne_prime(int p) {
    if (p == 2) return TRUE;

    const long long unsigned m_p = (1LLU << p) - 1;
    long long unsigned s = 4;
    int i;
    for (i = 3; i <= p; i++) {
        s = (s * s - 2) % m_p;
    }
    return BOOL(s == 0);
}

EOSIO_DISPATCH(rembenchmark, (cpu))
