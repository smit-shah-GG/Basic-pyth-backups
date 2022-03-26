import yfinance as yf

googl = yf.Ticker("GOOGL")

print(googl.info)
print(googl.history(period="max"))
print(googl.major_holders)

"""
List of available methods:

>> .info
>> .history
>> .actions
>> .dividends
>> .splits
>> .financials, .quaterly_financials
>> .major_holders, .institutional_holders
>> .balance_sheet, .quaterly_balance_sheet
>> .cashflow, .quaterly_cashflow
>> .earnings, .quaterly_earnings
>> .sustainability
>> .recommendations
>> .calendar
>> .isin                                   SHOWS INTERNATIONAL SECURITIES IDENTIFICATION NUMBER, IS EXPERIMENTAL
>> .options
>> .news

Returns a pandas df as object, eg. googl here is a pandas df

Can also make a 2D dataframe that includes multiple tickers:
Can be done as data = yf.download("MSFT GOOGL")

"""

print("\n Dataframe: ")
data = yf.download(tickers = "MSFT GOOGL AAPL", period = "max", auto_adjust = True, threads = True)
print(data)
