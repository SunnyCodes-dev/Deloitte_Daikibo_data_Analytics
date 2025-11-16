import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data
print("Loading data...")
df = pd.read_json(r"C:\Deloitte Project\daikibo_telemetry_data\daikibo_telemetry_data.json")

# Flatten nested structure
df = pd.json_normalize(df.to_dict(orient="records"))

print(f"✓ Data loaded successfully!")
print(f"Total records: {len(df):,}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}\n")

# Exploratory Data Analysis
print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print(f"\nDataset: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Columns: {df.columns.tolist()}")

# Show factories
print(f"\n--- Factories ({df['location.factory'].nunique()}) ---")
for factory in df['location.factory'].unique():
    print(f"  • {factory}")

# Show device types
print(f"\n--- Device Types ({df['deviceType'].nunique()}) ---")
for device in df['deviceType'].unique():
    print(f"  • {device}")

# Show status distribution
print(f"\n--- Status Distribution ---")
status_counts = df['data.status'].value_counts()
print(status_counts)
print(f"Healthy: {status_counts['healthy']/len(df)*100:.2f}%")
print(f"Unhealthy: {status_counts['unhealthy']/len(df)*100:.2f}%")

# Check data quality
print(f"\n--- Data Quality ---")
missing = df.isnull().sum().sum()
print(f"Missing values: {missing} ✓" if missing == 0 else f"Missing values: {missing} ⚠️")

# Calculate downtime
print("\n" + "=" * 50)
print("DOWNTIME ANALYSIS")
print("=" * 50)

# Create downtime column: 10 minutes for each unhealthy record
df['downtime'] = df['data.status'].apply(lambda x: 10 if x == 'unhealthy' else 0)

# Total downtime across all factories
total_downtime = df['downtime'].sum()
print(f"\nTotal Downtime:")
print(f"  • {total_downtime} minutes")
print(f"  • {total_downtime/60:.2f} hours")
print(f"  • {total_downtime/60/24:.2f} days")

# Downtime per factory
downtime_per_factory = df.groupby('location.factory')['downtime'].sum().sort_values(ascending=False)

print(f"\n--- Downtime per Factory ---")
for factory, downtime in downtime_per_factory.items():
    percentage = (downtime / total_downtime) * 100
    print(f"  • {factory}: {downtime} min ({downtime/60:.1f}h) - {percentage:.1f}%")

# Answer to Question 1
print(f"\n🎯 QUESTION 1: Which factory has most downtime?")
print(f"   Answer: {downtime_per_factory.index[0]}")
print(f"   Downtime: {downtime_per_factory.values[0]} minutes ({downtime_per_factory.values[0]/60:.1f} hours)")

# Analyze worst factory devices
worst_factory = downtime_per_factory.index[0]
print(f"\n--- Analyzing {worst_factory} ---")

# Filter for worst factory only
worst_factory_df = df[df['location.factory'] == worst_factory]

# Calculate downtime per device type
downtime_per_device = worst_factory_df.groupby('deviceType')['downtime'].sum().sort_values(ascending=False)

print(f"\nDowntime per Device Type:")
for device, downtime in downtime_per_device.items():
    if downtime > 0:
        print(f"  • {device}: {downtime} min ({downtime/60:.1f}h)")

# Get only devices with failures
devices_with_failures = downtime_per_device[downtime_per_device > 0]

# Answer to Question 2
print(f"\n🎯 QUESTION 2: Which device broke most in {worst_factory}?")
print(f"   Answer: {devices_with_failures.index[0]}")
print(f"   Downtime: {devices_with_failures.values[0]} minutes ({devices_with_failures.values[0]/60:.1f} hours)")
print(f"   Percentage: {(devices_with_failures.values[0]/downtime_per_factory.values[0])*100:.0f}% of factory downtime")

# Create visualizations
print("GENERATING DASHBOARD")

# Setup: Create figure with 2 charts side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Add main title
fig.suptitle('Daikibo Manufacturing Downtime Analysis - May 2021', 
             fontsize=18, fontweight='bold')

# Chart 1: Factory Downtime (Left)
factories = downtime_per_factory.index.tolist()
downtimes = downtime_per_factory.values.tolist()
colors = ['#c62828', '#e53935', '#ef5350', '#ef9a9a']

ax1.barh(factories, downtimes, color=colors, edgecolor='black')
ax1.set_xlabel('Downtime (minutes)', fontweight='bold')
ax1.set_ylabel('Factory', fontweight='bold')
ax1.set_title('Downtime per Factory', fontweight='bold')
ax1.grid(axis='x', alpha=0.3)

# Add value labels on bars
for i, (factory, downtime) in enumerate(zip(factories, downtimes)):
    ax1.text(downtime + 15, i, f'{downtime} min', va='center', fontweight='bold')

# Chart 2: Device Downtime (Right)
device_names = devices_with_failures.index.tolist()
device_downtimes = devices_with_failures.values.tolist()

ax2.bar(device_names, device_downtimes, color='#c62828', edgecolor='black', width=0.5)
ax2.set_xlabel('Device Type', fontweight='bold')
ax2.set_ylabel('Downtime (minutes)', fontweight='bold')
ax2.set_title(f'Downtime per Device - {worst_factory}', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, (device, downtime) in enumerate(zip(device_names, device_downtimes)):
    ax2.text(i, downtime + 15, f'{int(downtime)} min', ha='center', fontweight='bold')

# Add insight text at bottom
fig.text(0.5, 0.02, 
         f'Analysis: {factories[0]} has highest downtime → {device_names[0]} is the cause',
         ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.show()

print("ANALYSIS COMPLETE")
