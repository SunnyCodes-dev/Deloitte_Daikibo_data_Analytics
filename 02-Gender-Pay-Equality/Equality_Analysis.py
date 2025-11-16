import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("DAIKIBO GENDER PAY EQUALITY ANALYSIS")

# Loading Excel File
df = pd.read_excel(r"C:\Deloitte Project\daikibo_telemetry_data\Equality_Table.xlsx")

print("\nData loaded successfully!")
print(f"Total records: {len(df)}")

# Classifying equality scores based on project requirements
def classify_equality(score):
    if -10 <= score <= 10:
        return "Fair"
    elif (-20 <= score < -10) or (10 < score <= 20):
        return "Unfair"
    else:
        return "Highly Discriminative"

# New column equality class and calling function to filter results based on score
df['Equality_Class'] = df['Equality Score'].apply(classify_equality)

print("EQUALITY CLASSIFICATION")
print(df[['Factory', 'Job Role', 'Equality Score', 'Equality_Class']].head(10))

class_dist = df['Equality_Class'].value_counts()
print("OVERALL DISTRIBUTION")
print(class_dist)
for category, count in class_dist.items():
    print(f"{category}: {count/len(df)*100:.1f}%")

print("ANALYSIS BY FACTORY")

print("\nAverage Equality Score by Factory:")
factory_means = df.groupby('Factory')['Equality Score'].mean().sort_values()
for factory, score in factory_means.items():
    print(f"  {factory}: {score:.2f}")

# Avg, Min, Max, Count for each factory (stats)
print("\nFactory Statistics:")
for factory in df['Factory'].unique():
    factory_data = df[df['Factory'] == factory]['Equality Score']
    print(f"\n{factory}:")
    print(f"  Average: {factory_data.mean():.2f}")
    print(f"  Minimum: {factory_data.min()}")
    print(f"  Maximum: {factory_data.max()}")
    print(f"  Count: {len(factory_data)}")

print("ANALYSIS BY JOB ROLE")

print("\nAverage Equality Score by Job Role:")
role_means = df.groupby('Job Role')['Equality Score'].mean().sort_values()
for role, score in role_means.items():
    print(f"  {role}: {score:.2f}")

# Avg, Count for each unique job role (stats)
print("\nJob Role Statistics:")
for role in df['Job Role'].unique():
    role_data = df[df['Job Role'] == role]['Equality Score']
    print(f"\n{role}:")
    print(f"  Average: {role_data.mean():.2f}")
    print(f"  Count: {len(role_data)}")

print("WORST CASES")
worst = df[df['Equality_Class'] == 'Highly Discriminative'].sort_values('Equality Score')
print(worst[['Factory', 'Job Role', 'Equality Score']])

print("CREATING VISUALIZATIONS")

fig = plt.figure(figsize=(16, 10))

