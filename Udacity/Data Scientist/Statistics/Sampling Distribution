import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.random.seed(42)

students = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])

#1. Find the proportion of students who drink coffee in the above array. Store this value in a variable p.

p = np.mean(students)
print(p)

#2. Use numpy's random.choice to simulate 5 draws from the students array.
#What is proportion of your sample drink coffee?

sampling_set = np.random.choice(students,size = 5)
print(sampling_set)
print(np.mean(sampling_set==1))

#3. Repeat the above to obtain 10,000 additional proportions, where each sample was of size 5. Store these in a variable called sample_props.

sample_props = []
for _ in range(10000):
    sample = np.random.choice(students, 5, replace=True)
    sample_props.append(sample.mean())

print(sample_props)



#4. What is the mean proportion of all 10,000 of these proportions? This is often called the mean of the sampling distribution.
mean_sam_dis= np.mean(np.array(sample_props))
print(mean_sam_dis)

#5. What are the variance and standard deviation for the original 21 data values?
stu_var = np.var(students)
stu_std = np.std(students)
print(stu_var,stu_std)

#6. What are the variance and standard deviation for the 10,000 proportions you created?
sampling_var = np.var(sample_props)
sampling_std = np.std(sample_props)
print(sampling_var,sampling_std)



#7. Compute p(1-p), which of your answers does this most closely match?
print(p*(1-p))  # standard deviation of the sampling distribution

#8. Compute p(1-p)/n, which of your answers does this most closely match?

print(p*(1-p)/5)  # variance of the sampling distribution.

#9. Notice that your answer to 8. is commonly called the variance of the sampling distribution.
#If you were to change your first sample to be 20, what would this do for the variance of the sampling distribution?
#Simulate and calculate the new answers in 6. and 8. to check that the consistency you found before still holds.
##Simulate your 20 draws

#above sampling is wrong
sample_props = []
for _ in range(10000):
    sample_20 = np.random.choice(students, 20, replace=True)
    sample_props_20.append(sample_20.mean())
print(sample_props_20)


##Compare your variance values as computed in 6 and 8,
##but with your sample of 20 values
sampling_var_20 = np.var(np.array(sample_props_20))
sampling_std_20 = np.std(np.array(sample_props_20))
print(sampling_var_20,sampling_std_20)


#10. Finally, plot a histgram of the 10,000 draws from both the proportions with a sample size of 5 and the proportions with a sample size of 20.
#Each of these distributions is a sampling distribution.
#One is for the proportions of sample size 5 and the other a sampling distribution for proportions with sample size 20.
plt.hist(sample_props, alpha=.5);
plt.hist(np.array(sample_props_20), alpha=.5);
