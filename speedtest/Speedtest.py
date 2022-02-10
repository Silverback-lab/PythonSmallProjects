import speedtest

test = speedtest.Speedtest()


print("Loading server list...")
test.get_servers() # -> get list of servers

print("Choosing best server...")
best = test.get_best_server() # -> choosing best server
print(f"Found : {best['host']} located in {best['name']}")

print("Pinging Server...")
ping_result = test.results.ping
print(f"Ping: {ping_result:.2f}ms")

print("Performing download test...")
download_result = test.download()
print(f"Download Speed: {download_result / 1024 / 1024:.2f} mbps")

print("Performing upload test...")
upload_result = test.upload()
print(f"Upload Speed: {upload_result / 1024 / 1024:.2f} mbps")