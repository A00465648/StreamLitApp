import matplotlib.pyplot as plt
import pandas as pd

train_df = pd.read_csv('data/train.csv')
print(train_df.value_counts())
test_df = pd.read_csv('data/test.csv')


train_df['Age'].fillna(value=train_df['Age'].median(), inplace=True)


plt.pie(train_df['Sex'].value_counts(), labels = ['Male','Female'], autopct='%1.1f%%', explode  = [0,0.1])
plt.title('Passenger Distribution by Sex')
plt.show()
