# Real-Time Stock Portfolio Tracker

This project allows users to track their stock portfolio in real time. It uses efficient data structures for managing stocks, portfolio details, and stock market data, while providing a graphical interface to display this data dynamically.

## How It Works
The program provides the following functionalities:
1. **Portfolio Management**: Users can add, remove, and view stocks in their portfolio, including details like stock symbol, number of shares, and purchase price.
2. **Real-Time Stock Prices**: Fetches real-time stock prices using the Alpha Vantage API.
3. **Stock Transactions**: Allows users to keep track of stock purchases and sales.
4. **Visualization**: Displays portfolio summary and visualizes stock trends over time using charts and graphs.

## Features
- **Add/Remove Stocks**: Easily manage stocks in your portfolio.
- **Real-Time Price Updates**: Fetch current stock prices via API.
- **Portfolio Summary**: View the total portfolio value and individual stock details.
- **Transaction History**: Keep track of stock transactions.
- **Graphical Representation**: Visualize stock trends over time with graphs and charts.

## Sample Run
1. Add stocks to the portfolio with the stock symbol, number of shares, and purchase price.  
2. Remove stocks using the stock symbol.  
3. Fetch and update real-time stock prices by providing the stock symbol.  
4. View the entire portfolio and its total value.  
5. Visualize portfolio growth and trends using real-time data.

## How to Run
### Requirements
- Required Libraries: `PyQt5`, `requests`
 ```bash
  pip install PyQt5 requests
  ```
  
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nerdylua/DSA-lab-part-b.git
   cd realtime-stock-tracker
   ```
1. Replace the `api_key` in the code with your own Alpha Vantage API key.

### Run the application
Execute the following command:
```bash
python stock_tracker.py
```

### Data Structures Used
- Linked List: Manages the portfolio as a collection of stock nodes.
- Hash Map: Efficiently fetches and updates stock prices.
- Stack: Tracks stock transactions for undo/redo operations (future expansion).
- Priority Queue: Allows sorting stocks by performance metrics (future expansion).
- Graph: Displays stock price trends using graphical charts.

### Tools and Technologies
- Programming Language: Python
- GUI Framework: PyQt5
- API: Alpha Vantage for stock data
- Graphing Libraries: Matplotlib or Plotly

### License
This project is licensed under the MIT License. Feel free to use and modify it.

Happy tracking! 🎉
