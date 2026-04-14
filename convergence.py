import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes_call

def monte_carlo_convergence(S, K, r, T, sigma):
    np.random.seed(42)

    simulations = []
    prices = []

    Z = np.random.standard_normal(5000)

    bs_price = black_scholes_call(S, K, r, T, sigma)

    for i in range(100, 5000, 100):
        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z[:i])
        payoff = np.maximum(ST - K, 0)
        price = np.exp(-r * T) * np.mean(payoff)

        simulations.append(i)
        prices.append(price)

    plt.plot(simulations, prices, label="Monte Carlo")
    plt.axhline(bs_price, color="red", linestyle="--", label="Black-Scholes")

    plt.title("Monte Carlo Convergence vs Black-Scholes")
    plt.xlabel("Simulations")
    plt.ylabel("Option Price")
    plt.legend()
    plt.show()