import os

input_file = 'domains.txt'
output_file = 'ping_results.txt'

with open(input_file, 'r') as file:
    domains = file.read().splitlines()

with open(output_file, 'w') as result_file:
    for domain in domains:
        result_file.write(f"Pinging {domain}...\n")
        response = os.system(f"ping -c 1 {domain} > /dev/null 2>&1")
        if response == 0:
            result_file.write(f"{domain} is reachable \n\n")
        else:
            result_file.write(f"{domain} is not reachable \n\n")

print("Ping results saved in ping_results.txt")
