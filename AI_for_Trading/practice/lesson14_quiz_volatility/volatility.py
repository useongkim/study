import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    max_std = 0
    max_ticker = None
    tickers = prices['ticker'].unique()
    for ticker in tickers:
        price_df = prices.loc[prices['ticker'] == ticker]['price']
        log_return = np.log(price_df/price_df.shift(1))
        std = log_return.std()
        if max_std < std:
            max_std = std;
            max_ticker = ticker

    return max_ticker


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()

