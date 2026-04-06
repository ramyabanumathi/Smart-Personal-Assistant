import matplotlib.pyplot as plt

def generate_chart(tasks):
    completed = 0
    pending = 0

    for t in tasks:
        if t[3] == 1:
            completed += 1
        else:
            pending += 1

    labels = ["Completed", "Pending"]
    values = [completed, pending]

    plt.bar(labels, values)
    plt.title("Task Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Tasks")

    plt.show()