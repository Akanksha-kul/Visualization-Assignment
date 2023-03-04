
"""Import the necessary libraries ."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the relevant datset
data=pd.read_csv("amsterdam_weekdays.csv")

#Create a line plot 

def line_plot(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Arrange the data in ascending order as per Guest Satisfaction overall Rating
dy=data.sort_values("guest_satisfaction_overall")
dy1=dy[['guest_satisfaction_overall','dist','metro_dist','cleanliness_rating']]
df=dy1.iloc[25::100]


# Create line plot for overall guest rating against distance from city centre, from metro and the cleanliness rating
plt.plot(df['guest_satisfaction_overall'], df['dist'], label='dist')
plt.plot(df['guest_satisfaction_overall'], df['metro_dist'], label='metro_dist')
plt.plot(df['guest_satisfaction_overall'], df['cleanliness_rating'], label='cleanliness_rating')

plt.title('Overall ratings given by guests')
plt.ylabel('Factors for rating')
plt.xlabel('Guest Ratings')
plt.legend()
plt.show()



"""point plot"""

df = pd.read_csv("amsterdam_weekdays.csv")
df1=df.iloc[0::150]



def read_csv(filename):
    #Read the CSV file and returns a pandas DataFrame
    df = pd.read_csv("amsterdam_weekdays.csv")
    return df

#Create a point plot using seaborn

sns.set(rc={'figure.figsize':(11.6,8.27)})
ax=sns.pointplot(x="realSum",y="person_capacity",data=df1)
plt.xlabel("Prices of the listing")
plt.ylabel("Person Capacity")
plt.title("Price of Listing as per Person Capacity")
plt.show()



#Create a pie chart for understanding which types of rooms are preferred by the guests

def pie_chart(x, y, title, x_label, y_label):
    plt.plot(x, y)
   
priv_room=0
ent_home_apt=0
shared_room=0

for i in range (len(data["room_type"])):
    if(data["room_type"][i]=="Private room"):
        priv_room=priv_room+1
    elif(data["room_type"][i]=="Entire home/apt"):
        ent_home_apt=ent_home_apt+1
    elif(data["room_type"][i]=="Shared room"):
        shared_room=shared_room+1
    else:
        default:0

x=[priv_room, ent_home_apt, shared_room]
y=['Private Room','Entire Home or Apartment', 'Shared Room']
plt.pie(x,labels=y,autopct="%1.0f%%")
plt.title('Percentage of the room types usually booked by the guests')


plt.show()

