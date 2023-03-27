def toss():
    import random

    toss = random.randint(0, 1)
    coin = "Heads" if toss == 1 else "Tails"
    
    return coin

