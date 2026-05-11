import pandas as pd
import seaborn as sns

df = pd.read_csv('./data/netflix_customer_churn.csv')


df["monthly_fee"].value_counts()