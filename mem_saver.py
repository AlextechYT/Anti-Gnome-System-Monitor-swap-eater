import psutil
import subprocess
import time

# Set the swap usage threshold (in percentage) at which you want to restart System Monitor
SWAP_THRESHOLD = 80.0  # Example: Restart when swap usage is above 80%

# Function to get current swap usage
def check_swap():
    swap = psutil.swap_memory()
    return swap.percent  # Returns percentage of used swap memory

# Function to kill System Monitor
def kill_system_monitor():
    try:
        # Check if the gnome-system-monitor process is running and kill it
        subprocess.run(['pkill', 'gnome-system-monitor'], check=True)
        print("System Monitor killed successfully.")
    except subprocess.CalledProcessError:
        print("System Monitor was not running.")

# Function to restart System Monitor
def restart_system_monitor():
    try:
        # Start System Monitor
        subprocess.Popen(['gnome-system-monitor'])
        print("System Monitor restarted successfully.")
    except Exception as e:
        print(f"Failed to restart System Monitor: {e}")

# Main monitoring loop
def monitor_swap():
    while True:
        swap_usage = check_swap()

        if swap_usage > SWAP_THRESHOLD:
            print(f"Swap is heavily used: {swap_usage}% used. Restarting System Monitor.")
            kill_system_monitor()  # Kill the System Monitor if running
            time.sleep(2)          # Wait 2 seconds before restarting
            restart_system_monitor()  # Restart the System Monitor

        else:
            print(f"Swap usage is fine: {swap_usage}% used.")
        
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    monitor_swap()
