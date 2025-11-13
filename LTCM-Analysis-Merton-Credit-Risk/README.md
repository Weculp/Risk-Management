# MFE 409 Risk Management - Problem Set 8

## Overview

This repository contains the completed assignment for Problem Set 8 of MFE 409: Financial Risk Management, focusing on the Long-Term Capital Management (LTCM) crisis case study and application of the Merton structural model for credit risk assessment.

## Course Information

- **Course**: MFE 409: Financial Risk Management
- **Instructor**: Professor Valentin Haddad
- **Assignment**: Problem Set 8
- **Due Date**: June 2, 2025

## Files

### Assignment Materials

- **homework8.pdf**: Original problem statement provided by the instructor. Contains two main sections:
  - Question 1: LTCM case study analysis (5 essay questions)
  - Question 2: Merton model application for credit risk (distance to default, default probability, recovery rate)

### Case Study Reference

- **ltcm.pdf**: Academic paper "Risk Management Lessons from Long-Term Capital Management" by Philippe Jorion. Comprehensive analysis of LTCM's trading strategies, leverage, collapse in 1998, and risk management failures. Serves as the primary reference document for answering Question 1.

### Implementation

- **Untitled.ipynb**: Jupyter notebook containing Python implementation of:
  - Merton model solver using scipy.optimize.fsolve for simultaneous equations
  - Asset value and asset volatility estimation from equity market data
  - Distance to default (DD) calculation
  - Default probability computation using normal CDF
  - Expected recovery rate estimation using lognormal distribution integration
  - Uses numpy for numerical computations and scipy.stats for statistical functions

### Solution Document

- **HW8Risk.pdf**: Complete solution document including:
  - Critical analysis of LTCM's convergence arbitrage strategy
  - Examination of leverage requirements and funding fragility
  - Timeline and explanation of LTCM's 1998 collapse following Russian default
  - Identification of key risk management failures (liquidity risk, correlation assumptions, tail risk)
  - Proposed risk management framework for similar hedge fund strategies
  - Detailed Merton model implementation with step-by-step Python code
  - Numerical results: Asset value = $20.22B, Asset volatility = 8.71%, DD = 0.89, Default probability = 18.67%, Recovery rate = 92.29%

## Assignment Scope

The assignment explores both historical case analysis and quantitative credit modeling:

- Real-world risk management failure analysis through the LTCM crisis
- Understanding systemic risk and interconnectedness in financial markets
- Convergence trading strategies and associated risks
- Leverage dynamics and liquidity risk management
- Merton's structural approach to credit risk modeling
- Solving nonlinear systems for asset value and volatility inference
- Distance to default as a credit risk metric
- Recovery rate estimation under default scenarios

## Key Insights from LTCM Analysis

- **Trading Strategy**: Convergence arbitrage on yield spreads (on-the-run vs off-the-run Treasuries, sovereign bonds, swap spreads)
- **Leverage Rationale**: Amplify returns from narrow spreads; notional exposure exceeded $1 trillion at peak
- **Collapse Trigger**: Russian default (August 1998) caused flight to quality, widening spreads opposite to LTCM's positions
- **Risk Management Failures**: Overreliance on historical correlations, inadequate stress testing, ignored liquidity risk, concentration in convergence trades, underestimated tail risk
- **Systemic Impact**: Federal Reserve orchestrated private bailout to prevent contagion

## Key Results from Merton Model

- **Estimated Asset Value**: $20.22 billion
- **Estimated Asset Volatility**: 8.71%
- **Distance to Default**: 0.89 standard deviations
- **Default Probability**: 18.67% over 3-year horizon
- **Expected Recovery Rate**: 92.29%

## Technical Details

- **Programming Language**: Python 3.12
- **Key Libraries**: numpy, scipy.optimize, scipy.stats
- **Methodology**: Nonlinear system solving (fsolve), Black-Scholes framework, lognormal distribution integration
- **Input Parameters**: Equity value = $3B, Equity volatility = 50%, Debt face value = $20B, Time to maturity = 3 years, Risk-free rate = 4.5%

## Author

Vikalp Thukral (UID: 406534669)  
Cohort 1, Group 8
