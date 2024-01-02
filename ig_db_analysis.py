import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#Further analysis of Instagram database clone data.
#Data is hypothetical (not real data).
#Looking at link between comments and likes on a photo, and tags and likes on a photo.


#COMMENTS AND LIKES
data_com_likes = pd.read_csv('ig_db_comments_likes.csv')

#No null values
data_com_likes.isnull().sum()
    
#Visualization
#Scatterplot to assess link between number of comments and likes:

#creating independent variable as a list
comments = [x for x in data_com_likes["comments_count"]]

#creating dependent variable as a list
likes_com =[y for y in data_com_likes["likes_count"]]

#Scatterplot

sns.set_style("darkgrid")
sns.regplot(x=comments, y=likes_com, scatter = True, fit_reg = True, color = "royalblue")
plt.xlabel("Comments on Photo")
plt.ylabel("Likes On Photo")
plt.title("Assessing Relationship Between Number of Comments and Likes on a Photo")
plt.show()

#boxplot
sns.set_style("darkgrid")
sns.boxplot(x=comments, y=likes_com, color = "royalblue")
plt.xlabel("Comments on Photo")
plt.ylabel("Likes On Photo")
plt.title("Assessing Relationship Between Number of Comments and Likes on a Photo")
plt.show()

#Based off the scatterplot and regression line, there appears to be no association between comments on a photo and likes on that corresponding photo.
#The boxplot confirms this as the distribution of likes does not vary much based on number of comments.

#TAGS AND LKES
data_tags_likes = pd.read_csv("ig_db_tags_likes.csv")

#no null values
data_tags_likes.isnull().sum()

#Visualization
#Scatterplot and regression line to assess link between number of tags and likes

#creating independent variable as a list
tags = [x for x in data_tags_likes["tags_count"]]

#creating dependent variable as a list
likes_tags =[y for y in data_tags_likes["likes_count"]]

#Scatterplot

sns.set_style("darkgrid")
sns.regplot(x=tags, y=likes_tags, scatter = True, fit_reg = True, color = "green")
plt.xlabel("Tags on Photo")
plt.ylabel("Likes On Photo")
plt.title("Assessing Relationship Between Number of Tags and Likes on a Photo")
plt.show()

#boxplot
sns.set_style("darkgrid")
sns.boxplot(x=tags, y=likes_tags, color = "green" , hue=tags)
plt.legend([],[], frameon=False)
plt.xlabel("Tags on Photo")
plt.ylabel("Likes On Photo")
plt.title("Assessing Relationship Between Number of Tags and Likes on a Photo")
plt.show()

#Similarly to above there does not appear to be a link between number of tags used on a photo and likes on that photo.

#SUMMARY:
#There was no relationship between number of tags and likes, or number of comments and likes.
#This may not reflect the reality as this was a small amount of hypothetical data used. 




