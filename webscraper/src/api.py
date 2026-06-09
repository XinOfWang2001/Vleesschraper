import subprocess
import os

for i in range(5):
    print(f"Run attempt: {i + 1}")
    subprocess.run(["scrapy", "crawl", "quotes"], cwd=os.path.join(os.getcwd(), "myproject"))