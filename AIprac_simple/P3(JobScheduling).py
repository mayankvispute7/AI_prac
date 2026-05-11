jobs = [
    ['J1', 2, 100],
    ['J2', 1, 19],
    ['J3', 2, 27],
    ['J4', 1, 25],
    ['J5', 3, 15]
]

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = 3

slots = [False] * max_deadline

result = ['-'] * max_deadline

profit = 0

for job in jobs:

    for j in range(job[1] - 1, -1, -1):

        if not slots[j]:

            slots[j] = True

            result[j] = job[0]

            profit += job[2]

            break

print("Job Sequence:")

print(result)

print("Total Profit:", profit)