import requests
import time

# ask for path of scope.txt
scope_path = input("Enter path of scope.txt file: ")

# read URLs from scope.txt
with open(scope_path, 'r') as file:
    urls = [url.strip() for url in file.readlines()]

# ask for path to save output
output_path = input("Enter path to save output: ")

# create output files
output_files = {
    '200': open(output_path + '/200.txt', 'w'),
    'redirection': open(output_path + '/redirection.txt', 'w'),
    'unknown': open(output_path + '/unknown.txt', 'w'),
    'server_error': open(output_path + '/server_error.txt', 'w'),
    'invalid': open(output_path + '/invalid.txt', 'w')
}

# loop through URLs and make requests with a delay of 5 seconds
for url in urls:
    time.sleep(2)  # delay of 5 seconds

    # make request to URL and get response status code
    try:
        response = requests.get(url)
        status_code = response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        output_files['invalid'].write(f"{url}\n")
        continue

    # save output to appropriate file based on status code
    if status_code == 200:
        output_files['200'].write(f"{url}\n")
    elif status_code in [301, 302]:
        output_files['redirection'].write(f"{url} ({status_code})\n")
    elif status_code >= 400 and status_code <= 499:
        output_files['unknown'].write(f"{url} ({status_code})\n")
    elif status_code >= 500 and status_code <= 599:
        output_files['server_error'].write(f"{url} ({status_code})\n")

# close output files
for file in output_files.values():
    file.close()

print("Done!")
