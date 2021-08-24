import yfinance as yf   
 
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date 
data = yf.download('BTC-USD','2019-01-01','2021-08-01') 
 
# Plot the close prices 
import matplotlib.pyplot as plt 
data.Close.plot() 
plt.show()