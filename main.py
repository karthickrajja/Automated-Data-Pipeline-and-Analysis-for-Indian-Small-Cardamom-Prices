import functions_framework
import pandas as pd
import requests
import datetime
import pandas_gbq

def cardamom_data_collection(a):
    url = "http://www.indianspices.com/indianspices/marketing/price/domestic/daily-price-small.html?page=1"
    response = requests.get(url)
    df = pd.read_html(response.content)[1]
    df.columns = df.iloc[0]
    df = df[1:]
    df["Date of Auction"] = pd.to_datetime(df["Date of Auction"])
    df["Date of Auction"] = df["Date of Auction"].dt.date
    today = datetime.date.today()
    df = df[df["Date of Auction"] == today]
    df = df.drop(["Sno"],axis = 1)
    df.columns = ['Date_of_Auction', 'Auctioneer', 'No_of_Lots',
               'Total_Qty_Arrived', 'Qty__Sold', 'MaxPrice',
               'Avg_Price']
    df['No_of_Lots'] = df['No_of_Lots'].astype('Int64')
    df['Total_Qty_Arrived'] = df['Total_Qty_Arrived'].astype('float64')
    df['Qty__Sold'] = df['Qty__Sold'].astype('float64')
    df['MaxPrice'] = df['MaxPrice'].astype('float64')
    df['Avg_Price'] = df['Avg_Price'].astype('float64')
    df['Date_of_Auction'] = pd.to_datetime(df['Date_of_Auction'])
    df['Created_date'] = datetime.datetime.now()
    pandas_gbq.to_gbq(df, "Your dataset_name.table_name", project_id="Your Project Id", if_exists="append") 
    return "done"