# Options Pricing on Two Underlying Assets

Analytical and numerical implementation of European options on the minimum and maximum of two risky assets using Stulz (1982) closed-form solutions. Includes delta-normal, delta-gamma, and Monte Carlo VaR estimation with model risk analysis.

## Project Overview

Implementation of Value-at-Risk methodologies for exotic options written on multiple underlying assets. Demonstrates analytical pricing formulas, Greeks computation, and practical risk management considerations for derivatives with nonlinear payoffs and correlation risk.

**Course**: MFE 409 - Financial Risk Management, UCLA Anderson  
**Topic**: Risk Management for Options on Multiple Assets

## Repository Structure

```
options-pricing-two-assets/
│
├── README.md
├── homework5.pdf                           # Problem statement
├── HW5_VikalpThukral_406534669.pdf        # Complete solution and analysis
├── lecture5_Options_handout.pdf           # Course lecture notes
└── Options-on-the-Minimum-or-Maximum.pdf  # Stulz (1982) reference paper
```

## File Contents

### homework5.pdf
Problem set covering:
- Delta-normal VaR derivation for options on two underlyings
- Stulz formula implementation for European call on min(S₁, S₂)
- VaR calculation using analytical and simulation methods
- Delta-gamma approximation for nonlinear payoffs
- Model risk analysis and practical considerations
- Case study on quantitative risk management in Chinese investment banks

### HW5_VikalpThukral_406534669.pdf
Complete solution including:
- Mathematical derivations for delta-normal VaR
- Python implementation of Stulz pricing formula
- Numerical results with parameter sensitivity
- Comparison of analytical vs. Monte Carlo approaches
- Delta-gamma second-order approximation
- Volatility uncertainty quantification

### lecture5_Options_handout.pdf
Course materials covering:
- Delta, gamma, vega, theta, and rho definitions
- Greeks-based hedging strategies
- VaR computation for options portfolios
- Risk management frameworks for derivatives trading

### Options-on-the-Minimum-or-Maximum.pdf
Stulz (1982) original paper:
- Analytical formulas for options on extrema of two assets
- Bivariate normal distribution applications
- Applications to currency options, compensation plans, secured debt
- Properties and comparative statics

## Problem Formulation

### Option Contract

European call option with payoff at maturity T:

```
C(T) = max(min(S₁(T), S₂(T)) - K, 0)
```

where S₁ and S₂ follow correlated geometric Brownian motion:

```
dS₁/S₁ = μ₁dt + σ₁dW₁
dS₂/S₂ = μ₂dt + σ₂dW₂
corr(dW₁, dW₂) = ρdt
```

### Stulz Pricing Formula

Option price M(S₁, S₂, K, τ) given by:

```
M = S₁·N₂(α₁, β₁, ρ₁) + S₂·N₂(α₂, β₂, ρ₂) - K·e^(-rτ)·N₂(d₁, d₂, ρ)
```

where N₂(·,·,·) is the bivariate cumulative normal distribution with:

```
d₁ = [ln(S₁/K) + (r - σ₁²/2)τ] / (σ₁√τ)
d₂ = [ln(S₂/K) + (r - σ₂²/2)τ] / (σ₂√τ)
α₁ = d₁ + σ₁√τ
α₂ = d₂ + σ₂√τ
σ² = σ₁² + σ₂² - 2ρσ₁σ₂
β₁ = [ln(S₂/S₁) - σ²τ/2] / (σ√τ)
β₂ = [ln(S₁/S₂) - σ²τ/2] / (σ√τ)
ρ₁ = (ρσ₂ - σ₁) / σ
ρ₂ = (ρσ₁ - σ₂) / σ
```

## Implementation Results

### Base Case Parameters

| Parameter | Value | Unit |
|-----------|-------|------|
| S₁ | 99 | Current price asset 1 |
| S₂ | 101 | Current price asset 2 |
| K | 100 | Strike price |
| σ₁ = σ₂ | 1.5% | Daily volatility |
| ρ | 0.35 | Correlation |
| r | 0.02% | Daily risk-free rate |
| T | 126 | Days to maturity |

