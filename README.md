# Risk Management Projects (MGMTMFE 409)

**Author:** Vikalp Thukral  
**Program:** UCLA Anderson MFE III – Financial Risk Management  
**Course Instructor:** Prof. Valentin Haddad  
**Term:** Spring 2025

---

## Overview

This repository consolidates eight major projects completed as part of the **Financial Risk Management** course (MGMTMFE 409). Each problem set addresses fundamental risk measurement and management techniques used in modern financial institutions – from **Value-at-Risk (VaR) methodologies** through **credit risk modeling**, **derivatives risk analysis**, and **regulatory compliance frameworks**.

The sequence reflects both theoretical depth and practical application: beginning with portfolio risk decomposition and VaR estimation, progressing through backtesting and model validation during crisis periods, examining exotic derivatives and credit default swaps, and culminating in comprehensive case studies of bank risk management practices and systemic failures.

---

## Repository Structure

| Folder   | Topic / Theme                                           | Core Objective                                                                                                                                                                                                                                    |
| -------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PS1/** | **Portfolio Risk Analytics: VaR and CVaR Decomposition** | Implement Expected Shortfall derivations, Component VaR/CVaR calculations, and risk attribution for multi-asset portfolios. Apply risk decomposition to currency trading desks with correlation analysis.                                         |
| **PS2/** | **VaR Backtesting During the 2008 Financial Crisis**    | Analyze Bank of America's VaR methodology during 2008, implement historical simulation VaR, conduct multi-bank portfolio analysis with Component VaR decomposition, and evaluate model performance under extreme stress.                          |
| **PS3/** | **VaR Methodology Comparison**                          | Compare Historical (moving/expanding window), EWMA (λ=0.995, λ=0.96), GARCH(1,1), and Mixed Approach VaR methodologies. Conduct rigorous backtesting, confidence interval analysis, and propose hybrid real-time risk management framework.       |
| **PS4/** | **Financial Derivatives Risk Analysis**                 | Implement Stulz (1982) closed-form solutions for options on minimum/maximum of two assets. Compute delta-normal, delta-gamma, and Monte Carlo VaR for exotic derivatives with correlation risk and model uncertainty analysis.                   |
| **PS5/** | **BASEL Compliance Analysis: Bank of America**          | Examine post-2008 financial crisis risk management transformation at Bank of America (2009 vs 2023/2024). Analyze Basel III compliance, enterprise risk frameworks, capital adequacy, stress testing, and liquidity management evolution.         |
| **PS6/** | **CDS Hazard Rate Bootstrapping**                       | Bootstrap piecewise constant hazard rates from CDS spreads (3Y, 5Y, 10Y maturities), calculate survival probabilities, price credit-risky bonds, and compare market-implied versus historical default probabilities across credit ratings.        |
| **PS7/** | **LTCM Crisis Analysis & Merton Credit Risk Model**     | Analyze Long-Term Capital Management's 1998 collapse, convergence arbitrage strategies, and risk management failures. Implement Merton structural model for credit risk: estimate asset value/volatility, distance to default, and recovery rate. |
| **PS8/** | **Bank Risk Analysis: BOFA 2009-2024**                  | Comparative analysis of Bank of America's risk management evolution from immediate post-crisis (2009) through current practices (2023-2024). Examine regulatory compliance transformation, risk quantification methodologies, and capital buffers. |

---

## Project Summaries

### PS1 – Portfolio Risk Analytics: VaR and CVaR Decomposition

* Derived **Expected Shortfall (ES)** analytically for normally distributed returns using integration-by-parts.
* Implemented **Component CVaR** and **Delta VaR (DVaR)** for risk attribution across portfolio holdings.
* Conducted sensitivity analysis of finite difference methods for marginal risk calculations.
* Applied framework to **multi-currency trading desk** (USD/EUR and GBP/EUR) with correlation effects.
* **Key Results**: Portfolio VaR (99%) = $10.78M; demonstrated additive decomposition property of CVaR.

### PS2 – VaR Backtesting During the 2008 Financial Crisis

* Analyzed **Bank of America's VaR methodology** from 2008 10-K filing (reported 2 exceptions vs. actual crisis performance).
* Implemented **historical simulation VaR** with expanding window on Bank of America equity returns.
* Conducted **Kupiec proportional failure test**: observed 31 exceptions vs. 2.5 expected (p-value < 0.001).
* Performed **multi-bank portfolio analysis** ($15M across 10 major global banks) with Component VaR decomposition.
* **Key Finding**: Standard VaR models severely underestimated tail risk during 2008 crisis; diversification benefits diminished due to systemic correlation.

### PS3 – VaR Methodology Comparison

* Implemented and backtested four distinct VaR methodologies over 2014-2017 period:
  * **Historical VaR** (moving and expanding windows)
  * **EWMA** (λ=0.995 and λ=0.96)
  * **GARCH(1,1)** with conditional variance modeling
  * **Mixed Approach** (volatility-normalized returns)
* Computed **confidence intervals** using parametric and bootstrap methods.
* **Best Performance**: Mixed Approach achieved 10 violations vs. 9.80 expected (excellent calibration).
* Proposed **hybrid real-time framework** combining GARCH primary measure with EWMA monitoring and Mixed Approach stress regime adjustment.

### PS4 – Financial Derivatives Risk Analysis

* Implemented **Stulz (1982) analytical formulas** for European call options on min(S₁, S₂).
* Computed Greeks via finite differences and bivariate normal distribution functions.
* Calculated VaR using three approaches:
  * **Delta-Normal VaR**: 1.0282 (linear approximation)
  * **Monte Carlo VaR**: 0.9415 (full nonlinearity, 100,000 simulations)
  * **Delta-Gamma VaR**: 1.0302 (quadratic approximation)
* Conducted **model risk analysis**: ±10% volatility error → ±10% VaR error.
* **Key Insight**: For near-ATM options, delta-normal provides reasonable estimates; Monte Carlo captures full tail behavior.

### PS5 – BASEL Compliance Analysis: Bank of America

* Comparative analysis of **Bank of America's risk management framework** across 2009, 2023, and 2024.
* Examined transformation from **Basel II to Basel III** regulatory compliance.
* Analyzed evolution of:
  * Enterprise risk governance structures
  * Credit, market, and operational risk quantification methodologies
  * Capital adequacy ratios and stress testing frameworks
  * Liquidity buffers (LCR and NSFR)
* **Key Finding**: Post-crisis enhancements include strengthened capital ratios (CET1 >11%), comprehensive stress testing (CCAR/DFAST), and robust liquidity risk management.

### PS6 – CDS Hazard Rate Bootstrapping

* Bootstrapped **piecewise constant hazard rates** from CDS spreads using root-finding (scipy.optimize.brentq).
* **Recovered Hazard Rates**: λ₁ = 1.246%, λ₂ = 1.881%, λ₃ = 3.613% for 3Y, 5Y, and 10Y maturities.
* Priced **7-year credit-risky bond** (3% semiannual coupon): **$106.08**.
* Compared **market-implied vs. historical default probabilities** across credit ratings.
* **Key Insight**: Bond-implied hazard rates exceed historical rates for investment-grade credits due to credit risk premiums; relationship reverses for high-yield due to liquidity and recovery assumptions.

### PS7 – LTCM Crisis Analysis & Merton Credit Risk Model

* **Case Study Analysis**:
  * LTCM's convergence arbitrage strategy (on-the-run vs. off-the-run Treasuries, sovereign spreads)
  * Leverage rationale and funding fragility (notional exposure >$1 trillion)
  * 1998 collapse triggered by Russian default and flight to quality
  * Risk management failures: overreliance on historical correlations, inadequate stress testing, ignored liquidity risk
* **Merton Model Implementation**:
  * Solved nonlinear system for asset value and volatility using fsolve
  * **Results**: Asset value = $20.22B, Asset volatility = 8.71%, Distance to default = 0.89, Default probability = 18.67%, Recovery rate = 92.29%

### PS8 – Bank Risk Analysis: BOFA 2009-2024

* In-depth examination of **Bank of America's 2009 annual report** (immediate post-crisis practices).
* Comparative analysis with **2023 and 2024 annual reports** showing risk management evolution.
* Documented transition in:
  * Risk governance and organizational structure
  * Quantitative risk modeling sophistication
  * Regulatory capital requirements and compliance
  * Stress testing and scenario analysis frameworks
* Addressed theoretical risk management questions on VaR properties, forward pricing, and quanto options.

---

## Methodology Highlights

* **Data Sources:** WRDS (CRSP), Yahoo Finance, SEC EDGAR (10-K filings), CDS market data, Kenneth French Data Library.
* **VaR Techniques:** Historical simulation (moving/expanding windows), parametric (delta-normal, delta-gamma), EWMA, GARCH(1,1), Monte Carlo simulation.
* **Credit Risk Models:** CDS bootstrapping, hazard rate estimation, Merton structural model, survival probability calculations.
* **Backtesting:** Kupiec proportional failure test, binomial exception counting, confidence interval estimation (parametric and bootstrap).
* **Derivatives Pricing:** Stulz formulas for multi-asset options, Greeks computation via finite differences, bivariate normal distributions.
* **Risk Decomposition:** Component VaR/CVaR, Delta VaR (DVaR), marginal risk contributions, correlation effects.
* **Codebase:** Python notebooks using NumPy, pandas, scipy, matplotlib, arch (GARCH), statsmodels.

---

## Key Insights and Findings

### VaR Model Performance
* **Historical VaR** severely underestimates tail risk during crisis periods (31 exceptions in 2008 vs. 2.5 expected).
* **GARCH models** capture volatility clustering effectively but can be over-conservative.
* **Mixed Approach** (volatility-normalized returns) provides best calibration in practice.
* **Model risk** from volatility estimation dominates other parameter uncertainties.

### Crisis Period Observations
* Standard VaR models fail under extreme stress; **stress testing** and **scenario analysis** essential complements.
* Bank-reported VaR for diversified trading books outperformed single-asset equity VaR during 2008.
* **Systemic correlation** increases during crises, diminishing traditional diversification benefits.
* Real-time risk management requires **hybrid frameworks** combining multiple methodologies.

### Credit Risk Modeling
* **Market-implied hazard rates** embed credit risk premiums beyond historical default frequencies.
* CDS bootstrapping provides forward-looking default probability estimates.
* **Merton model** effectively links equity market signals to credit risk assessment.
* Recovery rate assumptions critically impact credit-risky bond valuations.

### Derivatives Risk Management
* **Delta-normal VaR** adequate for near-ATM options with moderate volatility.
* **Monte Carlo simulation** necessary for deep OTM/ITM options and complex payoffs.
* **Model risk** from volatility uncertainty dominates for options portfolios.
* Correlation risk significant for multi-asset derivatives.

### Regulatory Evolution
* **Basel III** substantially strengthened capital and liquidity requirements post-crisis.
* **CCAR/DFAST** stress testing now central to bank risk management frameworks.
* Enhanced risk governance, CRO independence, and board-level oversight.
* Greater emphasis on liquidity risk management (LCR, NSFR metrics).

---

## Technical Implementation

### Core Libraries
- **NumPy** – Numerical computations, matrix operations, random number generation
- **pandas** – Data manipulation, time series analysis
- **scipy** – Optimization (root-finding, fsolve), statistical distributions, hypothesis testing
- **matplotlib** – Visualization of VaR time series, confidence intervals, distributions
- **arch** – GARCH model estimation and forecasting
- **statsmodels** – Additional econometric tools
- **yfinance** – Market data retrieval

### Statistical Methods
- Monte Carlo simulation with variance reduction techniques
- Maximum likelihood estimation for GARCH parameters
- Bootstrap resampling for non-parametric confidence intervals
- Kupiec likelihood ratio test for backtesting
- Finite difference approximation for Greeks and marginal risks

---

## Academic Context

**Course**: MGMTMFE 409 – Financial Risk Management  
**Institution**: UCLA Anderson School of Management  
**Instructor**: Professor Valentin Haddad  
**Program**: Master of Financial Engineering  
**Student**: Vikalp Thukral (UID: 406534669)  
**Semester**: Spring 2025  
**Cohort**: Cohort 1, Group 8

---

## References

### Primary Textbooks
* Hull, J.C. (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
* Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk* (3rd ed.). McGraw-Hill.
* McNeil, A.J., Frey, R., & Embrechts, P. (2015). *Quantitative Risk Management: Concepts, Techniques and Tools*. Princeton University Press.

### Key Papers
* Stulz, R.M. (1982). Options on the Minimum or the Maximum of Two Risky Assets. *Journal of Financial Economics*, 10(2), 161-185.
* Kupiec, P. (1995). Techniques for Verifying the Accuracy of Risk Measurement Models. *Journal of Derivatives*, 3(2), 73-84.
* Jorion, P. (2000). Risk Management Lessons from Long-Term Capital Management. *European Financial Management*, 6(3), 277-300.

### Regulatory References
* Basel Committee on Banking Supervision. (2011). *Basel III: A Global Regulatory Framework for More Resilient Banks and Banking Systems*.
* Federal Reserve. *Comprehensive Capital Analysis and Review (CCAR)* guidelines.
* SEC EDGAR Database – Bank 10-K filings (2009, 2023, 2024).

### Data Sources
* WRDS (Wharton Research Data Services) – CRSP equity data
* Yahoo Finance – Historical price and return data
* Kenneth French Data Library – Factor returns and portfolios
* CDS market data – Credit spread quotes

---

## Repository Navigation

Each project folder contains:
* **README.md** – Detailed project documentation
* **Jupyter Notebooks (.ipynb)** – Complete Python implementation
* **Solution Documents (.pdf)** – Analytical derivations and results
* **Assignment Materials (.pdf)** – Original problem statements
* **Data Files (.csv, .pdf)** – Input datasets and reference documents

---

## License

Academic work completed as part of UCLA Anderson MFE program. Educational use only.

---

*This collection demonstrates comprehensive risk management techniques spanning market risk, credit risk, operational risk, and regulatory compliance – essential skills for quantitative risk management roles in financial institutions.*
