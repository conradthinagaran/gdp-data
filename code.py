import pandas as pd
import matplotlib.pyplot as plt

countries = [
    "United Kingdom",
    "United States", 
    "Brazil", 
    "Japan", 
    "China", 
    "Germany", 
    "Switzerland",
]

df = pd.read_csv("data.csv", skiprows=4)
df = df[["Country Name"] + [str(year) for year in range(2000, 2023)]]
df = df[df["Country Name"].isin(countries)]
df = df.reset_index(drop=True)
df = df.melt(
    id_vars="Country Name",
    var_name="Year",
    value_name="GDP"
)
df["GDP_billions"] = df["GDP"] / 1_000_000_000
df = df.drop(columns=["GDP"])
print(df)

uk = df[df["Country Name"] == "United Kingdom"]
us = df[df["Country Name"] == "United States"]
cn = df[df["Country Name"] == "China"]
br = df[df["Country Name"] == "Brazil"]
ge = df[df["Country Name"] == "Germany"]
jp = df[df["Country Name"] == "Japan"]
sw = df[df["Country Name"] == "Switzerland"]

plt.figure(figsize=(15, 6))

plt.plot(uk["Year"], uk["GDP_billions"])
plt.plot(cn["Year"], cn["GDP_billions"])
plt.plot(us["Year"], us["GDP_billions"])
plt.plot(br["Year"], br["GDP_billions"])
plt.plot(ge["Year"], ge["GDP_billions"])
plt.plot(jp["Year"], jp["GDP_billions"])
plt.plot(sw["Year"], sw["GDP_billions"])

plt.title("GDP over time")
plt.xlabel("Year")
plt.ylabel("GDP (billions, in 2015 dollars)")

plt.show()