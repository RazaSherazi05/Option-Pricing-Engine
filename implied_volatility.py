import math

def black_scholes_call(S, K, r, T, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))

    return S * N(d1) - K * math.exp(-r * T) * N(d2)


def implied_volatility(S, K, r, T, market_price, tol=1e-5):
    sigma = 0.2  # initial guess

    for i in range(100):
        price = black_scholes_call(S, K, r, T, sigma)

        diff = price - market_price

        if abs(diff) < tol:
            return sigma

        # Newton-style approximation
        sigma = sigma - diff * 0.1

    return sigma