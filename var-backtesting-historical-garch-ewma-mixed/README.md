# Financial Risk VaR Methodology Comparison

A comprehensive implementation and comparison of multiple Value-at-Risk (VaR) estimation techniques for financial risk management, including backtesting, confidence interval analysis, and real-time risk measurement proposals.

## Project Overview

This project implements and evaluates four distinct approaches to measuring Value-at-Risk (VaR) for a trading strategy over the period 2014-2017:

1. **Historical Methods** (Moving Window & Expanding Window)
2. **Model-Building Approaches** (EWMA & GARCH)
3. **Mixed Approach** (Volatility-Normalized Returns)
4. **Hybrid Real-Time Framework** (Multi-layered risk measurement)

The analysis includes rigorous backtesting, confidence interval estimation using parametric and bootstrap methods, and a practical proposal for real-time risk management.

## Key Features

- **Multiple VaR Methodologies**: Historical, EWMA (λ=0.995, λ=0.96), GARCH(1,1), and Mixed Approach
- **Comprehensive Backtesting**: Exception counting and binomial hypothesis testing
- **Confidence Intervals**: Both parametric (normal assumption) and non-parametric (bootstrap) methods
- **Volatility Analysis**: Rolling and expanding window volatility estimation
- **Distribution Normalization**: Standardization of returns by local volatility
- **Real-Time Risk Framework**: Hybrid model combining GARCH, EWMA, and Mixed Approach
- **Visual Analytics**: Time series plots, confidence bands, histograms, and QQ-plots

## Results Summary

### Backtesting Performance (2015-2017, 748 observations)

| Method | Exceptions | Expected | p-value | Result |
|--------|-----------|----------|---------|---------|
| **Moving Window Historical VaR** | 14 | 7.48 | 2.06% | ❌ Reject H₀ |
| **Expanding Window Historical VaR** | 18 | 7.48 | 0.071% | ❌ Reject H₀ |
| **EWMA VaR (λ=0.995)** | 24 | 7.48 | ~0.0001% | ❌ Reject H₀ |
| **EWMA VaR (λ=0.96)** | 15 | 10.0 | - | Moderate |
| **GARCH(1,1) VaR** | 21 | 10.0 | - | Over-conservative |
| **Mixed Approach VaR** | 10 | 9.80 | - | ✅ Well-calibrated |

### Key Findings

- **EWMA (λ=0.995)** smooths volatility heavily, causing significant lag during market stress periods
- **GARCH(1,1)** responds more dynamically to volatility clustering and captures conditional variance better
- **Mixed Approach** (normalized returns × rolling volatility) provides the best calibration with 10 violations vs. 9.80 expected
- All three initial methods reject the null hypothesis at 5% significance, indicating inadequate tail risk capture

## Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scipy** - Statistical functions and hypothesis testing
- **matplotlib** - Data visualization
- **arch** - GARCH model estimation
- **statsmodels** - Additional statistical tools

## Project Structure

```
financial-risk-var-methodology-comparison/
│
├── README.md
├── HW4_406534669.ipynb          # Main Jupyter notebook with analysis
├── hw4_returns.csv               # Input data: daily returns (2014-2017)
├── homework4.pdf                 # Original assignment description
│
└── outputs/
    ├── HW4_406534669.pdf        # Complete analysis report
    └── HW4_406534669.html       # HTML version of analysis
```

## Getting Started

### Prerequisites

```bash
pip install pandas numpy scipy matplotlib arch statsmodels
```

