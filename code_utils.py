import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    return pd.read_csv(filename, skiprows=4)

def clean_data(df, countries):
    df = df[["Country Name"] + [str(year) for year in range(2000, 2023)]]
    df = df[df["Country Name"].isin(countries)]
    df = df.reset_index(drop=True)
    df = df.melt(
        id_vars="Country Name",
        var_name="Year",
        value_name="GDP")
    df["GDP_billions"] = df["GDP"] / 1_000_000_000
    return df.drop(columns=["GDP"])

def plot_data(df):
    plt.figure(figsize=(15, 6))

    for country in df["Country Name"].unique():
        data = df[df["Country Name"] == country]
        plt.plot(data["Year"], data["GDP_billions"], label=country)

    plt.title("GDP over time")
    plt.xlabel("Year")
    plt.ylabel("GDP (billions, constant 2015 US$)")
    plt.legend()
    return plt.show()
