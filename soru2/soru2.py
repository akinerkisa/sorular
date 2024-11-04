import asyncio
import aioping

# Ping atılacak IP adresleri (192.168.1.1 - 192.168.1.254 / 192.168.2.1 - 192.168.2.254)
ip_addresses = [f"192.168.1.{i}" for i in range(1, 255)] + [f"192.168.2.{i}" for i in range(1, 255)]

async def ping_ip(ip):
  try:
      # Ping atma
      response_time = await aioping.ping(ip, timeout=1)
      print(f"{ip} - Ulaşılabilir (Zaman: {response_time:.2f} ms)")
  except TimeoutError:
      print(f"{ip} - Ulaşılamıyor")
      return ip  # Ulaşılamayan IP adresini döndür

async def main():
  while True:
      tasks = [ping_ip(ip) for ip in ip_addresses]
      unreachable_ips = await asyncio.gather(*tasks)
      # Ulaşılamayan IP adreslerini filtrele
      unreachable_ips = [ip for ip in unreachable_ips if ip is not None]
      # Ulaşılamayan IP adreslerini yazdır
      if unreachable_ips:
          print("Ulaşılamayan IP adresleri:")
          for ip in unreachable_ips:
              print(ip)

if __name__ == "__main__":
  asyncio.run(main())