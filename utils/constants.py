"""
Constants used throughout the application.
Reference: https://docs.openalgo.in/api-documentation/v1/order-constants
"""

# Exchange Types - Indian Markets
EXCHANGE_NSE = "NSE"  # NSE Equity
EXCHANGE_NFO = "NFO"  # NSE Futures & Options
EXCHANGE_CDS = "CDS"  # NSE Currency
EXCHANGE_BSE = "BSE"  # BSE Equity
EXCHANGE_BFO = "BFO"  # BSE Futures & Options
EXCHANGE_BCD = "BCD"  # BSE Currency
EXCHANGE_MCX = "MCX"  # MCX Commodity
EXCHANGE_NCDEX = "NCDEX"  # NCDEX Commodity
EXCHANGE_NSE_INDEX = "NSE_INDEX"  # NSE Index
EXCHANGE_BSE_INDEX = "BSE_INDEX"  # BSE Index

# Exchange Types - US Markets
EXCHANGE_NYSE = "NYSE"  # New York Stock Exchange
EXCHANGE_NASDAQ = "NASDAQ"  # NASDAQ
EXCHANGE_AMEX = "AMEX"  # American Stock Exchange
EXCHANGE_ARCA = "ARCA"  # NYSE Arca
EXCHANGE_BATS = "BATS"  # BATS Global Markets
EXCHANGE_KALSHI = "KALSHI"  # Kalshi Prediction Market

VALID_EXCHANGES = [
    # Indian Exchanges
    EXCHANGE_NSE,
    EXCHANGE_NFO,
    EXCHANGE_CDS,
    EXCHANGE_BSE,
    EXCHANGE_BFO,
    EXCHANGE_BCD,
    EXCHANGE_MCX,
    EXCHANGE_NCDEX,
    EXCHANGE_NSE_INDEX,
    EXCHANGE_BSE_INDEX,
    # US Exchanges
    EXCHANGE_NYSE,
    EXCHANGE_NASDAQ,
    EXCHANGE_AMEX,
    EXCHANGE_ARCA,
    EXCHANGE_BATS,
    EXCHANGE_KALSHI,
]

# Product Types - Indian Markets
PRODUCT_CNC = "CNC"  # Cash & Carry for equity
PRODUCT_NRML = "NRML"  # Normal for futures and options
PRODUCT_MIS = "MIS"  # Intraday Square off

# Product Types - US Markets
PRODUCT_CASH = "CASH"  # Cash account
PRODUCT_MARGIN = "MARGIN"  # Margin account
PRODUCT_BRACKET = "BRACKET"  # Bracket order
PRODUCT_OCO = "OCO"  # One cancels other
PRODUCT_DAY = "DAY"  # Day order

VALID_PRODUCT_TYPES = [
    # Indian Product Types
    PRODUCT_CNC,
    PRODUCT_NRML,
    PRODUCT_MIS,
    # US Product Types
    PRODUCT_CASH,
    PRODUCT_MARGIN,
    PRODUCT_BRACKET,
    PRODUCT_OCO,
    PRODUCT_DAY,
]

# Price Types
PRICE_TYPE_MARKET = "MARKET"  # Market Order
PRICE_TYPE_LIMIT = "LIMIT"  # Limit Order
PRICE_TYPE_SL = "SL"  # Stop Loss Limit Order
PRICE_TYPE_SLM = "SL-M"  # Stop Loss Market Order
PRICE_TYPE_STOPLIMIT = "STOPLIMIT"  # Stop Limit Order (US)
PRICE_TYPE_TRAILING = "TRAILING"  # Trailing Stop Order (US)

VALID_PRICE_TYPES = [
    PRICE_TYPE_MARKET,
    PRICE_TYPE_LIMIT,
    PRICE_TYPE_SL,
    PRICE_TYPE_SLM,
    PRICE_TYPE_STOPLIMIT,
    PRICE_TYPE_TRAILING,
]

# Order Actions
ACTION_BUY = "BUY"  # Buy
ACTION_SELL = "SELL"  # Sell
ACTION_SHORT = "SHORT"  # Short (US Markets)
ACTION_COVER = "COVER"  # Cover Short (US Markets)

VALID_ACTIONS = [ACTION_BUY, ACTION_SELL, ACTION_SHORT, ACTION_COVER]

# Exchange Badge Colors (for UI)
EXCHANGE_BADGE_COLORS = {
    # Indian Exchanges
    EXCHANGE_NSE: "badge-accent",
    EXCHANGE_NFO: "badge-secondary",
    EXCHANGE_CDS: "badge-info",
    EXCHANGE_BSE: "badge-neutral",
    EXCHANGE_BFO: "badge-warning",
    EXCHANGE_BCD: "badge-error",
    EXCHANGE_MCX: "badge-primary",
    EXCHANGE_NCDEX: "badge-success",
    EXCHANGE_NSE_INDEX: "badge-accent",
    EXCHANGE_BSE_INDEX: "badge-neutral",
    # US Exchanges
    EXCHANGE_NYSE: "badge-primary",
    EXCHANGE_NASDAQ: "badge-secondary",
    EXCHANGE_AMEX: "badge-neutral",
    EXCHANGE_ARCA: "badge-info",
    EXCHANGE_BATS: "badge-accent",
    EXCHANGE_KALSHI: "badge-success",
}

# Required Fields for Order Placement
REQUIRED_ORDER_FIELDS = ["apikey", "strategy", "symbol", "exchange", "action", "quantity"]

# Required Fields for Smart Order Placement
REQUIRED_SMART_ORDER_FIELDS = [
    "apikey",
    "strategy",
    "symbol",
    "exchange",
    "action",
    "quantity",
    "position_size",
]

# Required Fields for Cancel Order
REQUIRED_CANCEL_ORDER_FIELDS = ["apikey", "strategy", "orderid"]

# Required Fields for Cancel All Orders
REQUIRED_CANCEL_ALL_ORDER_FIELDS = ["apikey", "strategy"]

# Required Fields for Close Position
REQUIRED_CLOSE_POSITION_FIELDS = ["apikey", "strategy"]

# Required Fields for Modify Order
REQUIRED_MODIFY_ORDER_FIELDS = [
    "apikey",
    "strategy",
    "symbol",
    "action",
    "exchange",
    "orderid",
    "product",
    "pricetype",
    "price",
    "quantity",
    "disclosed_quantity",
    "trigger_price",
]

# Default Values for Optional Fields
DEFAULT_PRODUCT_TYPE = PRODUCT_MIS
DEFAULT_PRICE_TYPE = PRICE_TYPE_MARKET
DEFAULT_PRICE = "0"
DEFAULT_TRIGGER_PRICE = "0"
DEFAULT_DISCLOSED_QUANTITY = "0"
