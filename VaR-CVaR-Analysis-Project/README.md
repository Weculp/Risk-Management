# Portfolio Risk Analytics: VaR and CVaR Decomposition

## Project Overview

This project implements quantitative risk management techniques for portfolio analysis, focusing on Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR) decomposition methodologies. The analysis encompasses both theoretical derivations and practical Monte Carlo simulation-based implementations for multi-asset portfolios and currency trading desks.

## Key Components

### 1. Expected Shortfall Analysis
- Analytical derivation of Expected Shortfall (ES) for normally distributed returns
- Mathematical proof of equivalence between alternative ES definitions
- Integration-by-parts approach for continuous risk measures

### 2. Portfolio Risk Decomposition
- Component VaR and CVaR calculations for multi-asset portfolios
- Delta VaR (DVaR) computation using finite difference methods
- Sensitivity analysis of numerical approximation techniques
- Risk attribution across individual portfolio holdings

### 3. Currency Trading Desk Risk Management
- Multi-currency VaR calculations (USD/EUR and GBP/EUR)
- Correlation effects on portfolio-level risk metrics
- Risk-neutral portfolio optimization
- Hedge ratio derivation for constant VaR maintenance

## Technical Implementation

### Methodologies
- Monte Carlo simulation with 100,000 scenarios
- Regime-switching return distributions (normal and stress periods)
- Finite difference approximation for marginal risk contributions
- Covariance matrix analysis for multi-asset portfolios

### Risk Metrics Computed
- 99% Value-at-Risk (VaR)
- Conditional Value-at-Risk (CVaR/Expected Shortfall)
- Component CVaR by asset
- Delta VaR (marginal VaR contributions)
- Portfolio variance decomposition

## Files Description

### `homework2.pdf`
Problem statement containing three main sections:
1. Theoretical derivation of Expected Shortfall formulas
2. Portfolio VaR decomposition exercises with black-box return generator
3. Currency trading desk risk management case study (Deutsche Bank EUR book)

### `HW2.ipynb`
Jupyter notebook containing complete Python implementation:
- Monte Carlo simulation engine for asset returns
- VaR and CVaR calculation functions
- Risk decomposition algorithms (Component CVaR and DVaR)
- Sensitivity analysis of step size parameters
- Visualization of numerical approximation stability
- Currency desk VaR calculations

### `HW2_final.pdf`
Complete analytical and computational solutions including:
- Mathematical proofs and derivations
- Python code implementation with detailed comments
- Numerical results and risk decomposition tables
- Graphical analysis of step size sensitivity
- Interpretation of risk attribution results

## Key Results

### Portfolio Analysis (3M/4M/3M allocation in assets A/B/C)
- Portfolio VaR (99%): $10,784,608
- Asset C identified as primary risk contributor
- Component CVaR validation confirms additive decomposition
- DVaR analysis shows marginal risk impacts

### Currency Desk Analysis
- USD desk VaR: €1.298M
- GBP desk VaR: €408K
- Combined portfolio VaR: €1.053M (correlation benefit)
- Optimal hedge ratios derived for risk-neutral rebalancing

## Technical Requirements

- Python 3.x
- NumPy for numerical computations
- Matplotlib for visualization
- Jupyter Notebook environment

## Applications

This analysis framework is applicable to:
- Portfolio risk management and attribution
- Capital allocation decisions
- Regulatory capital calculations (Basel III)
- Trading desk risk limits and monitoring
- Risk-adjusted performance measurement

## Methodology Notes

The DVaR sensitivity analysis demonstrates the importance of appropriate step size selection in finite difference methods. Very small perturbations may introduce numerical precision errors, while large perturbations violate local linearity assumptions. Optimal step sizes typically range from 10^-4 to 10^-2 for stable marginal risk estimates.

## References

- Course: MFE 409 Financial Risk Management
- Institution: UCLA Anderson School of Management
- Instructor: Valentin Haddad
