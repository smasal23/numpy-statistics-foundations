import numpy as np

# How to create Random Values? - will always give random float values between 0 and 1
# Random.rand()
print(np.random.rand(5))
#* Array of Random values
np.random.rand(2, 3)
# Array of integers
np.random.randint(100, size = (2, 4))
np.random.randint(low = 300, high = 400, size = (3, 5))

# Matrices
# Gives a matrix of zero
print(np.zeros((3, 4)))
# Gives a matrix of one
print(np.ones((5, 7)))
# Gives a matrix of diagonal ones according to the specified size
print(np.eye(5))
# Gives a matrix full of specified fill_value in the parameters.
np.full((3, 6), 6)

# arange
SN = np.arange(1, 501)
print(SN)


# Manipulation of array shapes
x1 = np.arange(1, 16)
print(x1)
#* reshape
print(x1.reshape(3, 5)) # We can convert a one dimensional array into a matrix according to the specified shape.


# Transform n dimensional array into one dimension.
#* Flatten
x1.flatten()

x1.ravel() - # faster and memory efficient compared to flatten.


# Stacking numpy arrays
x2 = np.arange(1, 10).reshape(3,3)
print(x2)

x3 = np.array([[1,2,3], [22,33,44], [100, 300, 400]]) # Remember a list within a list for coding arrays as well.
print(x3)

# hstack
np.hstack((x2, x3))
np.concatenate((x1, x2), axis = 1)

# vstack
np.vstack((x2, x3))


# Probability
np.random.choice(['H', 'T',], size = 10)
# Sample space
S = np.arange(1, 7)
E = S[S % 2 == 0]

print('Sample space:', S)
print('Event space:', E)


# Axioms of Probability
# 1] Probability between 0 and 1 (0 < P(A) < 1)
# 2] Total Probability of sample space = 1, (P(S) = 1)
# 3] If A and B can't happen together
#    P(A U B) = P(A) + P(B)


# Conditional Probability
    # Probability of event A happening given that event B already happened.
#        P(A | B) = P(A intersection B)/ P(B)

# Total Probability Theorem
    # When an event depends on multiple condition.
# P(A) = P(A|B1).P(B) + P(A|B2).P(B2) + P(A|B3).P(B3)

#    Probability of getting defective product


# Bayes Theorem
# P(A | B) = P(B | A) * P(B) / P(A)

# Prior probablilty
# Likelihood of observing B of A
# Total Probability
# Posterior Probability