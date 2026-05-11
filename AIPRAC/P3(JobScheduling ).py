# Job Scheduling Problem using Greedy Method

# Input number of jobs
n = int(input("Enter number of jobs: "))

jobs = []

# Input job details
for i in range(n):

    job_id = input(f"\nEnter Job ID for Job {i+1}: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append([job_id, deadline, profit])

# Sort jobs according to profit (descending order)
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = max(job[1] for job in jobs)

# Create slots
slots = [False] * max_deadline
job_sequence = ['-'] * max_deadline

total_profit = 0

# Perform job scheduling
for job in jobs:

    job_id = job[0]
    deadline = job[1]
    profit = job[2]

    # Find free slot from deadline-1 to 0
    for j in range(deadline - 1, -1, -1):

        if not slots[j]:

            slots[j] = True
            job_sequence[j] = job_id
            total_profit += profit

            break

# Display result
print("\nSelected Job Sequence:")

for job in job_sequence:
    if job != '-':
        print(job, end=" ")

print("\n\nTotal Profit:", total_profit)