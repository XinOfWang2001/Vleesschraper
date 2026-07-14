import os
import sys
import time

from dotenv import load_dotenv

load_dotenv()

prefix = os.environ.get("STAGE", "dev")

def run_job():
    # Use Polars to collect data in-memory
    print(f"Running job for {prefix} environment")

    # Transform on Polars.

    # Load data into analytics database.
    time.sleep(3)
    print(f"Job completed for {prefix} environment")
    sys.exit(0)


if __name__ == "__main__":
    run_job()
    