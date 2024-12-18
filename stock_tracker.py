import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Stock Class
class Stock:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.next = None


# Portfolio Class
class Portfolio:
    def __init__(self):
        self.head = None

    def add_stock(self, symbol, shares, price):
        new_stock = Stock(symbol, shares, price)
        new_stock.next = self.head
        self.head = new_stock

    def remove_stock(self, symbol):
        temp = self.head
        prev = None
        while temp:
            if temp.symbol == symbol:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                del temp
                return True
            prev = temp
            temp = temp.next
        return False

    def update_stock_price(self, symbol, new_price):
        temp = self.head
        while temp:
            if temp.symbol == symbol:
                temp.price = new_price
                return True
            temp = temp.next
        return False

    def get_total_value(self):
        total_value = 0.0
        temp = self.head
        while temp:
            total_value += temp.shares * temp.price
            temp = temp.next
        return total_value

    def display_portfolio(self):
        portfolio_data = ""
        temp = self.head
        while temp:
            portfolio_data += f"{temp.symbol} - {temp.shares} shares at ${temp.price:.2f} each\n"
            temp = temp.next
        return portfolio_data if portfolio_data else "No stocks in portfolio"


# Main App Class
class StockTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Portfolio Tracker")
        self.portfolio = Portfolio()
        self.api_key = "R02AZ2MTJ5THYL24"  # Replace with your API key

        # Layout setup
        main_layout = QVBoxLayout()

        # Add Stock Section
        add_stock_layout = QHBoxLayout()
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Stock Symbol")
        self.shares_input = QLineEdit()
        self.shares_input.setPlaceholderText("Shares")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Price per Share")
        add_stock_button = QPushButton("Add Stock")
        add_stock_button.clicked.connect(self.add_stock)

        add_stock_layout.addWidget(self.symbol_input)
        add_stock_layout.addWidget(self.shares_input)
        add_stock_layout.addWidget(self.price_input)
        add_stock_layout.addWidget(add_stock_button)
        main_layout.addLayout(add_stock_layout)

        # Remove Stock Section
        remove_stock_layout = QHBoxLayout()
        self.remove_input = QLineEdit()
        self.remove_input.setPlaceholderText("Remove Stock Symbol")
        remove_stock_button = QPushButton("Remove Stock")
        remove_stock_button.clicked.connect(self.remove_stock)

        remove_stock_layout.addWidget(self.remove_input)
        remove_stock_layout.addWidget(remove_stock_button)
        main_layout.addLayout(remove_stock_layout)

        # Update Price Section
        update_price_layout = QHBoxLayout()
        self.update_symbol_input = QLineEdit()
        self.update_symbol_input.setPlaceholderText("Update Stock Symbol")
        update_price_button = QPushButton("Fetch & Update Price")
        update_price_button.clicked.connect(self.update_stock_price)

        update_price_layout.addWidget(self.update_symbol_input)
        update_price_layout.addWidget(update_price_button)
        main_layout.addLayout(update_price_layout)

        # Show Portfolio Button
        show_portfolio_button = QPushButton("Show Portfolio")
        show_portfolio_button.clicked.connect(self.show_portfolio)
        main_layout.addWidget(show_portfolio_button)

        # Total Value Label
        self.total_value_label = QLabel("Total Portfolio Value: $0.00")
        main_layout.addWidget(self.total_value_label)

        # Apply styles
        self.apply_styles()
        self.setLayout(main_layout)

    def apply_styles(self):
        font = QFont("Arial", 14)
        self.symbol_input.setFont(font)
        self.shares_input.setFont(font)
        self.price_input.setFont(font)
        self.remove_input.setFont(font)
        self.update_symbol_input.setFont(font)
        self.total_value_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.total_value_label.setAlignment(Qt.AlignCenter)

    def fetch_stock_price(self, symbol):
        try:
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
            response = requests.get(url)
            data = response.json()
            print(data)  # Debug: Print the entire response
            if "Global Quote" in data and "05. price" in data["Global Quote"]:
                price = float(data["Global Quote"]["05. price"])
                return price
            else:
                raise ValueError("Invalid response format or symbol not found.")
        except Exception as e:
            QMessageBox.warning(self, "API Error", f"Failed to fetch price for {symbol}: {e}")
            return None


    def add_stock(self):
        symbol = self.symbol_input.text()
        try:
            shares = int(self.shares_input.text())
            price = float(self.price_input.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid shares and price.")
            return

        self.portfolio.add_stock(symbol, shares, price)
        QMessageBox.information(self, "Stock Added", f"{symbol} added to portfolio.")
        self.clear_inputs()

    def remove_stock(self):
        symbol = self.remove_input.text()
        if self.portfolio.remove_stock(symbol):
            QMessageBox.information(self, "Stock Removed", f"{symbol} removed from portfolio.")
        else:
            QMessageBox.warning(self, "Stock Not Found", f"{symbol} not found in portfolio.")
        self.remove_input.clear()

    def update_stock_price(self):
        symbol = self.update_symbol_input.text()
        price = self.fetch_stock_price(symbol)
        if price:
            if self.portfolio.update_stock_price(symbol, price):
                QMessageBox.information(self, "Price Updated", f"Updated price for {symbol} to ${price:.2f}")
                self.update_portfolio_value()
            else:
                QMessageBox.warning(self, "Stock Not Found", f"{symbol} not found in portfolio.")

    def show_portfolio(self):
        portfolio_data = self.portfolio.display_portfolio()
        total_value = self.portfolio.get_total_value()
        self.total_value_label.setText(f"Total Portfolio Value: ${total_value:.2f}")
        QMessageBox.information(self, "Portfolio", portfolio_data)

    def update_portfolio_value(self):
        total_value = self.portfolio.get_total_value()
        self.total_value_label.setText(f"Total Portfolio Value: ${total_value:.2f}")

    def clear_inputs(self):
        self.symbol_input.clear()
        self.shares_input.clear()
        self.price_input.clear()
        self.update_symbol_input.clear()


# Run the app
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = StockTrackerApp()
    window.show()
    sys.exit(app.exec_())