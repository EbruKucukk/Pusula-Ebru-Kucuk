import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excel dosyasını yüklenir
df = pd.read_excel('C:/Users/kucuk/Desktop/pusula/side_effect_data.xlsx')

# Verinin ilk birkaç satırını inceleme
print(df.head())

# Eksik verilerin sayısını gösterme
print(df.isnull().sum())

# Her bir sütunun veri türlerini görüntüleme
print(df.dtypes)

# Boy ve kilo için boxplot
sns.boxplot(data=df[['Kilo', 'Boy']])
plt.title('Boy ve Kilo Değişkenlerinde Uç Değerler')
plt.show()

# Kilo ve boy dağılımı
df[['Kilo', 'Boy']].hist(bins=20, figsize=(10,5))
plt.show()

# Boy ve kilo arasındaki ilişki
sns.scatterplot(x='Boy', y='Kilo', data=df)
plt.title('Boy ve Kilo İlişkisi')
plt.show()

# Cinsiyet dağılımı
sns.countplot(x='Cinsiyet', data=df)
plt.title('Cinsiyet Dağılımı')
plt.show()

# İlaç dağılımı
df['Ilac_Adi'].value_counts().head(10).plot(kind='bar')
plt.title('En Sık Kullanılan 10 İlaç')
plt.show()