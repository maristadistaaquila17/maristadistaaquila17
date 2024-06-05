import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

# Membaca data dari file CSV
data = pd.read_csv('marista.csv')

# 1. Scatter plot: Hubungan antara Harga Satuan dan Jumlah Barang
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Harga Satuan', y='Jumlah', data=data)
plt.title('Scatter Plot: Harga Satuan vs Jumlah Barang')
plt.xlabel('Harga Satuan (IDR)')
plt.ylabel('Jumlah Barang')
plt.grid(True)
plt.show()

# 2. Pie chart: Persentase penjualan per bulan
total_penjualan_per_bulan = data.groupby('Bulan')['Jumlah'].sum()
plt.figure(figsize=(8, 6))
plt.pie(total_penjualan_per_bulan, labels=total_penjualan_per_bulan.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart: Persentase Penjualan per Bulan')
plt.axis('equal')
plt.show()

# 3. Diagram Venn: Hubungan antara penjualan Oli Mesin dan Aki Mobil
oli_mesin = set(data[data['Nama Barang'] == 'Oli Mesin']['Tanggal'])
aki_mobil = set(data[data['Nama Barang'] == 'Aki Mobil']['Tanggal'])

plt.figure(figsize=(8, 6))
venn2([oli_mesin, aki_mobil], ('Oli Mesin', 'Aki Mobil'))
plt.title('Diagram Venn: Hubungan antara penjualan Oli Mesin dan Aki Mobil')
plt.show()

# 4. Bar chart: Penjualan per jenis barang
penjualan_per_barang = data.groupby('Nama Barang')['Jumlah'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=penjualan_per_barang.values, y=penjualan_per_barang.index, palette='viridis')
plt.title('Bar Chart: Penjualan per Jenis Barang')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Nama Barang')
plt.show()
