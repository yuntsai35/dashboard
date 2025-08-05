import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://drive.google.com/uc?id=1HzSqBa_3ZCOre-jB64-nwuPHiEwAvbRZ

years = st.multiselect("選擇年份", sorted(df["birthyear"].unique()), default=[2010])

filtered_df = df[df["birthyear"].isin(years)]

fig, ax = plt.subplots()
sns.swarmplot(x="birthyear", y="dischage", data=filtered_df, size=0.5, ax=ax)

ax.set_title("Birthyear vs Discharge Age")
ax.set_xlabel("Birth Year")
ax.set_ylabel("Discharge Age (Days)")

st.pyplot(fig)


