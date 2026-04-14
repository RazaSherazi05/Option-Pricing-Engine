from black_scholes import black_scholes_call
from monte_carlo import monte_carlo_call
from greeks import delta_call, gamma_call, vega_call
from convergence import monte_carlo_convergence
from implied_volatility import implied_volatility

monte_carlo_convergence(100, 100, 0.05, 1, 0.2)
S, K, r, T, sigma = 100, 100, 0.05, 1, 0.2
market_price = 10.5

iv = implied_volatility(100, 100, 0.05, 1, market_price)
print("\n===== OPTION PRICING ENGINE =====\n")
bs = black_scholes_call(S, K, r, T, sigma)
mc = monte_carlo_call(S, K, r, T, sigma)

print("Black-Scholes Price:", bs)
print("Monte Carlo Price   :", mc)
print("\n----- GREKS -----")
print("Delta:", delta_call(S, K, r, T, sigma))
print("Gamma:", gamma_call(S, K, r, T, sigma))
print("Vega :", vega_call(S, K, r, T, sigma))
print("\n----- IMPLIED VOLATILITY -----")
print("IV:", iv)
