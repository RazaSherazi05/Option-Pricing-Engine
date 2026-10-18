import math
from black_scholes import black_scholes_call
from monte_carlo import monte_carlo_call
from implied_volatility import implied_volatility

S, K, r, T, sigma = 100, 100, 0.05, 1, 0.2


def test_black_scholes_reference_value():
    assert abs(black_scholes_call(S, K, r, T, sigma) - 10.4506) < 1e-4


def test_monte_carlo_within_3_standard_errors():
    mc, se = monte_carlo_call(S, K, r, T, sigma, simulations=100000)
    assert abs(mc - black_scholes_call(S, K, r, T, sigma)) < 3 * se


def test_implied_volatility_round_trip():
    for vol in [0.05, 0.2, 0.5, 1.0]:
        price = black_scholes_call(S, K, r, T, vol)
        assert abs(implied_volatility(S, K, r, T, price) - vol) < 1e-6


def test_put_call_parity():
    call = black_scholes_call(S, K, r, T, sigma)
    put = call - S + K * math.exp(-r * T)
    assert abs(put - 5.5735) < 1e-4


if __name__ == "__main__":
    test_black_scholes_reference_value()
    test_monte_carlo_within_3_standard_errors()
    test_implied_volatility_round_trip()
    test_put_call_parity()
    print("All tests passed")
