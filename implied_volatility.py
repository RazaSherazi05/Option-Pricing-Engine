import math
from black_scholes import black_scholes_call
from greeks import vega_call


def implied_volatility(S, K, r, T, market_price, tol=1e-8, max_iter=100):
    # No-arbitrage bounds for a European call: max(S - K*e^(-rT), 0) < C < S
    lower = max(S - K * math.exp(-r * T), 0.0)
    if not (lower < market_price < S):
        raise ValueError("Market price outside no-arbitrage bounds")

    sigma = 0.2  # initial guess

    for _ in range(max_iter):
        diff = black_scholes_call(S, K, r, T, sigma) - market_price

        if abs(diff) < tol:
            return sigma

        # Newton-Raphson step: sigma_new = sigma - f(sigma) / f'(sigma), with f' = Vega
        sigma_new = sigma - diff / vega_call(S, K, r, T, sigma)

        if sigma_new <= 1e-6:  # keep sigma positive
            sigma_new = sigma / 2

        sigma = min(sigma_new, 5.0)  # cap to avoid overshooting

    return sigma
