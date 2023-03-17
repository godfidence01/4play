import subprocess
import os

# Prompt the user to enter the path to the file containing the list of URLs
file_path = input("Enter the path to the file containing the list of URLs: ")

# Open the file and read the URLs into a list
with open(file_path, "r") as file:
    urls = [line.strip() for line in file]

# Prompt the user to enter the path to the output file
output_file_path = input("Enter the path to the output file: ")

# Get the directory path of the output file
output_dir = os.path.dirname(output_file_path)

# Create the Alive.txt file path
alive_file_path = os.path.join(output_dir, "Alive.txt")

# Create the Dead.txt file path
dead_file_path = os.path.join(output_dir, "Dead.txt")

# Loop through each URL and run the curl -I command using subprocess
with open(output_file_path, "w") as out, open(alive_file_path, "w") as alive, open(dead_file_path, "w") as dead, open(os.path.join(output_dir, "output.txt"), "w") as all_output:
    for url in urls:
        output = subprocess.run(["curl", "-I", url], capture_output=True, text=True)
        if output.stdout:
            all_output.write(f"Output for {url}:\n")
            all_output.write(output.stdout)
            all_output.write("\n")
            out.write(f"Output for {url}:\n")
            out.write(output.stdout)
            out.write("\n")
            # Check the response code
            response_code = int(output.stdout.split()[1])
            if 200 <= response_code <= 399:
                alive.write(f"{url} {response_code}\n")
            else:
                dead.write(f"{url}\n")
        else:
            all_output.write(f"Host {url} seems not alive\n")
            dead.write(f"{url}\n")
