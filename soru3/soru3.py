import sqlite3
import time
import random

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('soru3.db')
cursor = conn.cursor()

# Tablo oluşturma
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
product TEXT NOT NULL,
quantity INTEGER NOT NULL,
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# 50.000 kullanıcı kaydı ekleme
start_time = time.time()
for i in range(50000):
  cursor.execute('''
  INSERT INTO users (name, email, age) VALUES (?, ?, ?)
  ''', (f'User{i}', f'user{i}@example.com', random.randint(18, 65)))

conn.commit()
print(f'Kullanıcı ekleme süresi: {time.time() - start_time:.2f} saniye')

# Kullanıcı ekleme işlemi sonrası kayıt sayısı kontrolü
cursor.execute('SELECT COUNT(*) FROM users')
user_count = cursor.fetchone()[0]
print(f'Eklenen kullanıcı sayısı (users): {user_count}')

# 50.000 sipariş kaydı ekleme
start_time = time.time()
for i in range(50000):
  cursor.execute('''
  INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)
  ''', (random.randint(1, 50000), f'Product{i}', random.randint(1, 10)))

conn.commit()
print(f'Sipariş ekleme süresi: {time.time() - start_time:.2f} saniye')

# Sipariş ekleme işlemi sonrası kayıt sayısı kontrolü
cursor.execute('SELECT COUNT(*) FROM orders')
order_count = cursor.fetchone()[0]
print(f'Eklenen sipariş sayısı (orders): {order_count}')

# Kullanıcıları güncelleme
start_time = time.time()
cursor.execute('''
UPDATE users SET age = age + 1
''')
conn.commit()
print(f'Kullanıcı güncelleme süresi: {time.time() - start_time:.2f} saniye')

# Kullanıcıları silme
start_time = time.time()
cursor.execute('DELETE FROM users')
conn.commit()
print(f'Kullanıcı silme süresi: {time.time() - start_time:.2f} saniye')

# Siparişleri silme
start_time = time.time()
cursor.execute('DELETE FROM orders')
conn.commit()
print(f'Sipariş silme süresi: {time.time() - start_time:.2f} saniye')

# Veritabanı bağlantısını kapat
conn.close()