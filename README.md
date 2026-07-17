# CLT-Housing-Prices-Simulation

## Visualizing the Central Limit Theorem Through Repeated Sampling of Indian Housing Prices

## Overview

This project demonstrates the **Central Limit Theorem (CLT)** through computational experimentation using real-world Indian housing price data. By repeatedly drawing random samples of varying sizes and visualizing the distribution of sample means, this project provides an intuitive understanding of why sample means become more stable and normally distributed as sample size increases.

**Course:** ES111 Applied Statistics  
**Institution:** GIKI
**Semester:** Spring 2026  
**Instructor:** Dr. Tahir Naseem  

## Project Objectives

- Load and clean real-world housing price data
- Implement statistical formulas manually (mean, variance, standard deviation)
- Perform repeated random sampling with replacement (1000 iterations)
- Visualize sampling distributions for different sample sizes (N = 5, 10, 30, 100)
- Create standardized z-value distributions (N = 10, 30, 100)
- Interpret results and connect theory with computation

### Libraries (Only allowed functions used)
| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and cleaning |
| `numpy` | Random sampling (`np.random.choice`) |
| `matplotlib` | Histogram plotting and visualization |
| `math` | Square root calculations |

> **Important:** All statistical calculations (mean, variance, standard deviation, z-values) were implemented **manually** using loops and basic arithmetic, as per project requirements.

## Dataset Description

**Source:** Indian House Prices Dataset  
**Used Column:** `Price` (only)
