import time

def write_data(days, temps):
    """Days and temps writing to file"""
    print("Writing temperature data...\n")
    for day, temp in zip(days, temps):
        print(f"{day}: {temp}°C")
        time.sleep(1)
    print("\nData writing complete.\n")
    return temps  # return temps list for further use


def max_temp(temps):
    """Find max temp from file"""
    maximum = max(temps)
    print(f"Maximum Temperature: {maximum}°C")
    return maximum


def avg_temp(temps):
    """Find avg temp from file"""
    average = sum(temps) / len(temps)
    print(f"Average Temperature: {average:.2f}°C")
    return average


# ----------------------------
# Main Program Execution
# ----------------------------
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temps = [25.5, 28.0, 30.2, 27.8, 29.5, 31.0, 26.4]  # parameter wise temperature data

# Step 1: Data writing to file
recorded_temps = write_data(days, temps)

# Step 2: Find max temp from file
max_value = max_temp(recorded_temps)

# Step 3: Find avg temp from file
avg_value = avg_temp(recorded_temps)

# Step 4: Summary Report
print("\nSummary Report:")
print(f"Days Recorded: {len(days)}")
print(f"Maximum Temperature: {max_value}°C")
print(f"Average Temperature: {avg_value:.2f}°C")
