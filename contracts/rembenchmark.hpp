#include <eosio/eosio.hpp>
//#include <eosiolib/print.hpp>
#include <math.h>
#pragma precision=log10l(ULLONG_MAX)/2
typedef enum { FALSE=0, TRUE=1 } BOOL;

// Max when calculating primes in cpu test
#define CPU_PRIME_MAX 375

using namespace eosio;

CONTRACT rembenchmark : public contract {
  public:
    using contract::contract;

    ACTION cpu();

  private:
    BOOL is_prime(int p);
    BOOL is_mersenne_prime(int p);
};