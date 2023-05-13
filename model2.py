#  Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
#print (dataset.shape)
#print (dataset.head(5))

#  Implementing UCB
import math
observations = 10000  
no_of_Ads = 10

ads_selected = []
total_reward = 0

numbers_of_selections_of_each_ads = [0] * no_of_Ads
sums_of_rewards_of_each_ads = [0] * no_of_Ads


for n in range(0, observations):
  ad = 0
  max_upper_bound = 0
  
  for i in range(0, no_of_Ads):
    if (numbers_of_selections_of_each_ads[i] > 0):
      average_reward = sums_of_rewards_of_each_ads[i] / numbers_of_selections_of_each_ads[i]
      delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections_of_each_ads[i])
      upper_bound = average_reward + delta_i
    
    else:
      upper_bound = 1e400
    
    if (upper_bound > max_upper_bound):
      max_upper_bound = upper_bound
      ad = i
  
  ads_selected.append(ad)
  numbers_of_selections_of_each_ads[ad] = numbers_of_selections_of_each_ads[ad] + 1
  reward = dataset.values[n, ad]
  sums_of_rewards_of_each_ads[ad] = sums_of_rewards_of_each_ads[ad] + reward
  total_reward = total_reward + reward

#print("Rewards by Ads = ",sums_of_rewards_of_each_ads)
#print("Total Rewards by UCB = ",total_reward)

#  Visualising the results --- Histogram of ads selected
plt.figure(figsize = (7,5))
plt.bar(x=dataset.columns, height=10)
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.xticks(horizontalalignment='center', fontsize='9', color='black')
plt.yticks(fontsize='9', color='black')
plt.tight_layout()
#plt.show()

true_clicks = []
for i in range(0,10):
    true_clicks.append(sum(dataset.iloc[:,i:i+1].values))
    
true_clicks = [int(item) for item in true_clicks]
    
true_clicks_array = np.array(true_clicks)
true_clicks_array = true_clicks_array.reshape(1,10)

true_clicks_df = pd.DataFrame(data=true_clicks_array, columns=dataset.columns, index=['Total True Clicks'])
#print(true_clicks_df)

#  Visualising the results --- True Clicks on Ads
plt.figure(figsize = (7,5))
plt.bar(x=dataset.columns, height=true_clicks)
plt.title('True Clicks on Ads\n')
plt.xlabel('\nAds', color='black')
plt.ylabel('Clicks\n', color='black')
plt.xticks(horizontalalignment='center', fontsize='9', color='black')
plt.yticks(fontsize='9', color='black')
plt.tight_layout()
#plt.show()

# Find the index of the ad with the most rewards
best_ad = sums_of_rewards_of_each_ads.index(max(sums_of_rewards_of_each_ads))
#print("Best ad is: Ad", best_ad+1)

import pickle

# Determine the index of the ad with the most rewards
best_ad = sums_of_rewards_of_each_ads.index(max(sums_of_rewards_of_each_ads))

# Save the variables to a file
data = {"dataset": dataset, "ads_selected": ads_selected, "true_clicks": true_clicks, "best_ad": best_ad}
with open("UCB_data.pickle", "wb") as f:
    pickle.dump(data, f)

