# Scatter plot of Titanic data
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="ticks",color_codes= True)

# titanic = sns.load_dataset("titanic")
# g = sns.FacetGrid(titanic,row="sex",hue="alone")
# g = (g.map(plt.scatter,"age","fare").add_legend())
# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks",color_codes= True)

titanic = sns.load_dataset("titanic")
plot1 = sns.countplot(x="who",hue="alone",data=titanic)
plot1.set_title("Plot for Counting")
plt.show()
