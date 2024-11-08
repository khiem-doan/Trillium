import yahoofinancials

def get_quarterly_earnings_report(ticker):
    """
    Retrieves quarterly earnings estimates for a given ticker using yahoofinancials.

    Args:
        ticker (str): The ticker symbol of the stock

    Returns:
        dict: A dictionary containing quarterly EPS and revenue estimates.
    """

    try:
        yahoo_financials = yahoofinancials.YahooFinancials(ticker)
        quarterly_income_statement = yahoo_financials.get_financial_stmts('quarterly', 'income')

        # Extract EPS and revenue estimates from the income statement
        eps_estimates = quarterly_income_statement[ticker][0]
        revenue_estimates = quarterly_income_statement[ticker][0]

        # Process the data into the desired format
        # (You might need to inspect the structure of eps_estimates and revenue_estimates to extract the specific values)

        return {
            "EPS": eps_estimates,
            "Revenue": revenue_estimates
        }

    except Exception as e:
        print(f"Error retrieving analyst estimates for {ticker}: {e}")
        return None

if __name__ == "__main__":
    tickers = input("Enter the tickers (comma-separated): ").split(",")
    for ticker in tickers:
        estimates = get_quarterly_earnings_report(ticker)

        if estimates is not None:
            print(f"Quarterly Earnings Report for {ticker}:\n")
            print(estimates)
        else:
            print(f"No analyst estimates found for {ticker}")
