# VaR Backtesting During the 2008 Financial Crisis

## Project Overview

This project analyzes the performance and limitations of Value-at-Risk (VaR) models during the 2008 financial crisis through empirical backtesting and portfolio risk decomposition. The analysis examines major global banks' VaR methodologies, compares theoretical models with actual crisis performance, and evaluates systematic risk across the banking sector.

## Objectives

1. Analyze Bank of America's VaR methodology and risk management practices during 2008
2. Implement historical simulation VaR and conduct rigorous backtesting
3. Perform multi-bank portfolio analysis with risk attribution
4. Evaluate VaR model performance under extreme market stress
5. Apply theoretical concepts to real-world risk management challenges

## Key Components

### 1. Bank VaR Methodology Analysis

Analysis of Bank of America's 2008 10-K filing with focus on:
- VaR computation techniques and data sources
- Time horizons and confidence levels
- Data weighting methodologies
- Reported VaR exceptions during the crisis
- Post-crisis methodology enhancements

Key Findings:
- Bank of America reported 2 VaR exceptions in 2008 for their trading book
- Methodology enhancements included increased data update frequency and enhanced stress testing
- Acknowledged limitations of VaR during extreme market conditions

### 2. Historical Simulation and Backtesting

Implementation Details:
- 99% confidence level, 1-day horizon
- Historical simulation using expanding window (2006-2008)
- Daily VaR calculation for Bank of America stock returns
- Kupiec proportional failure test for model validation

Results:
- 31 VaR exceptions observed (vs. 2.5 expected)
- P-value < 0.001 indicating severe model miscalibration
- Demonstrates inadequacy of historical VaR during crisis periods

### 3. Multi-Bank Portfolio Analysis

Portfolio Composition:
- $1M positions in odd-numbered banks (Goldman Sachs, JP Morgan, Barclays, Deutsche Bank, BNP Paribas)
- $2M positions in even-numbered banks (UBS, Citigroup, Morgan Stanley, Bank of America, Credit Suisse)
- Total portfolio: $15M

Risk Metrics Computed:
- Portfolio VaR using historical simulation
- Component VaR (CVaR) by institution
- Delta VaR (DVaR) for marginal risk contributions
- Risk attribution across the banking sector

### 4. Theoretical Risk Analysis

Short Questions Addressed:
1. Pigeonhole principle application to VaR exception clustering
2. VaR scaling across time horizons and confidence levels
3. Statistical tests for VaR exception bunching
4. Event-driven VaR estimation (FOMC announcement analysis)

## Technical Implementation

### Methodologies
- Historical simulation with expanding window
- Log-returns calculation for risk measurement
- Kupiec likelihood ratio test for backtesting
- Finite difference approximation for marginal VaR
- Component VaR decomposition using conditional expectations

### Statistical Tests
- Kupiec proportional failure test
- Binomial exception counting
- Bunching analysis for temporal clustering

## Files Description

### `homework3.pdf`
Problem statement containing:
1. Bank-specific VaR methodology analysis assignments
2. Individual bank backtesting requirements
3. Multi-bank portfolio analysis specifications
4. Theoretical short questions on VaR properties

### `Bank_of_America_Corporation_Form_10-K.pdf`
Official SEC filing containing:
- Market risk management disclosures
- VaR methodology documentation
- 2008 trading performance metrics
- Risk management framework descriptions

### `HW3.ipynb`
Primary analysis notebook containing:
- Bank of America VaR methodology summary
- Historical VaR implementation and backtesting
- Portfolio risk decomposition analysis
- Visualization of VaR exceptions and performance
- Statistical test implementations

### `PS3.ipynb`
Supplementary analysis notebook with additional calculations and validation

### `Rsk_Hw3_Q2_2.pdf`
Analytical solutions to theoretical questions including:
- VaR scaling formulas
- Time horizon adjustments
- Confidence level conversions

### `CS.csv` and `CS2.csv`
Historical price data for Credit Suisse and other banks (2006-2008)

## Key Results and Insights

### Model Performance
- Historical VaR severely underestimated crisis risk
- Single-asset equity VaR: 31 exceptions in 2008
- Bank of America trading book VaR: 2 exceptions in 2008
- Scope and diversification critically impact VaR performance

### Crisis Period Observations
- Standard VaR models failed during extreme volatility
- Banks supplemented VaR with stress testing
- Data recency weighting became more critical
- Desk-level risk limits proved essential

### Portfolio Risk Attribution
- Systemic risk dominated idiosyncratic risk during crisis
- High correlation across banking sector
- Traditional diversification benefits diminished
- Component VaR revealed concentration risks

## Practical Applications

This analysis demonstrates:
- Limitations of historical VaR in stressed markets
- Importance of backtesting for model validation
- Need for complementary risk measures (stress testing, scenario analysis)
- Value of risk decomposition for portfolio management
- Critical evaluation of risk model assumptions

## Risk Management Implications

1. VaR should not be used in isolation during stressed periods
2. Regular backtesting and model validation are essential
3. Stress testing provides critical complementary information
4. Data recency and weighting schemes require dynamic adjustment
5. Portfolio-level vs. asset-level risk measurement yields different insights

## Technical Requirements

- Python 3.x
- pandas for data manipulation
- NumPy for numerical computations
- yfinance for market data retrieval
- Matplotlib for visualization
- scipy for statistical testing

## Academic Context

- Course: MFE 409 Financial Risk Management
- Institution: UCLA Anderson School of Management
- Instructor: Valentin Haddad
- Focus: Empirical validation of risk models during financial crises

## References

- Bank of America Corporation 2008 Form 10-K
- Basel Committee on Banking Supervision guidelines
- Kupiec, P. (1995). "Techniques for Verifying the Accuracy of Risk Measurement Models"
- Historical market data from Yahoo Finance (2006-2008)
