# Moneycontrol Mutual Fund API

This is a simple Python Flask API that fetches mutual fund details from Moneycontrol using the `mfperfquery` library.

## Features
- Fetch performance metrics (1Y, 3Y, 5Y CAGR, volatility, drawdowns, etc.)
- Get fund details like AUM, Expense Ratio, Exit Load, Benchmark, etc.
- Returns clean JSON output
- Accepts one or two fund URLs for comparison

## Example API Call

Single fund:
