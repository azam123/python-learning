import os
import subprocess
from datetime import datetime

# Define topics and their corresponding files
TOPICS = {
    "Python Basics": ["day1_variables.py", "day2_loops.py", "day3_functions.py"],
    "OOP Concepts": ["day10_classes.py", "day11_inheritance.py", "day12_polymorphism.py"],
    "Kafka Basics": ["day20_kafka_intro.py", "day21_producers.py", "day22_consumers.py"],
    "Terraform Basics": ["day28_terraform_setup.tf", "day29_ec2_instance.tf", "day30_s3_bucket.tf"]
}

# Get the current day of the month
day_of_month = datetime.now().day
topic_keys = list(TOPICS.keys())

# Determine topic based on the day
topic_index = (day_of_month - 1) // 10  # Change topic every 10 days
topic = topic_keys[topic_index]

# Get the file for the specific day
files = TOPICS[topic]
file_index = (day_of_month - 1) % len(files)
file_to_publish = files[file_index]

# Check if file exists, if not create it
if not os.path.exists(file_to_publish):
    with open(file_to_publish, "w") as f:
        f.write(f"# {file_to_publish}\n# Auto-published on Day {day_of_month}")

# Git commands to add, commit, and push changes
subprocess.run(["git", "add", file_to_publish])
subprocess.run(["git", "commit", "-m", f"Day {day_of_month} - {file_to_publish}"])
subprocess.run(["git", "push", "origin", "main"])

print(f"✅ Published {file_to_publish} successfully!")
