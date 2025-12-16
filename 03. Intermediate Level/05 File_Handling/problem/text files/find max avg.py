import time

def write_data(days, file_path):
    """Days and temps writing to file (user input)"""
    temps = []
    with open(file_path, "w") as file:
        for day in days:
            while True:
                try:
                    temp = float(input(f"Enter temperature for {day}: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
            temps.append(temp)
            file.write(f"{day}: {temp}\n")
            time.sleep(0.5)  # simulate writing delay
    print("\nData writing complete.\n")
    return temps  # return for further processing


def max_temp(file_path):
    """Find max temp from file"""
    with open(file_path, "r") as file:
        temps = [float(line.strip().split(": ")[1]) for line in file]
    maximum = max(temps)
    print(f"Maximum Temperature: {maximum}°C")
    return maximum


def avg_temp(file_path):
    """Find avg temp from file"""
    with open(file_path, "r") as file:
        temps = [float(line.strip().split(": ")[1]) for line in file]
    average = sum(temps) / len(temps)
    print(f"Average Temperature: {average:.2f}°C")
    return average


# ----------------------------
# Main execution
# ----------------------------
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
file_path = "data.txt"

# Step 1: Get user input and write to file
write_data(days, file_path)

# Step 2: Calculate max and avg from file
maximum = max_temp(file_path)
average = avg_temp(file_path)

# Step 3: Summary Report
print("\nSummary Report:")
print(f"Days Recorded: {len(days)}")
print(f"Maximum Temperature: {maximum}°C")
print(f"Average Temperature: {average:.2f}°C")
