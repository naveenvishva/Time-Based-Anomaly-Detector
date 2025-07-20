# 📈 Spike & Drop Detection in Daily Transactions Using NumPy Filters

A lightweight, NumPy-powered anomaly detection engine for identifying spikes and drops in daily transaction data — extended with Power BI dashboarding for interactive visualization and exploration.

---

## 🚀 Project Overview

This project detects time-based anomalies in transactional data using statistical smoothing and deviation detection techniques. It flags significant spikes and drops using NumPy filters and generates severity scores and alerts. The final results are exported to Power BI for interactive analysis.

---

## 🔍 Key Features

- 🧠 **NumPy-based Rolling Averages** for efficient time-series smoothing
- ⚡ **Anomaly Detection** using statistical thresholds (mean ± k·std)
- 🎯 **Severity Scoring** for each detected anomaly
- 🚨 **Alert Categorization**: High / Medium / Low
- 📊 **Interactive Power BI Dashboard** for filtering anomalies by severity, type, and time
- 🕒 **Benchmarking** comparing NumPy vs. Pandas performance on 100k+ rows

---

## 📁 Data

- **Source**: Synthetic daily transaction data for ~10,000 dates.
- **Columns**: `Date`, `Value`

---

## 🧪 Methodology

1. **Smoothing**: 7-day rolling mean using `np.convolve` with reflection padding
2. **Deviation Calculation**: Difference between actual and smoothed signal
3. **Anomaly Rules**: Values outside `mean ± 2·std` flagged as spike or drop
4. **Severity Score**: Normalized deviation (`|x - avg| / std`)
5. **Alert Levels**:
   - `High` if severity > 2
   - `Medium` if severity > 1.5
   - `Low` otherwise

---


## 🧪 Benchmarking (NumPy vs Pandas)

```bash
Data Size: 100,000 points
NumPy Runtime: 0.0124s
Pandas Runtime: 0.0531s
→ NumPy is 4.3× faster
Benchmark code available in notebook under benchmark() function.

📤 Output
Final CSV report includes:

Date	Value	Smoothed	Difference	Anomaly	Severity	Alert

Example filename:
anomaly_report_20250720_1210.csv

