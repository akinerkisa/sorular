# Soru
1- Eş zamanlı 172.29.0.1/16 networkü tarayan ve burda bulduğu IP adreslerine aynı
şekilde eş zamanlı SSH connection açan basit bir proje oluşturubilir misin?

# Kurulum
<p><code>git clone https://github.com/akinerkisa/sorular/</code></p>
<p><code>cd sorular/soru1</code></p>
<p><code>pip install -r requirements.txt</code></p>

# Kullanım
Kurulan bağlantıları görmek için
<p><code>python soru1.py</code></p>

Tüm denemeleri görmek için
<p><code>python soru1.py -verbose</code></p>

# Olası Çıktılar
## Başarılı Bağlantılar
Eğer bazı IP adreslerine başarılı bağlantılar kurulursa, bu IP adresleri için "{ip} adresine bağlanıldı" mesajı yazdırılacaktır. Ayrıca, bağlantı kurulduğunda çalıştırılan komutun çıktısı da gösterilecektir.
### Örnek Çıktı:
<p>172.29.0.2 adresine bağlanıldı</p>
<p></p>SSH bağlantısı başarılı</p>
<p>172.29.0.3 adresine bağlanıldı</p>
<p>SSH bağlantısı başarılı</p>

## Bağlantı Kurulamayan IP Adresleri
Eğer belirli IP adreslerine bağlantı kurulamazsa, bu durum verbose modunda çalıştırıldığında hata mesajlarıyla gösterilecektir. Eğer verbose modu kapalıysa, yalnızca "Hiçbir bağlantı kurulamadı." mesajı yazdırılır.
### Örnek Çıktı (verbose modda):
<p>172.29.0.1 adresine bağlanılamadı: [Errno 111] Connection refused</p>
<p></p>172.29.0.4 adresine bağlanılamadı: [Errno 110] Connection timed out</p>

### Örnek Çıktı (verbose mod kapalı):
Hiçbir bağlantı kurulamadı.

## Aynı Anda Açılan Bağlantılar
Eğer uygulama belirli bir sayıda bağlantıyı aynı anda açıyorsa, bu bağlantıların durumu da konsola yazdırılacaktır ve bu bağlantılardan bazıları başarılı, bazıları ise başarısız olabilir.
### Olası Çıktı (verbose modda):
<p>172.29.0.1 adresine bağlanılamadı: [Errno 111] Connection refused</p>
<p>172.29.0.2 adresine bağlanıldı</p>
<p>SSH bağlantısı başarılı</p>
<p>172.29.0.3 adresine bağlanıldı</p>
<p>SSH bağlantısı başarılı</p>
<p>172.29.0.4 adresine bağlanılamadı: [Errno 110] Connection timed out</p>
<p>172.29.0.5 adresine bağlanılamadı: [Errno 111] Connection refused</p>

### Olası Çıktı (verbose mod kapalı):
<p>172.29.0.2 adresine bağlanıldı</p>
<p>SSH bağlantısı başarılı</p>
<p>172.29.0.3 adresine bağlanıldı</p>
<p>SSH bağlantısı başarılı</p>
<p>Hiçbir bağlantı kurulamadı.</p>


