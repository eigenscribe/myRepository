import pandas as pd 
import scipy.stats as st
import math 

df = pd.read_csv('credit_card_cleaned.csv')

# Calculate population parameters
pop_mean = df['AGE'].mean()
pop_std_dev = df['AGE'].std()

# Sample
sample_size = 100
sample = df['AGE'].sample(n = sample_size,random_state = 5)
sample_mean = sample.mean()

# Confidence interval caclulations
cl = 0.95
quantile = 1 - ( (1-cl)/2 )
z_value = st.norm.ppf(q = quantile)

margin_error = z_value * (pop_std_dev / math.sqrt(sample_size))
CI = (sample_mean - margin_error,sample_mean + margin_error)


print('Sample Mean : ',sample_mean)
print('margin of error : ', margin_error)
print('CI : ',CI)
print('Population Mean : ', pop_mean)