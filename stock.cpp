// infy, tcs

#include <iostream>
#include <string>
#include <unordered_map> 
#include <iomanip>       

using namespace std;

// Struct to represent stock information
struct Stock {
    int shares;   
    double price; 
};

// Unordered Map for portfolio storage
unordered_map<string, Stock> portfolio; 
// Key: Stock symbol (e.g., "AAPL")

void addStock(const string &symbol, int shares, double price) {
    portfolio[symbol] = {shares, price}; // Insert or update stock details
    cout << "Stock added/updated: " << symbol << endl;
}

void removeStock(const string &symbol) {
    if (portfolio.find(symbol) != portfolio.end()) {
        portfolio.erase(symbol); // Remove stock
        cout << "Stock removed: " << symbol << endl;
    } else {
        cout << "Stock not found: " << symbol << endl;
    }
}

void displayPortfolio() {
    if (portfolio.empty()) {
        cout << "Portfolio is empty." << endl;
        return;
    }

    cout << "Portfolio:" << endl;
    double totalValue = 0.0;

    // Iterate through the unordered_map to display stock details
    for (const auto &entry : portfolio) {
        const string &symbol = entry.first;
        const Stock &stock = entry.second;
        double stockValue = stock.shares * stock.price; 
        totalValue += stockValue;

        
        cout << fixed << setprecision(2);
        cout << "Symbol: " << symbol 
             << ", Shares: " << stock.shares 
             << ", Price: $" << stock.price 
             << ", Value: $" << stockValue << endl;
    }

    
    cout << "Total Portfolio Value: $" << totalValue << endl;
}

int main() {
    int choice;
    do {
        cout << "\nPortfolio Manager\n";
        cout << "1. Add/Update Stock\n";
        cout << "2. Remove Stock\n";
        cout << "3. Display Portfolio\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                string symbol;
                int shares;
                double price;

                
                cout << "Enter stock symbol: ";
                cin >> symbol;
                cout << "Enter number of shares: ";
                cin >> shares;
                cout << "Enter price per share: ";
                cin >> price;

                addStock(symbol, shares, price); 
                break;
            }
            case 2: {
                string symbol;

                
                cout << "Enter stock symbol to remove: ";
                cin >> symbol;

                removeStock(symbol); 
                break;
            }
            case 3:
                displayPortfolio(); 
                break;
            case 4:
                cout << "Exiting portfolio manager." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);

    return 0;
}
