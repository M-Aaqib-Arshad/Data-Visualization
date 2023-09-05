# Steps in Data Visulization 

#Step: 1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#step :2  Select the theme
# set a theme
sns.set_theme(style="ticks",color_codes=True)

# Step: 3 import data form data set or you can also import your own data
# import data set to use seaborn
# titanic is built-in data of seaborn
ship = sns.load_dataset('titanic')

# step : 4 
#basic Graph
# p = sns.countplot(x="sex", data=ship)
# plt.show()

# step : 5

p = sns.countplot(x="sex", data=ship, hue="class")
p.set_title("Advance Count Plot for Titanic ship tickets")
plt.show()

