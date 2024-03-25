#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:33:25 2024

@author: louiscacia
"""
import os
import tkinter as tk
import yfinance as yf
import pandas as pd



def get_stock():
    
    try: 
        
        # Get the stock ticker symbol
        ticker = str(ticker_entry.get()).upper()

        # Get the stock data for the specified ticker
        stock = yf.Ticker(ticker)

        # Get the historical data for a specific date
        date = pd.Timestamp(date_entry.get())  # YYYY-MM-DD format
        data = stock.history(start=date, end=date)
        start_date = pd.Timestamp(date, tz="America/New_York")
        end_date = start_date + pd.Timedelta(days=1)
        data = stock.history(start=start_date, end=end_date)

        # Print the closing price for the specified date
        if not data.empty:
            close_price = data["Close"][0]
            result_label.config(text=f"The closing price of {ticker} on {date} was {close_price}")
        else:
            result_label.config(text=f"No data available for {ticker} on {date}")
        
    except:
        result_label.config(text="Not a valid entry")

# Create the main application window
root = tk.Tk()
root.geometry("350x250")
root.title("Options Sidekick")

# Create a label and text entry field for ticker
ticker_label = tk.Label(root, text="Enter your ticker :")
ticker_label.pack()
ticker_entry = tk.Entry(root)
ticker_entry.pack()

# Create a label and text entry field for height
date_label = tk.Label(root, text="Enter your date (in YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()


# Button to calculate BMI
calculate_button = tk.Button(root, text="get quote", command=get_stock)
calculate_button.pack()

# Label to display the BMI result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()