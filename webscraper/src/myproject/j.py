import subprocess
for i in range(2):
    print(f"Run attempt: {i + 1}")
    subprocess.run(["scrapy", "crawl", "quotes"])
    print(f"Completed run {i + 1}\n")
