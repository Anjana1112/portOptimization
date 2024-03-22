
# Portfolio Optimization using Maximum Sharpe Ratio

This python script constructs an optimized investment portfolio using Modern Portfolio Theory (MPT). It maximizes the portfolio's Sharpe ratio and allocates capital efficiently by importing historical stock data for selected S&P 500 stocks, calculating returns, covariance matrix, and then simulating multiple portfolios to find the one with the highest Sharpe ratio.



## Usage

**Dependencies**:

- pandas
- numpy 
- yfinance 
- datetime

It can be installed in terminal using: 

    pip install pandas numpy yfinance datetime

- CSV file named "selected_sp_500_stocks.csv" containing the tickers of the selected S&P 500 stocks

- Run the script

Example output:

Total capital:  100000

           weight  number of shares  dollar amount
    
    MSFT    0.9%               2.0         858.74
    NVDA   9.39%              10.0        9143.50
    AMZN   0.95%               5.0         890.75
    META   0.08%               0.0           0.00
    GOOG    0.8%               5.0         743.70
    LLY   10.09%              13.0       10013.38
    AVGO   7.83%               5.0        6740.00
    TSLA   4.46%              25.0        4320.50
    JPM    1.94%               9.0        1791.54
    UNH     0.8%               1.0         491.69
    V      2.04%               7.0        2032.59
    XOM    5.08%              44.0        4993.56
    JNJ    7.15%              45.0        7008.75
    MA     3.45%               7.0        3420.48
    NFLX   1.41%               2.0        1245.42
    AMD    7.66%              42.0        7504.56
    CRM    0.83%               2.0         616.78
    MRK    9.61%              77.0        9518.74
    HD     6.86%              17.0        6718.40
    COST   5.01%               6.0        4455.36
    ABBV  10.22%              57.0       10117.50
    PG     3.45%              21.0        3399.06


