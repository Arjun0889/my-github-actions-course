import os
import time
import requests

def ping_url(url, delay, max_trials):
    """
    Pings the provided URL at regular intervals.
    
    Args:
        url (str): The URL to ping.
        delay (int): The time (in seconds) to wait between retries.
        max_trials (int): The maximum number of retry attempts.

    Returns:
        bool: True if the URL responds with a 200 status code, False otherwise.
    """
    trials = 0
    while trials < max_trials:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Website {url} is reachable")
                return True
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        print(f"Attempt {trials + 1}/{max_trials} failed. Retrying in {delay} seconds...")
        time.sleep(delay)
        trials += 1

    return False

def run():
    """
    Retrieves input values from environment variables and calls `ping_url`.
    Raises an exception if the URL does not respond successfully.
    """
    url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY", 5))  # Default delay of 5 seconds if not provided
    max_trials = int(os.getenv("INPUT_MAX_TRIALS", 3))  # Default max_trials to 3 if not provided

    if not url:
        raise ValueError("INPUT_URL environment variable is required but not set.")

    print(f"Pinging {url} with a delay of {delay} seconds (Max trials: {max_trials})...")

    if not ping_url(url, delay, max_trials):
        raise Exception(f"Failed to reach {url} after {max_trials} attempts.")
    

if __name__ == "__main__":
    run()