### Pricing Results

**Option Price**: 3.4173

**Greeks** (via finite differences, ε = 0.01):
- Δ₁ = 0.1916 (sensitivity to S₁)
- Δ₂ = 0.1671 (sensitivity to S₂)
- Γ₁₁, Γ₂₂, Γ₁₂ computed numerically

### VaR Comparison

| Method | 1-Day 99% VaR | Approach |
|--------|--------------|----------|
| Delta-Normal | 1.0282 | Linear approximation |
| Monte Carlo | 0.9415 | 100,000 simulations |
| Delta-Gamma | 1.0302 | Quadratic approximation |

**Key Insight**: For near-ATM options with moderate volatility:
- Delta-normal provides reasonable first-order estimate
- Monte Carlo captures full nonlinearity (lower VaR)
- Delta-gamma offers marginal improvement for short horizons
- Difference ~9% between linear and full simulation

### Model Risk Analysis

Volatility sensitivity (bumping σ by ±30%):

| Volatility Multiplier | Volatility Level | Delta-Normal VaR |
|----------------------|------------------|------------------|
| 0.70 | 1.05% | 0.7202 |
| 0.85 | 1.28% | 0.8740 |
| 1.00 | 1.50% | 1.0282 |
| 1.15 | 1.73% | 1.1830 |
| 1.30 | 1.95% | 1.3377 |

**Conclusion**: ±10% volatility error → ±10% VaR error. Volatility uncertainty is the dominant model risk factor.

## Key Methodologies

### Delta-Normal VaR

First-order Taylor expansion:

```
dM ≈ Δ₁·dS₁ + Δ₂·dS₂

Var(dM) = (Δ₁S₁σ₁)² + (Δ₂S₂σ₂)² + 2ρ·Δ₁Δ₂·S₁S₂·σ₁σ₂

VaR₉₉% = 2.326 × √Var(dM)
```

### Delta-Gamma VaR

Second-order Taylor expansion:

```
dM ≈ Δ₁·dS₁ + Δ₂·dS₂ + ½Γ₁₁(dS₁)² + ½Γ₂₂(dS₂)² + Γ₁₂·dS₁·dS₂

Var(dM) includes quadratic terms:
- Linear variance: (Δ₁S₁σ₁)² + (Δ₂S₂σ₂)² + 2ρ·Δ₁Δ₂·S₁S₂·σ₁σ₂
- Quadratic variance: ½(Γ₁₁(S₁σ₁)²)² + ½(Γ₂₂(S₂σ₂)²)² + (Γ₁₂S₁σ₁S₂σ₂)²

VaR₉₉% = 2.326 × √Var(dM)
```

### Monte Carlo Simulation

Algorithm:
1. Generate correlated standard normals (Z₁, Z₂) using Cholesky decomposition
2. Simulate price paths: S'ᵢ = Sᵢ·exp((r - σᵢ²/2)·dt + σᵢ·√dt·Zᵢ)
3. Reprice option with T-1 days to maturity using Stulz formula
4. Compute loss distribution: Loss = M₀ - M₁
5. VaR₉₉% = 99th percentile of loss distribution

### Greeks Computation

Finite difference approximation (central differences):

```
Δ₁ ≈ [M(S₁+ε, S₂) - M(S₁-ε, S₂)] / (2ε)
Δ₂ ≈ [M(S₁, S₂+ε) - M(S₁, S₂-ε)] / (2ε)

Γ₁₁ ≈ [M(S₁+ε, S₂) - 2M(S₁, S₂) + M(S₁-ε, S₂)] / ε²
Γ₂₂ ≈ [M(S₁, S₂+ε) - 2M(S₁, S₂) + M(S₁, S₂-ε)] / ε²
Γ₁₂ ≈ [M(S₁+ε, S₂+ε) - M(S₁+ε, S₂-ε) - M(S₁-ε, S₂+ε) + M(S₁-ε, S₂-ε)] / (4ε²)
```

