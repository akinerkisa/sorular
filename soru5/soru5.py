import paramiko
from concurrent.futures import ThreadPoolExecutor


# SSH bilgileri
username = "anonymous"
password = "anonymous"

# Uzak sunucuların IP adresleri
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Çalıştırılacak komut
command = "uname -a"


class RemoteSSH:
  def __init__(self, username, password):
      self.username = username
      self.password = password

  def execute_command(self, host, command):
      try:
          # SSH istemcisi oluştur
          client = paramiko.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
          client.connect(host, username=self.username, password=self.password)

          # Komutu çalıştır
          stdin, stdout, stderr = client.exec_command(command)
          output = stdout.read().decode()
          error = stderr.read().decode()

          client.close()

          return {
              'host': host,
              'output': output,
              'error': error
          }
      except Exception as e:
          return {
              'host': host,
              'error': str(e)
          }

  def execute_commands_on_hosts(self, hosts, command):
      results = []
      with ThreadPoolExecutor(max_workers=len(hosts)) as executor:
          futures = {executor.submit(self.execute_command, host, command): host for host in hosts}
          for future in futures:
              result = future.result()
              results.append(result)
      return results

if __name__ == "__main__":
  ssh_client = RemoteSSH(username, password)
  results = ssh_client.execute_commands_on_hosts(hosts, command)

  for result in results:
      print(f"Host: {result['host']}")
      if 'output' in result:
          print(f"Output: {result['output']}")
      if 'error' in result:
          print(f"Error: {result['error']}")