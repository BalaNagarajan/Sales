import pandas as pd
import matplotlib.pyplot as plt
import os


# File path to the Parts CSV file
parent_path = os.path.dirname(os.getcwd())
sales_data_path = os.path.join(parent_path, "data", "sales_data.csv")

#Read from sales_data.csv under/data folder and group by SHOWROOM_ID and compute the total PRICE for each SHOWROOM_ID and prints a output to the console
def sales_analyzer():
   
    # Read the data from the csv file
    data = pd.read_csv(sales_data_path)
    # Group the data by SHOWROOM_ID and compute the sum of PRICE for each SHOWROOM_ID

    grouped_data = data.groupby("SHOWROOM_ID")["PRICE"].sum()
    # Find the showroom with the highest sales

    max_sales_showroom = grouped_data.idxmax()
    max_sales_city = data.loc[data["SHOWROOM_ID"] == max_sales_showroom, "CITY"].iloc[0]
    print(f"Showroom with highest sales: SHOWROOM_ID {max_sales_showroom}, CITY {max_sales_city}")

    # Find the showroom with the lowest sales
    min_sales_showroom = grouped_data.idxmin()
    min_sales_city = data.loc[data["SHOWROOM_ID"] == min_sales_showroom, "CITY"].iloc[0]
    print(f"Showroom with lowest sales: SHOWROOM_ID {min_sales_showroom}, CITY {min_sales_city}")
    # Plot a pie chart based on each SHOWROOM_ID
    data.groupby("SHOWROOM_ID")["PRICE"].sum().plot(kind="pie", autopct="%1.1f%%")

    plt.axis("equal")
    plt.show()

    # Group the data by CITY and find the most frequent MODEL and TYPE for each city
    famous_models = data.groupby("CITY")["MODEL"].agg(lambda x: x.value_counts().index[0])
    famous_types = data.groupby("CITY")["TYPE"].agg(lambda x: x.value_counts().index[0])

    # Create a bar graph to visualize the famous models and types for each city
    plt.figure(figsize=(10, 6))
    plt.bar(famous_models.index, famous_models.values, label="Famous Model")
    plt.bar(famous_types.index, famous_types.values, label="Famous Type")

    plt.xlabel("City")
    plt.ylabel("Count")
    plt.title("Famous Models and Types for Each City")
    plt.legend()

    plt.show()
if __name__ == "__main__":
    sales_analyzer()
