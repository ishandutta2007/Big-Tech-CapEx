import matplotlib.pyplot as plt
import pandas as pd

# Hardcoded historical financial data (Revenue and CapEx in Billions USD)
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'Amazon_Rev': [177.9, 232.9, 280.5, 386.1, 469.8, 514.0, 574.8, 641.5, 716.9, 825.0],
    'Amazon_CapEx': [10.1, 13.4, 16.8, 40.1, 61.1, 63.6, 52.7, 107.6, 128.0, 220.0],
    'Alphabet_Rev': [110.9, 136.8, 161.9, 182.5, 257.6, 282.8, 307.4, 350.2, 402.8, 470.0],
    'Alphabet_CapEx': [13.2, 25.1, 23.5, 22.3, 24.6, 31.5, 32.3, 52.1, 91.0, 200.0],
    'Microsoft_Rev': [96.6, 110.4, 125.8, 143.0, 168.1, 198.3, 211.9, 245.1, 281.7, 331.8],
    'Microsoft_CapEx': [8.1, 11.6, 13.9, 15.4, 20.6, 23.9, 28.1, 44.5, 65.0, 115.9],
    'Meta_Rev': [40.7, 55.8, 70.7, 86.0, 117.9, 116.6, 134.9, 134.9, 201.0, 192.5],
    'Meta_CapEx': [6.7, 13.9, 15.1, 15.7, 19.2, 31.4, 27.3, 38.4, 72.0, 135.0]
}

# Load dictionary directly into a pandas DataFrame
df = pd.DataFrame(data)

# Calculate CapEx to Revenue Ratio as a Percentage (%)
df['Amazon_Ratio'] = (df['Amazon_CapEx'] / df['Amazon_Rev']) * 100
df['Alphabet_Ratio'] = (df['Alphabet_CapEx'] / df['Alphabet_Rev']) * 100
df['Microsoft_Ratio'] = (df['Microsoft_CapEx'] / df['Microsoft_Rev']) * 100
df['Meta_Ratio'] = (df['Meta_CapEx'] / df['Meta_Rev']) * 100

# Configure visual canvas
plt.figure(figsize=(14, 8))

# Define data configurations for iteration and labeling
plot_configs = [
    {'column': 'Amazon_Ratio', 'label': 'Amazon', 'color': '#FF9900', 'marker': 'o'},
    {'column': 'Alphabet_Ratio', 'label': 'Alphabet (Google)', 'color': '#4285F4', 'marker': 's'},
    {'column': 'Microsoft_Ratio', 'label': 'Microsoft', 'color': '#F25022', 'marker': '^'},
    {'column': 'Meta_Ratio', 'label': 'Meta', 'color': '#0668E1', 'marker': 'd'}
]

# Plot lines and dynamically annotate points
for config in plot_configs:
    col = config['column']
    plt.plot(df['Year'], df[col], marker=config['marker'], linewidth=2.5, 
             label=config['label'], color=config['color'])
    
    # Loop over individual line nodes to generate annotations
    for x, y in zip(df['Year'], df[col]):
        plt.annotate(f"{y:.1f}%", 
                     xy=(x, y), 
                     xytext=(0, 8),              # Displaces the text 8 pixels vertically
                     textcoords="offset points", # Anchors tracking logic safely
                     ha='center',                # Center aligns horizontally
                     fontsize=9,                 # Readable micro-font scale
                     fontweight='semibold', 
                     color=config['color'])      # Matches label typography to company colour

# Configure comprehensive chart text, anchors, and grids
plt.title('Big Tech CapEx-to-Revenue Ratio Over Time (2017 - 2026E)', fontsize=15, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('CapEx as % of Total Revenue (%)', fontsize=12, labelpad=10)
plt.xticks(df['Year'])
plt.ylim(0, 80) # Adds padding to the upper ceiling to accommodate the peak Meta labels cleanly
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11, loc='upper left', frameon=True, shadow=True)

# Optimize canvas space bounds and execute window
plt.tight_layout()
plt.show()
