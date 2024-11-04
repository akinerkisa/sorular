# Soru
2- Eş zamanlı ve arka planda 512 adet IP adresine sürekli ping atan ve ulaşılamayan
IP adreslerini listeleyen uygulama yazabilir misin? Not: Uygulama sürekli olarak
çalışacaktır

# Kurulum
<p><code>git clone https://github.com/akinerkisa/sorular/tree/main/soru2</code></p>
<p><code>cd soru2</code></p>
<p><code>pip install -r requirements.txt</code></p>

# Kullanım
<p><code>python soru2.py</code></p>

# Olası Çıktılar
## Başarılı Ping Sonuçları
Eğer bazı IP adreslerine başarılı bağlantılar kurulursa, bu IP adresleri için "{ip} adresine bağlanıldı" mesajı yazdırılacaktır. Ayrıca, bağlantı kurulduğunda çalıştırılan komutun çıktısı da gösterilecektir.
### Örnek Çıktı:
<p>192.168.1.2 - Ulaşılabilir (Zaman: 0.03 ms)</p>
<p>192.168.2.1 - Ulaşılabilir (Zaman: 0.04 ms)</p>

## Ulaşılamayan IP Adresleri
Eğer belirli IP adreslerine ping atılamazsa, bu durum aşağıdaki gibi bir mesajla gösterilecektir.

### Örnek Çıktı 
<p>192.168.1.24 - Ulaşılamıyor</p>
<p>192.168.2.5 - Ulaşılamıyor</p>

## Ulaşılamayan IP Adreslerinin Listesi
Ulaşılamayan IP adresleri, her döngüde ekrana yazdırılacaktır. Eğer hiç ulaşılamayan IP adresi yoksa, bu durum belirtilmeyecektir.
### Örnek Çıktı
<p>Ulaşılamayan IP adresleri:</p>
<p>192.168.1.24</p>
<p>192.168.2.5</p>