# Subplot 1. Name: Overall Equality Classification (Bar Chart)
ax1 = plt.subplot(2, 3, 1)
class_counts = df['Equality_Class'].value_counts()
colors = ['#4CAF50', '#FF9800', '#F44336']
ax1.bar(class_counts.index, class_counts.values, color=colors, edgecolor='black')
ax1.set_xlabel('Classification', fontweight='bold')
ax1.set_ylabel('Number of Cases', fontweight='bold')
ax1.set_title('Overall Equality Classification', fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Subplot 2. Name: Distribution of Equality Scores (Histogram)
ax2 = plt.subplot(2, 3, 2)
ax2.hist(df['Equality Score'], bins=20, color='#2196F3', edgecolor='black')
ax2.axvline(-20, color='red', linestyle='--', linewidth=2)
ax2.axvline(-10, color='orange', linestyle='--', linewidth=2)
ax2.axvline(10, color='orange', linestyle='--', linewidth=2)
ax2.axvline(0, color='green', linestyle='-', linewidth=2)
ax2.set_xlabel('Equality Score', fontweight='bold')
ax2.set_ylabel('Frequency', fontweight='bold')
ax2.set_title('Distribution of Equality Scores', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Subplot 3. Name: Average Equality Score by Factory (Bar Chart horizontal)
ax3 = plt.subplot(2, 3, 3)
ax3.barh(factory_means.index, factory_means.values, color='orange', edgecolor='black')
ax3.axvline(0, color='green', linestyle='-', linewidth=2)
ax3.set_xlabel('Average Equality Score', fontweight='bold')
ax3.set_ylabel('Factory', fontweight='bold')
ax3.set_title('Average Equality Score by Factory', fontweight='bold')
ax3.grid(axis='x', alpha=0.3)

# Subplot 4. Name: Classification Distribution by Factory (Stacked Bar Chart)
ax4 = plt.subplot(2, 3, 4)
factory_class = df.groupby(['Factory', 'Equality_Class']).size().unstack(fill_value=0)
factory_class = factory_class[['Fair', 'Unfair', 'Highly Discriminative']]
factory_class.plot(kind='barh', stacked=True, ax=ax4, color=['#4CAF50', '#FF9800', '#F44336'], edgecolor='black')
ax4.set_xlabel('Number of Job Roles', fontweight='bold')
ax4.set_ylabel('Factory', fontweight='bold')
ax4.set_title('Classification Distribution by Factory', fontweight='bold')
ax4.grid(axis='x', alpha=0.3)

# Subplot 5. Name: Average Equality Score by Job Role (Bar Chart horizontal)
ax5 = plt.subplot(2, 3, 5)
ax5.barh(role_means.index, role_means.values, color='red', edgecolor='black')
ax5.axvline(0, color='green', linestyle='-', linewidth=2)
ax5.set_xlabel('Average Equality Score', fontweight='bold')
ax5.set_ylabel('Job Role', fontweight='bold')
ax5.set_title('Average Equality Score by Job Role', fontweight='bold')
ax5.grid(axis='x', alpha=0.3)

# Subplot 6. Name: Score Distribution by Factory (Box Plot)
ax6 = plt.subplot(2, 3, 6)
factories = df['Factory'].unique()
data_by_factory = [df[df['Factory'] == factory]['Equality Score'].values for factory in factories]
bp = ax6.boxplot(data_by_factory, labels=factories, patch_artist=True)
for patch in bp['boxes']:
    patch.set_facecolor('#2196F3')
ax6.axhline(0, color='green', linestyle='-', linewidth=2)
ax6.axhline(-10, color='orange', linestyle='--', linewidth=1.5)
ax6.axhline(-20, color='red', linestyle='--', linewidth=1.5)
ax6.set_ylabel('Equality Score', fontweight='bold')
ax6.set_title('Score Distribution by Factory', fontweight='bold')
ax6.grid(axis='y', alpha=0.3)
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Main Title for the Visuals
fig.suptitle('Daikibo Industries - Gender Pay Equality Analysis Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()  # visuals complete

# Calculating best and worst factories and roles
worst_factory = factory_means.idxmin()
best_factory = factory_means.idxmax()
worst_factory_score = factory_means[worst_factory]
best_factory_score = factory_means[best_factory]
worst_role = role_means.idxmin()
worst_role_score = role_means[worst_role]

print("KEY FINDINGS")
print(f"\nFair cases: {class_dist.get('Fair', 0)} ({class_dist.get('Fair', 0)/len(df)*100:.1f}%)")
print(f"Unfair cases: {class_dist.get('Unfair', 0)} ({class_dist.get('Unfair', 0)/len(df)*100:.1f}%)")
print(f"Highly Discriminative: {class_dist.get('Highly Discriminative', 0)} ({class_dist.get('Highly Discriminative', 0)/len(df)*100:.1f}%)")
print(f"\nWorst Factory: {worst_factory} (Score: {worst_factory_score:.1f})")
print(f"Best Factory: {best_factory} (Score: {best_factory_score:.1f})")
print(f"Worst Job Role: {worst_role} (Score: {worst_role_score:.1f})")

# Saving results to a Excel file
output_file = r"C:\Deloitte Project\daikibo_telemetry_data\Equality_Analysis_Results.xlsx"
df.to_excel(output_file, index=False)
print(f"\nResults saved to: {output_file}")
