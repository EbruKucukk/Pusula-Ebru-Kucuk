import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('C:/Users/kucuk/Desktop/pusula/side_effect_data.xlsx')

# Eksik değerlerin kontrolü
print(df.isnull().sum())

# Adım 1: Eksik Değerlerin Ele Alınması
# Kategorik sütunlar
categorical_cols = ['Cinsiyet', 'Il', 'Alerjilerim', 'Kronik Hastaliklarim', 
                    'Baba Kronik Hastaliklari', 'Anne Kronik Hastaliklari', 
                    'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari', 
                    'Kan Grubu']

# Sayısal sütunlar
numerical_cols = ['Kilo', 'Boy']

# Kategorik değişkenler için SimpleImputer (en sık kullanılan değer ile doldur)
cat_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])

# Sayısal değişkenler için KNNImputer
num_imputer = KNNImputer()
df[numerical_cols] = num_imputer.fit_transform(df[numerical_cols])

# Adım 2: Kategorik Değişkenlerin Kodlanması
encoder = OneHotEncoder(drop='first', sparse_output=False)  # sparse_output=False ile yoğun matris
encoded_cat = encoder.fit_transform(df[categorical_cols])
encoded_cat_df = pd.DataFrame(encoded_cat, columns=encoder.get_feature_names_out(categorical_cols))

# Kategorik değişkenleri çıkartıp yeni kodlanmış değişkenleri ekleyin
df = pd.concat([df.drop(columns=categorical_cols), encoded_cat_df], axis=1)

# Adım 3: Sayısal Özelliklerin Normalleştirilmesi
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Temizlenmiş veriyi görüntüleme
print(df.head())

# Gerekirse temizlenmiş veriyi kaydetmek için
# df.to_csv('temizlenmis_veri.csv', index=False)  # Temizlenmiş veriyi kaydetmek için