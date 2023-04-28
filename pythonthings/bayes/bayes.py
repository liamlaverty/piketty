
def Bayes(p_a, p_b, p_b_a):
    """calculates the probability that p_a orrurs, given that p_b occurs
        p_a is the probability that event A occurs
        p_b is the probability that event B occurs

        p_b_a is the probability that event B occurs if event A occurs
    """
   
    prob_a_b = (p_a * p_b_a) / p_b
    
    return prob_a_b




bayes_probability_test = Bayes(0.1, 0.98, 0.8)
print("Bayes Probabiliy test is expected 8.16, was {}".format(bayes_probability_test * 100))