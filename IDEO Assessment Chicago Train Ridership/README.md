# IDEO Assessment Chicago Train Ridership

Project can be viewed without a notebook by opening the html file with any internet browser

A post interview submission for IDEO's data science team.

In this project, I was tasked to help a company open a new store in Chicago, using the dataset providede:
1. https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f
2. https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme

In this project, I chose MOMOFUKU Noodle Bar as my business. I used linear regression to identify stations with the highest growth as well as the highest average ridership. 
Next, I webscrapped yelp for all ramen stores in Chicago and used Geopy to get the lat & long for each of them.

With this information, I created a google map and choropleth using Folium to show the highest avarage rides per wards, with markers of trainstaions that has the highest average rides, as well as train stations with the largest rise since 2001.

## Reflection

It was a really fun project which was ultimately rejected because my coding was deemed too rudimentary. I did not know the existance of seaborn's lmplots before this and was using a very long winded SKlearn + matplotlib method of creating regression plots. With sns.lmplot, I could create a facetgrid + regression graph.

It also took me quite a while to understand how Folium worked and the one I handed in did not have it. (I later found out that the dtype of the column which will be used with KEYON of the choropleth has to be a string instead of an int or float)

The bright side was IDEO mentioned I had good instincts on how to proceed with a vague project, and to apply again when I have better understanding/experience with code and data science.
