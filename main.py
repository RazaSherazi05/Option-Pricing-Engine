from black_scholes import black_scholes_call
from monte_carlo import monte_carlo_call
from greeks import delta_call, gamma_call, vega_call
from convergence import monte_carlo_convergence
from implied_volatility import implied_volatility

S, K, r, T, sigma = 100, 100, 0.05, 1, 0.2
market_price = 10.5

print("\n===== OPTION PRICING ENGINE =====\n")
bs = black_scholes_call(S, K, r, T, sigma)
mc, se = monte_carlo_call(S, K, r, T, sigma)

print("Black-Scholes Price:", round(bs, 4))
print("Monte Carlo Price  :", round(mc, 4), "+/-", round(se, 4), "(1 SE)")
print("95% CI             : [", round(mc - 1.96 * se, 4), ",", round(mc + 1.96 * se, 4), "]")

print("\n----- GREEKS -----")
print("Delta:", round(delta_call(S, K, r, T, sigma), 4))
print("Gamma:", round(gamma_call(S, K, r, T, sigma), 6))
print("Vega :", round(vega_call(S, K, r, T, sigma), 4))

print("\n----- IMPLIED VOLATILITY -----")
iv = implied_volatility(S, K, r, T, market_price)
print("Market price:", market_price, "-> IV:", round(iv, 4))

monte_carlo_convergence(S, K, r, T, sigma)
