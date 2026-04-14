python
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
annual_data = pd.read_csv('Annual_Trading_Summary_by_Investor_Type_2026.csv')
monthly_data = pd.read_csv('Monthly_Trading_Summaries_by_Sector_2026.csv')

# Clean and preprocess the data
annual_data['Buy Value (AED)'] = annual_data['Buy Value (AED)'].str.replace(',', '').astype(float)
annual_data['Sell Value (AED)'] = annual_data['Sell Value (AED)'].str.replace(',', '').astype(float)

monthly_data['Buy Value (AED)'] = monthly_data['Buy Value (AED)'].str.replace(',', '').astype(float)
monthly_data['Sell Value (AED)'] = monthly_data['Sell Value (AED)'].str.replace(',', '').astype(float)

# Example Analysis: Annual Buy vs Sell Value
plt.figure(figsize=(10, 6))
plt.bar(annual_data['Investor Type'], annual_data['Buy Value (AED)'], label='Buy Value', alpha=0.7)
plt.bar(annual_data['Investor Type'], annual_data['Sell Value (AED)'], label='Sell Value', alpha=0.7)
plt.xlabel('Investor Type')
plt.ylabel('Value (AED)')
plt.title('Annual Buy vs Sell Value by Investor Type (2026)')
plt.legend()
plt.show()

# Example Analysis: Monthly Buy Value by Sector
monthly_data_grouped = monthly_data.groupby('Sector')['Buy Value (AED)'].sum()
monthly_data_grouped.plot(kind='bar', figsize=(10, 6), title='Total Buy Value by Sector (2026)', color='green')
plt.xlabel('Sector')
plt.ylabel('Total Buy Value (AED)')
plt.show()
