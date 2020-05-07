import numpy as np
import matplotlib
import matplotlib.pyplot as plt

"""

Probability simulation
"""
#simulation method
np.random.randint(2)
np.random.randint(2,size=1000)
np.random.randint(2,size=1000).mean()
np.random.choice([0,1])
np.random.choice([0,1],size=1000)
np.random.choice([0,1],size=1000).mean()
np.random.choice([0,1],p=[0.8,0.2],size=1000)
np.random.choice([0,1],p=[0.8,0.2],size=1000).mean()


#1. Two fair coin flips produce exactly two heads
# simulate 1 million tests of two fair coin flips
tests = np.random.randint(2, size=(int(1e6), 2))

# sums of all tests
test_sums = tests.sum(axis=1)

# proportion of tests that produced exactly two heads
(test_sums == 0).mean()

#2.Three fair coin flips produce exactly one head
# simulate 1 million tests of three fair coin flips
tests = np.random.randint(2,size=(int(1e6),3))

# sums of all tests
test_sums = np.sum(tests,axis = 1)

# proportion of tests that produced exactly one head
(test_sums==2).mean()

#3.Three biased coin flips with P(H) = 0.6 produce exactly one head

# simulate 1 million tests of three biased coin flips
# hint: use np.random.choice()
tests = np.random.choice([0,1],p=[0.6,0.4],size=(int(1e6),3))

# sums of all tests
test_sums = np.sum(tests,axis=1)

# proportion of tests that produced exactly one head
(test_sums==2).mean()


# 4. A die rolls an even number
# simulate 1 million tests of one die roll
tests = np.random.randint(1,7,size=int(1e6))
#tests = np.random.choice(np.arange(1, 7), size=int(1e6))
# proportion of tests that produced an even number
even_prop = np.count_nonzero((tests%2==0))/int(1e6)
#(tests % 2 == 0).mean()



#5. Two dice roll a double
# simulate the first million die rolls
first = np.random.randint(1,7,size=int(1e6))

"""

Binomial Distribution
"""

# simulate the second million die rolls
second = np.random.randint(1,7,size=int(1e6))

# proportion of tests where the 1st and 2nd die rolled the same number
same_num_prop = np.count_nonzero(first-second ==0)/int(1e6)
#(first == second).mean()


# number of heads from 10 fair coin flips
np.random.binomial(10, 0.5)

# results from 20 tests with 10 coin flips
np.random.binomial(10, 0.5, 20)

# mean number of heads from the 20 tests
np.random.binomial(10, 0.5, 20).mean()

# reflects the fairness of the coin more closely as # tests increases
np.random.binomial(10, 0.5, 1000000).mean()
plt.hist(np.random.binomial(10, 0.5, 1000000))
plt.show()


#1. A fair coin flip produces heads
# simulate 1 million tests of one fair coin flip
# remember, the output of these tests are the # successes, or # heads
tests = np.random.binomial(1, 0.5, int(1e6))

# proportion of tests that produced heads
(tests == 1).mean()


#2. Five fair coin flips produce exactly one head
# simulate 1 million tests of five fair coin flips
tests = np.random.binomial(5,0.5,int(1e6))

# proportion of tests that produced 1 head
(tests ==1).mean()


#3.Ten fair coin flips produce exactly four heads

# simulate 1 million tests of ten fair coin flips
tests = np.random.binomial(10,0.5, int(1e6))
print(tests)
# proportion of tests that produced 4 heads
(tests==4).mean()

#4. Five biased coin flips with P(H) = 0.8 produce exactly five heads
# simulate 1 million tests of five biased coin flips
tests = np.random.binomial(5,0.8, int(1e6))

# proportion of tests that produced 5 heads
(tests==5).mean()


#5. Ten biased coin flips with P(H) = 0.15 produce at least 3 heads
# simulate 1 million tests of ten biased coin flips
tests = np.random.binomial(10,0.15,int(1e6))

# proportion of tests that produced at least 3 heads
(tests>=3).mean()
