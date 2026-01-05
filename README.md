# Project-ValueBet

# ValueBet Detection Using Market Odds

## Overview

This project aims to identify **value bets in football betting markets** by comparing odds across multiple bookmakers and detecting significant deviations from the market consensus.

Instead of estimating probabilities using a machine learning model, the core assumption is that **the betting market itself provides a strong implicit estimate of true probabilities**. When many bookmakers offer very similar odds for the same outcome, and a single bookmaker offers a significantly higher odds, this discrepancy is treated as a potential value bet.

The project focuses on:
- Collecting up-to-date football odds from multiple bookmakers
- Structuring the data for analysis using databases retrieved for som API
- Detecting statistical outliers in odds distributions
- Flagging potential value bets close to kickoff or during live betting

---

## Motivation

Manually searching for value bets is time-consuming and error-prone. Odds change quickly, especially close to match start and during live games.

This project automates the process by:
- Continuously monitoring bookmaker odds
- Comparing prices for identical outcomes
- Highlighting cases where one bookmaker deviates strongly from the market

The guiding idea is:
> If 8–10 bookmakers agree on a price range, it is unlikely that they are all wrong simultaneously. A strong deviation by one bookmaker may indicate mispricing.

---

## What Is a Value Bet (in this project)

In this project, a **value bet** is defined as:

- The same football outcome (same match, market, line, and rules)
- Offered by multiple bookmakers
- Where one bookmaker’s odds are significantly higher than the market median

The project **does not**:
- Predict match outcomes
- Train models to estimate win probabilities
- Use historical labels to learn success rates

Instead, it relies on **market efficiency and consensus pricing** as the reference.

---

## Methodology

### 1. Data Collection
- Odds are fetched from football-specific odds APIs
- Data includes match information, market type, outcome, bookmaker, odds, and timestamps
- Data is stored in CSV files or a relational database

### 2. Data Normalization
To ensure valid comparisons, only identical outcomes are compared:
- Same match and kickoff time
- Same market (e.g. 1X2, Over/Under 2.5)
- Same line and betting rules

### 3. Outlier Detection
For each outcome:
- The **median odds** across bookmakers is computed
- Each bookmaker’s odds is compared to the median
- A ratio or implied probability difference is used as a signal

Example:
- Median odds: 2.15
- One bookmaker offers: 3.50
- Ratio to median: 3.50 / 2.15 ≈ 1.63

Such cases are flagged as potential value bets.

### 4. Filtering and Sanity Checks
Optional filters include:
- Minimum number of bookmakers per outcome
- Tight market spread among non-outliers
- Time-based filtering (latest odds only)

---

## Technologies Used

- Python
- NumPy
- CSV-based data pipelines
- Football odds and statistics APIs
