# risk_mitigation/utils.py

def calculate_sharpe_ratio(returns, risk_free_rate):
    # Calculate the Sharpe Ratio based on the returns and risk-free rate
    excess_returns = returns - risk_free_rate
    sharpe_ratio = np.mean(excess_returns) / np.std(returns)
    return sharpe_ratio

# Add more utility functions or helper classes as needed
