def toss():
    import random

    toss = random.randint(0, 1)
    tossResult = "Heads" if toss == 1 else "Tails"

    return tossResult

