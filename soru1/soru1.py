import asyncio
import paramiko
import sys
from ipaddress import ip_network

SSH_USERNAME = "anonymous"
SSH_PASSWORD = "anonymous"
# SSH bilgileri anonymous login olarak tanımlanmıştır - Değiştirilebilir


# Global değişkenler
verbose_mode = False  # Varsayılan olarak verbose modu kapalı

# Asenkron SSH bağlantısı kurma
async def ssh_connect(ip):
  # Belirtilen IP adresine SSH bağlantısı açar
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  try:
      # Asenkron bağlantı denemesi
      await asyncio.get_event_loop().run_in_executor(
          None,
          client.connect,
          str(ip),
          SSH_USERNAME,
          SSH_PASSWORD,
          5
      )
      print(f"{ip} adresine bağlanıldı")
      # Bağlanılan ip'de komut çalıştırma
      stdin, stdout, stderr = client.exec_command("echo 'SSH bağlantısı başarılı'")
      print(stdout.read().decode())
      return True  # Bağlantı başarılı
  except Exception as e:
      if verbose_mode:
          print(f"{ip} adresine bağlanılamadı: {e}")
      return False  # Bağlantı başarısız
  finally:
      client.close()

# Asenkron verilen IP adresinin taranması
async def scan_network(network):
  # Verilen IP bloğundaki adresleri tarar ve SSH bağlantısı açar
  tasks = []
  for ip in ip_network(network).hosts():
      tasks.append(ssh_connect(ip))
  
  results = await asyncio.gather(*tasks)
  
  # Hiçbir bağlantı kurulamazsa mesaj yazdır
  if not any(results):
      print("Hiçbir bağlantı kurulamadı.")

def main():
  global verbose_mode
  if len(sys.argv) > 1 and sys.argv[1] == '-verbose': # Tüm deneme sonuçlarını yazdırmak için parametre
      verbose_mode = True

  network = "172.29.0.0/16"  # Tarama yapılacak IP bloğu
  asyncio.run(scan_network(network))

if __name__ == "__main__":
  main()