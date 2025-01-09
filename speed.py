import speedtest

try:
    hiz=speedtest.Speedtest()
    hiz.get_servers()
    best_server=hiz.get_best_server()

    print(f"Best Server {best_server['host']} ({best_server['country']})")

    download_speed=hiz.download()/1000000
    print(f"Download speed {download_speed:.2f} Mbps")

    upload_speed=hiz.upload()/1000000
    print(f"Upload speed {upload_speed:.2f} Mbps")

    ping=hiz.results.ping
    print(f"Ping {ping:.2f} ms")
except Exception as error:
    print(f"{error}")