## Technical Implementation

### Required Libraries

```python
import numpy as np
import pandas as pd
from scipy.stats import norm, multivariate_normal
```

### Core Functions

**Stulz Formula**:
```python
def price_min_option_stulz(S1, S2, K, r, sigma1, sigma2, rho, T_days):
    # Implementation of bivariate normal CDF approach
    # Returns option price
```

**Delta-Normal VaR**:
```python
def delta_var_min_option(S1, S2, K, r, sigma1, sigma2, rho, T_days, epsilon):
    # Finite difference Greeks computation
    # Variance calculation with correlation
    # Returns VaR at 99% confidence
```

**Monte Carlo VaR**:
```python
def simulate_var_min_option_mc(S1, S2, K, r, sigma1, sigma2, rho, T_days, n_sim):
    # Correlated normal generation
    # Path simulation and repricing
    # Returns VaR from loss distribution
```

## Key Insights

### Advantages of Analytical Approach
- Exact pricing under Black-Scholes assumptions
- Fast computation suitable for real-time risk
- Greeks available via differentiation
- No sampling error

### Advantages of Monte Carlo
- Captures full nonlinearity of payoff
- No Taylor approximation error
- Extensible to path-dependent features
- Provides full loss distribution

### Model Risk Considerations

**Primary Risk: Volatility Misestimation**
- Small volatility errors amplify linearly to VaR errors
- Implied vs. historical volatility choice matters
- Correlation estimation uncertainty significant

**Secondary Risks**:
- Distributional assumptions (normality, no jumps)
- Constant parameters (volatility smile, term structure)
- Model specification (stochastic volatility, regime switching)

### Practical Recommendations

For real-world trading:
1. Use analytical formulas for speed and transparency
2. Validate with Monte Carlo for complex positions
3. Stress test volatility and correlation assumptions
4. Monitor implied vs. realized volatility divergence
5. Consider parameter uncertainty in risk limits

## Applications

### Option Types Priced
- Call on minimum: max(min(S₁, S₂) - K, 0)
- Call on maximum: max(max(S₁, S₂) - K, 0)
- Put on minimum: max(K - min(S₁, S₂), 0)
- Put on maximum: max(K - max(S₁, S₂), 0)

### Real-World Examples
- Currency option bonds (dual-currency bonds)
- Basket options on multiple equities
- Cross-commodity spread options
- Index options with correlation risk
- Compensation plans with performance hurdles

### Parity Relationships

```
Call_max(V, H, K) = Call(V, K) + Call(H, K) - Call_min(V, H, K)
Put_min(V, H, K) = K·e^(-rT) - Min_asset(V, H, 0) + Call_min(V, H, K)
```

## Academic Context

**Course**: MFE 409 - Financial Risk Management  
**Institution**: UCLA Anderson School of Management  
**Instructor**: Professor Valentin Haddad  
**Student**: Vikalp Thukral (UID: 406534669)  
**Semester**: Spring 2025  
**Cohort**: Cohort 1, Group 8

## References

### Primary Source
Stulz, R.M. (1982). Options on the Minimum or the Maximum of Two Risky Assets: Analysis and Applications. *Journal of Financial Economics*, 10(2), 161-185.

### Options Pricing Theory
- Black, F. & Scholes, M. (1973). The Pricing of Options and Corporate Liabilities. *Journal of Political Economy*, 81, 637-659.
- Merton, R.C. (1973). Theory of Rational Option Pricing. *Bell Journal of Economics and Management Science*, 4, 141-183.
- Margrabe, W. (1978). The Value of an Option to Exchange One Asset for Another. *Journal of Finance*, 33, 177-186.

### Risk Management
- Hull, J.C. (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk* (3rd ed.). McGraw-Hill.

## License

Academic work completed as part of UCLA Anderson MFE program. Educational use only.

---

*This analysis demonstrates quantitative risk management techniques for exotic derivatives and should not be used as the sole basis for production trading systems.*
