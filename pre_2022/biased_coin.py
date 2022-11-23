# Goal: Simulate a biased coin. Using the biased coin, generate
# a sample of heads/tails as if it were a fair coin.

from random import *

# Define bias
bias = random()
print("Bias is:"+str(bias))

# Generate a distribution
samples = 85
number_printed = 10
distribution_biased = [1 if bias > random() else 0 for sample in range(samples)]

# Describe the biased distribution
distribution_b_mean = sum(distribution_biased)/len(distribution_biased)
print('\nThe original distribution mean is:'+str(distribution_b_mean))
print(f'First {number_printed} values:')
print(['T' if flip == 0 else 'H' for flip in distribution_biased[0:number_printed]])
if distribution_b_mean > 0.5:
	print('This distribution favors heads.')
else:
	print('This distribution favors tails.')
	
# Find distribution mean, and use that to correct existing values	
if distribution_b_mean > 0.5:
	print('\nThreshold to convert H to T is '+str(abs(1-0.5/distribution_b_mean)))
	distribution_fair = [int(random()>abs(1-0.5/distribution_b_mean)) if sample == 1 else 0 for sample in distribution_biased]
else:
	print('\nThreshold to convert T to H is '+str(abs(1-0.5/(1-distribution_b_mean))))
	distribution_fair = [int(random()<abs(1-0.5/(1-distribution_b_mean))) if sample == 0 else 1 for sample in distribution_biased]

# Describe the fair distribution
distribution_f_mean = sum(distribution_fair)/len(distribution_fair)
print("\nFair distribution's mean is:"+str(distribution_f_mean))
print(f'First {number_printed} values:')
print(['T' if flip == 0 else 'H' for flip in distribution_fair[0:number_printed]])
