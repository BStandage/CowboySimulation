"""cowboy_simulation.py, by Brian Standage. 06-19-2018"""

import random

def main():
    # initializing variables
    one_survivor = 0
    no_survivors = 0
    i = 0
    # randomly chosen probability to make checking for convergence easier
    previous_prob = .20

    # Creates a list of n cowboys each represented by a number 1-n (This is the number of cowboys in the circle)
    n = input("Enter the number of cowboys you wish to: ")
    cowboys = list(range(1, int(n) + 1))
    cowboys_copy = cowboys[:]

    # while loop executes infinitely until the probability converges
    while True:
        i += 1
        while len(cowboys_copy) > 2:
            for j in cowboys:

                # while loop is used to make sure that a cowboy doesn't shoot himself
                while True:
                    cb = random.choice(cowboys)
                    if cb != j:
                        break

                # removes the cowboys who have been shot from a copy of the list this keeps track
                # of living cowboys while also making sure cowboys can be shot more than once
                if (cb in cowboys_copy):
                    cowboys_copy.remove(cb)
            # this simulates creating a new circle with the living cowboys
            cowboys = cowboys_copy[:]

        # Checking and keeping track of how many times there was one survivor
        # and how many times there were no survivors
        if len(cowboys) == 1:
            one_survivor += 1
        else:
            no_survivors += 1

        prob = one_survivor / i
        # Checking for convergence
        if abs(prob - previous_prob) < .00005 and i >= 1000:
            print("Converged at trial: " + str(i))
            break
        else:
            previous_prob = prob

        # creating a new group of n cowboys
        cowboys = list(range(1, int(n) + 1))
        cowboys_copy = cowboys[:]

    # Display results
    print("Trials with one survivor: " + str(one_survivor))
    print("Trials with no survivors: " + str(no_survivors))
    print("Probability of survival with " + n + " cowboys: "+ str(one_survivor/(one_survivor + no_survivors)))


if __name__ == "__main__":
    main()