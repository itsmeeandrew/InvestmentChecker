from tkinter import *
from yahooquery import Ticker
from windows.searchstock.add_stock import display_add_stock_window
from controllers.controllers import create_widget, config_widgets


def display_search_stock_window():
    root = Tk()
    root.title("Search Stock")
    root.config(padx="20", pady="10")

    def search_stock():
        nonlocal stock_ticker, stock_name, stock_currency, stock_currency_symbol
        stock_ticker = entry_stock_ticker_input.get()
        try:
            # Retrive and prepare stock data
            ticker = Ticker(stock_ticker)
            data = ticker.price[stock_ticker]

            stock_name = data["shortName"]
            stock_price = data["regularMarketPrice"]
            stock_currency = data["currency"]
            stock_currency_symbol = data["currencySymbol"]

            # Update stock related data
            label_stock_name_data.config(text=stock_name)
            label_regular_market_price_data.config(text=f"{stock_currency_symbol}{stock_price}")
            label_currency_data.config(text=stock_currency)

            # Enable add stock button
            btn_add_stock.config(state="normal")

        except:
            # Display "NOT FOUND" if the given stock ticker gives no data
            label_stock_name_data.config(text="NOT FOUND")
            label_regular_market_price_data.config(text="NOT FOUND")
            label_currency_data.config(text="NOT FOUND")

            # Disable add stock button
            btn_add_stock.config(state="disabled")

    # Stock related variables
    stock_ticker            = None
    stock_name              = None
    stock_currency          = None
    stock_currency_symbol   = None

    Labels = []
    Entries = []
    Buttons = []

    # Search related widgets
    label_basic_1 = create_widget("label", Labels, root, txt="Stock ticker: ", r=1, c=1)
    entry_stock_ticker_input = create_widget("entry", Entries, root, w=30, r=1, c=2)
    btn_search = create_widget("button", Buttons, root, txt="Search", comm=search_stock, r=1, c=3)

    # Create labels for data
    label_stock_name = create_widget("label", Labels, root, txt="Stock name:", r=2, c=1)
    label_regular_market_price = create_widget("label", Labels, root, txt="Regular Market Price:", r=3, c=1)
    label_currency = create_widget("label", Labels, root, txt="Currency:", r=4, c=1)

    label_stock_name_data = create_widget("label", Labels, root, txt="", r=2, c=2)
    label_regular_market_price_data = create_widget("label", Labels, root, txt="", r=3, c=2)
    label_currency_data = create_widget("label", Labels, root, txt="", r=4, c=2)

    # Create add stock button
    btn_add_stock = create_widget("button", Buttons, root, txt="Add to My Stocks",
                                  comm=lambda: display_add_stock_window(
                                      stock_ticker,
                                      stock_name,
                                      stock_currency,
                                      stock_currency_symbol),
                                  r=5, c=2, state="disabled")

    # Widget styling
    basic_config = {
        "font": "44",
    }

    config_widgets(widgets=Labels, basic_cfg=basic_config, additional_cfg={"padx": "8", "pady": "8"})
    config_widgets(widgets=Buttons, basic_cfg=basic_config, additional_cfg={"padx": "8", "pady": "8"})
    config_widgets(widgets=Entries, basic_cfg=basic_config)

    root.mainloop()
