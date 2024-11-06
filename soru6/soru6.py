import re
import time

def parse_dhcp_message(data):
    client_id = None
    request_ip = None
    vendor_class = None
    host_name = None

    # DHCPREQUEST mesajını kontrol et
    if "OPTION: 53 ( 1) DHCP message type 3 (DHCPREQUEST)" in data:
        # Client-identifier ayrıştırma
        client_id_match = re.search(r'OPTION: 61 \( 7\) Client-identifier (.+)', data)
        if client_id_match:
            client_id = client_id_match.group(1).strip()

        # Request IP address ayrıştırma
        request_ip_match = re.search(r'OPTION: 50 \( 4\) Request IP address (.+)', data)
        if request_ip_match:
            request_ip = request_ip_match.group(1).strip()

        # Vendor class identifier ayrıştırma
        vendor_class_match = re.search(r'OPTION: 60 \( 15\) Vendor class identifier (.+)', data)
        if vendor_class_match:
            vendor_class = vendor_class_match.group(1).strip()

        # Host name ayrıştırma
        host_name_match = re.search(r'OPTION: 12 \( 12\) Host name (.+)', data)
        if host_name_match:
            host_name = host_name_match.group(1).strip()

    return {
        "Client-identifier": client_id,
        "Request IP address": request_ip,
        "Vendor class identifier": vendor_class,
        "Host name": host_name
    }

def main():
    parsed_data_list = []
    
    try:
        with open('soru6.txt', 'r') as file:
            data_lines = file.readlines()
    except FileNotFoundError:
        print("soru6.txt dosyası bulunamadı.")
        return

    end_time = time.time() + 300  
    for line in data_lines:
        if time.time() > end_time:
            break

        data_str = line.strip() 

        # Alınan veriyi konsola ve parsed_data_list'e yazdır
        print(f"Gelen Veri: {data_str}")
        parsed_data_list.append(f"Gelen Veri: {data_str}")

        # DHCP mesajını ayrıştır
        parsed_data = parse_dhcp_message(data_str)
        if parsed_data:
            parsed_data_list.append(f"Ayrıştırılan Veri: {parsed_data}")
            print(f"Ayrıştırılan Veri: {parsed_data}")

    output_file = 'soru6_parsed.txt'
    with open(output_file, 'w', encoding="utf-8") as f:
        for entry in parsed_data_list:
            f.write(f"{entry}\n")

    print("Ayrıştırma tamamlandı.")
    print(f"Ayrıştırılan veriler '{output_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
