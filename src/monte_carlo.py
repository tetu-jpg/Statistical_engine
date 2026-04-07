import random

def simulate_crashes(days):
    crash_probability = 0.045
    crashes = 0

    for i in range(days):
        r = random.random()

        if r < crash_probability:
            crashes += 1


    simulated_probability = crashes / days

    return crashes, simulated_probability
if name =="main":

    days_list = [10, 100, 1000]

    for d in days_list:
        crashes, prob = simulate_crashes(d)
        print("Days: ",d)
        print("Total Crashes: ", crashes)
        print("Simulated Probability: ", prob)
        print()