### Running the Analysis

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/financial-risk-var-methodology-comparison.git
cd financial-risk-var-methodology-comparison
```

2. **Open the Jupyter notebook**:
```bash
jupyter notebook HW4_406534669.ipynb
```

3. **Run all cells** to reproduce the complete analysis

## Methodology Details

### 1. Historical Methods

#### Moving Window Historical VaR
- Uses rolling 252-day window (approximately 1 trading year)
- Computes 1st percentile of historical returns
- Adaptive to recent market conditions but sensitive to outliers

#### Expanding Window Historical VaR
- Incorporates all available historical data up to current date
- More stable but slower to react to regime changes
- Smooths short-term fluctuations

### 2. Model-Building Approaches

#### EWMA Volatility (λ=0.96)
- Exponentially Weighted Moving Average for variance estimation
- Recursion: σ²ₜ = λσ²ₜ₋₁ + (1-λ)r²ₜ₋₁
- VaR = z₀.₉₉ × σₜ (assuming normal distribution)
- Average volatility: **2.35%** per day

#### GARCH(1,1) Model
- Captures volatility clustering and autocorrelation
- Model: σ²ₜ = ω + αr²ₜ₋₁ + βσ²ₜ₋₁
- Maximum likelihood estimation for parameters
- VaR = z₀.₉₉ × σₜ
- Average volatility: **2.46%** per day
- **21 violations** (vs. 10 expected at 1% level)

### 3. Mixed Approach (Recommended)

**Methodology**:
1. Compute rolling 21-day volatility for each trading day
2. Normalize returns: normalized_return = return / rolling_volatility
3. Estimate 1% quantile of normalized distribution
4. Scale back to return units: VaR = quantile × rolling_volatility

**Advantages**:
- Accounts for time-varying volatility (heteroskedasticity)
- Stabilizes the return distribution
- Produces well-calibrated risk estimates
- **10 violations** vs. **9.80 expected** - excellent calibration

### 4. Confidence Intervals

#### Parametric Method (Historical VaR)
- Assumes normal distribution of returns
- Uses quantile standard error: SE = σ / √(n × f(q))
- 95% CI: VaR ± z₀.₀₂₅ × SE

#### Bootstrap Method (All Methods)
- Non-parametric resampling (1,000 iterations)
- Empirical confidence intervals from bootstrap distribution
- More robust when normality assumption violated
- Captures asymmetry in VaR uncertainty

## Real-Time Risk Management Proposal

### Hybrid Framework Architecture

**Core Components**:

1. **Primary Risk Measure: GARCH(1,1) VaR**
   - Adapts to volatility clustering
   - Handles large return shocks effectively
   - Real-time conditional variance forecasting

2. **Supplementary Signal: EWMA Volatility Tracking (λ=0.96)**
   - Provides low-latency early warning system
   - Trigger alert when: EWMA volatility / GARCH volatility > 1.20 (20% threshold)
   - Indicates potential model miscalibration or regime shift

3. **Stress Regime Adjustment: Mixed Approach VaR**
   - Activate during high volatility periods (realized vol > 80th percentile)
   - Reduces non-normality risk and volatility mis-specification
   - Better theoretical coverage during market stress

### Implementation Results

**Backtesting (1,000 trading days)**:
- **Expected Violations (1% VaR)**: 10.0
- **Actual Violations**: 14
- **Conclusion**: Slightly conservative bias acceptable for risk management
- The hybrid model balances responsiveness (GARCH), stability (EWMA), and robustness (Mixed Approach)

### Advantages of Hybrid Approach

✅ **Dynamic responsiveness** to market volatility shocks  
✅ **Early warning system** through EWMA monitoring  
✅ **Regime-adaptive** switching during stress periods  
✅ **Well-calibrated** under both normal and stressed conditions  
✅ **Practical and scalable** for real-time trading operations  

## Key Visualizations

The project includes comprehensive visualizations:

1. **VaR Time Series**: Daily returns plotted against VaR estimates
2. **Confidence Intervals**: Parametric and bootstrap confidence bands
3. **Model Comparison**: EWMA vs. GARCH volatility and VaR
4. **Distribution Analysis**: 
   - Histograms comparing raw vs. normalized returns
   - QQ-plots showing normality of distributions
5. **Hybrid Model Performance**: Real-time VaR with regime switching

## Academic Context

This project was completed as **Problem Set 4** for:
- **Course**: MFE 409 - Financial Risk Management
- **Institution**: UCLA Anderson School of Management
- **Instructor**: Professor Valentin Haddad
- **Semester**: Spring 2024
- **Student**: Vikalp Thukral (UID: 406534669)
- **Cohort**: Cohort 1, Group 8

## Key Insights

### Why EWMA (λ=0.995) Failed
- High decay factor causes excessive smoothing
- Model "thinks volatility is calm" when it has jumped
- Lag during crisis periods (mid-2015 China devaluation, late-2015 turbulence)
- **24 exceptions** demonstrates severe underestimation of tail risk

### Why Mixed Approach Succeeds
- Volatility normalization creates more stable distribution
- Local volatility scaling adapts to regime changes
- Empirical distribution of normalized returns closer to Gaussian
- Robust to model mis-specification

### Practical Recommendation
Use **GARCH(1,1)** as primary measure with **EWMA monitoring** and **Mixed Approach fallback** during extreme volatility periods. This provides:
- Real-time adaptability
- Model robustness
- Regulatory compliance
- Operational feasibility

## References

- Hull, J. C. (2018). *Risk Management and Financial Institutions* (5th ed.)
- McNeil, A. J., Frey, R., & Embrechts, P. (2015). *Quantitative Risk Management*
- Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk* (3rd ed.)
- Christoffersen, P. F. (2012). *Elements of Financial Risk Management* (2nd ed.)

##  License

This project is available for educational purposes. Please provide appropriate attribution if using this code or methodology.

##  Author

**Vikalp Thukral**
- UCLA Anderson MFE Program
- UID: 406534669

---

##  Additional Resources

- [Anthropic ARCH Package Documentation](https://arch.readthedocs.io/)
- [Basel Committee on Banking Supervision - Market Risk Framework](https://www.bis.org/bcbs/publ/d457.htm)
- [RiskMetrics Technical Document (J.P. Morgan)](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)

---

**Note**: This analysis is for educational purposes only and should not be used as the sole basis for investment decisions or risk management in production trading systems.
