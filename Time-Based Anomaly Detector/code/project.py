import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r'C:\Pandas\Time-Based Anomaly Detector\data\synthetic_daily_transactions_10k.csv')
values = df['Value'].values

# --- Week 2: Deviation Detection & Tagging ---

# Challenge 3: Calculate differences and anomaly thresholds
window_size = 7
sma_filter = np.ones(window_size) / window_size
smoothed = np.convolve(values, sma_filter, mode='valid')

# Align raw values with smoothed (discard first/last 3 days)
aligned_values = values[window_size//2 : -(window_size//2)]
differences = aligned_values - smoothed

# Anomaly detection rule (mean ± k*std)
k = 2  # Sensitivity parameter
mean_diff = np.mean(differences)
std_diff = np.std(differences)
upper_threshold = mean_diff + k * std_diff
lower_threshold = mean_diff - k * std_diff

# Challenge 4: Tag anomalies using np.where
anomaly_tags = np.empty_like(aligned_values, dtype=object)
anomaly_tags[:] = 'normal'  # Initialize all as normal

anomaly_tags = np.where(
    aligned_values > smoothed + upper_threshold, 
    'spike',
    np.where(
        aligned_values < smoothed + lower_threshold,
        'drop',
        'normal'
    )
)

# --- Week 3: Severity Score + Alerts ---

# Challenge 5: Create severity score
severity_scores = np.abs(differences) / std_diff

# Challenge 6: Alert rules
alert_levels = np.select(
    [severity_scores > 2, 
     severity_scores > 1.5],
    ['High', 'Medium'],
    default='Low'
)

# --- Week 4: Reporting & Visualization ---

# Challenge 7: Export results
results = pd.DataFrame({
    'Date': df['Date'].iloc[window_size//2 : -(window_size//2)],
    'Value': aligned_values,
    'Smoothed': smoothed,
    'Difference': differences,
    'Anomaly': anomaly_tags,
    'Severity': severity_scores,
    'Alert': alert_levels
})

results.to_csv('anomaly_analysis_results.csv', index=False)

# Challenge 8: Visualization
plt.figure(figsize=(14, 8))

# Plot main data
plt.plot(results['Date'], results['Value'], label='Actual', alpha=0.5)
plt.plot(results['Date'], results['Smoothed'], label='7-Day SMA', color='orange')

# Highlight anomalies
spikes = results[results['Anomaly'] == 'spike']
drops = results[results['Anomaly'] == 'drop']

plt.scatter(spikes['Date'], spikes['Value'], color='red', label='Spike')
plt.scatter(drops['Date'], drops['Value'], color='green', label='Drop')

# Formatting
plt.title('Transaction Anomaly Detection\n(Red=Spike, Green=Drop)')
plt.xlabel('Date')
plt.ylabel('Transactions')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()