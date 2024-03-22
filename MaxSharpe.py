import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf


with open("selected_sp_500_stocks.csv", "r") as file:
    tickers = file.readlines()
tickers = tickers[1:]
tickers=[ticker.strip() for ticker in tickers]

end_date = datetime.today()
start_date = '2019-1-1'

adj_close_prices = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start= start_date, end = end_date)
    adj_close_prices[ticker] = data['Adj Close']

normal_log_returns = np.log(adj_close_prices) - np.log(adj_close_prices.shift(1))

total_financial_days= 252
mean_returns = normal_log_returns.mean() * total_financial_days
cov_matrix = normal_log_returns.cov() *np.sqrt(252)

num_portfolios_simulated = 50000

output = pd.DataFrame(columns= ['returns', 'sharpe', 'weights'])
weights_arr = []

for i in range (num_portfolios_simulated):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)
    exp_returns = np.dot(weights, mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe = exp_returns / volatility
    output.loc[i, 'returns'] = exp_returns
    output.loc[i, 'sharpe'] = sharpe
    output.loc[i, 'weights'] = ','.join(str(np.round(weight, 4)) for weight in weights)
    weights_arr.append(weights)

max_sharpe_port = output.iloc[output['sharpe'].idxmax()]

max_sharpe_weights = np.array(max_sharpe_port['weights'].split(','), dtype=float)

example_total_cap = 100000
print("Total capital: ", example_total_cap)

current_price = adj_close_prices.iloc[-1]
allocation = example_total_cap * max_sharpe_weights
number_shares = {ticker: np.floor(allocation[i] / current_price[ticker]) for i, ticker in enumerate(tickers)}

final_data = pd.DataFrame(columns= ['weight', 'number of shares', 'dollar amount'])


for i, ticker in enumerate(tickers):
    weight_percent = f"{round(max_sharpe_weights[i] * 100, 2)}%"
    shares = number_shares[ticker]
    dollar_amt = round(shares * current_price[ticker],2)
    final_data.loc[ticker] = [weight_percent, shares, dollar_amt]
    #print(f"{ticker}: {max_sharpe_weights[i] * 100:.2f}%, number of shares to buy:")

print(final_data)