import math

def d1(S, K, r, T, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S, K, r, T, sigma):
    return d1(S, K, r, T, sigma) - sigma * math.sqrt(T)


# PDF
def pdf(x):
    return math.exp(-0.5 * x**2) / math.sqrt(2 * math.pi)


# CDF
def cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


# DELTA
def delta_call(S, K, r, T, sigma):
    return cdf(d1(S, K, r, T, sigma))


# GAMMA
def gamma_call(S, K, r, T, sigma):
    return pdf(d1(S, K, r, T, sigma)) / (S * sigma * math.sqrt(T))


# VEGA
def vega_call(S, K, r, T, sigma):
    return S * pdf(d1(S, K, r, T, sigma)) * math.sqrt(T)