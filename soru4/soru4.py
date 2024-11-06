import multiprocessing
import sqlite3
import time

# Veritabanı oluşturma fonksiyonu
def create_database():
    conn = sqlite3.connect('soru4.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS process_status (
            process_id INTEGER PRIMARY KEY,
            status TEXT,
            start_time TIMESTAMP,
            end_time TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# İşlem fonksiyonu
def worker(process_id):
    start_time = time.time()
    
    time.sleep(1)
    
    end_time = time.time()
    
    # Veritabanına kaydetme
    conn = sqlite3.connect('process_status.db', timeout=5)  
    cursor = conn.cursor()
    
    try:
        # process_id'nin zaten mevcut olup olmadığını kontrol et
        cursor.execute('SELECT COUNT(*) FROM process_status WHERE process_id = ?', (process_id,))
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO process_status (process_id, status, start_time, end_time)
                VALUES (?, ?, ?, ?)
            ''', (process_id, 'completed', start_time, end_time))
            conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError for process {process_id}: {e}")
    finally:
        conn.close()

# Durumları kontrol etme fonksiyonu
def check_process_status():
    conn = sqlite3.connect('process_status.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM process_status')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    create_database()
    processes = []
    
    # 1000 adet işlemi başlat
    for i in range(1000):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    # Tüm işlemlerin bitmesini bekle
    for p in processes:
        p.join()
    
    # İşlem durumlarını kontrol et
    check_process_status()