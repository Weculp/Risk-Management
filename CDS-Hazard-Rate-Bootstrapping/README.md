# MFE 409 Credit Risk Analysis - Problem Set 7

## Overview

This repository contains the completed assignment for Problem Set 7 of MFE 409: Financial Risk Management, focusing on Credit Default Swap (CDS) curve bootstrapping, hazard rate estimation, and credit-risky bond pricing.

## Course Information

- **Course**: MFE 409: Financial Risk Management
- **Instructor**: Professor Valentin Haddad
- **Assignment**: Problem Set 7
- **Due Date**: May 26, 2025

## Files

### Assignment Materials

- **homework7.pdf**: Original problem statement provided by the instructor. Contains three main sections:
  - Question 1: Bootstrapping a CDS curve and pricing a 7-year bond
  - Question 2: Analysis of historical vs bond-implied hazard rates
  - Question 3 (Optional): Dynamic credit model using rating transition matrices

### Implementation

- **HW7.ipynb**: Jupyter notebook containing Python implementation of:
  - Piecewise constant hazard rate bootstrapping from CDS spreads (3, 5, and 10-year maturities)
  - Survival probability calculations using recovered hazard rates
  - Credit-risky bond pricing for a 7-year bond with 3% semiannual coupon
  - Uses scipy.optimize.brentq for root-finding and numpy for numerical computations

### Solution Documents

- **RiskHw7_without_optional.pdf**: Complete solution document including:
  - Detailed mathematical derivation and explanation of CDS bootstrapping methodology
  - Step-by-step code explanation with embedded Python code figures
  - Bootstrapped hazard rates: λ₁ = 1.25%, λ₂ = 1.88%, λ₃ = 3.61%
  - 7-year bond price calculation: $106.08
  - Comparative analysis of historical vs bond-implied hazard rates across credit ratings
  - Discussion of risk-neutral vs real-world measures and credit risk premiums

## Assignment Scope

The assignment explores quantitative credit risk modeling techniques used in financial risk management:

- CDS spread bootstrapping to extract implied default intensities
- Piecewise constant hazard rate modeling
- Survival probability functions and credit-risky cash flow valuation
- Recovery rate assumptions in credit derivative pricing
- Comparison of market-implied vs historical default probabilities
- Understanding risk premiums embedded in credit spreads

## Key Results

- **Hazard Rates**: λ₁ = 1.246%, λ₂ = 1.881%, λ₃ = 3.613%
- **7-Year Bond Price**: $106.08 (face value $100, 3% annual coupon paid semiannually)
- **Key Finding**: Bond-implied hazard rates exceed historical rates for investment-grade credits due to credit risk premiums, while the relationship reverses for high-yield credits due to liquidity and recovery assumptions

## Technical Details

- **Programming Language**: Python 3.12
- **Key Libraries**: numpy, scipy.optimize
- **Methodology**: Sequential bootstrapping with root-finding, survival probability weighting
- **Assumptions**: 60% recovery rate, 0% risk-free rate, semiannual payment frequency

## Author

Vikalp Thukral (UID: 406534669)  
Cohort 1, Group 8
