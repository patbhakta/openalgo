# US Market Broker Integration Guide

This guide explains how OpenAlgo has been modified to support US market brokers including Interactive Brokers, Alpaca, and Polygon.io.

## Overview

OpenAlgo uses a plugin-based broker system where:
- Broker configurations are stored in `broker/{broker_name}/plugin.json`
- Broker API implementations are in the `openalgo` Python package (v1.0.45)
- The system dynamically imports broker modules: `broker.{broker_name}.api.order_api`

## US Broker Support

### 1. Interactive Brokers (IB)

**Directory:** `broker/interactive_brokers/`

**API Implementation Location:** The actual broker code needs to be added to the `openalgo` package.

**Setup Requirements:**
1. Install TWS (Trader Workstation) or IB Gateway
2. Enable ActiveX/Socket clients
3. Configure port: 7497 (paper) or 7496 (live)
4. Add to .env file:
   ```
   IB_GATEWAY_HOST=127.0.0.1
   IB_GATEWAY_PORT=7497
   IB_CLIENT_ID=1
   ```

**Trading Features:**
- Stock and Options trading
- Market, Limit, Stop, Stop-Limit orders
- Bracket orders
- Real-time market data

### 2. Alpaca

**Directory:** `broker/alpaca/`

**Setup Requirements:**
1. Create account at alpaca.markets
2. Get API keys from dashboard
3. Add to .env file:
   ```
   ALPACA_API_KEY=your_api_key
   ALPACA_API_SECRET=your_api_secret
   ALPACA_BASE_URL=https://paper-api.alpaca.markets
   ```

**Trading Features:**
- Commission-free trading
- Paper and live trading
- Real-time market data via WebSocket
- Historical data API

### 3. Polygon.io

**Directory:** `broker/polygon/`

**Setup Requirements:**
1. Sign up at polygon.io
2. Get API key
3. Add to .env file:
   ```
   POLYGON_API_KEY=your_api_key
   ```

**Data Features:**
- Real-time quotes
- Historical market data
- Aggregated bars (OHLCV)
- Trades and quotes data

## Symbol Format

### US Markets
- Stocks: Simple symbol (e.g., AAPL, TSLA, MSFT)
- Options: Underlying + Date + Strike + Type (e.g., AAPL25011700150000C)
- Crypto: Symbol with prefix (e.g., X:BTCUSD)

### Indian Markets (Existing)
- Stocks: Exchange format (e.g., RELIANCE, INFY)
- F&O: Symbol format (e.g., NIFTY 50, BANKNIFTY)

## Exchange Mapping

Added US exchanges to `utils/constants.py`:
- NYSE (New York Stock Exchange)
- NASDAQ
- AMEX (American Stock Exchange)
- ARCA (NYSE Arca)
- BATS

## Product Type Mapping

Added US product types:
- CASH (Cash account)
- MARGIN (Margin account)
- BRACKET (Bracket order)
- OCO (One-Cancels-Other)
- DAY (Day order)

## Order Type Mapping

Added US order types:
- MARKET (Market Order)
- LIMIT (Limit Order)
- SL (Stop Loss Limit)
- SL-M (Stop Loss Market)
- STOPLIMIT (Stop Limit Order - US specific)
- TRAILING (Trailing Stop Order - US specific)

## Docker Deployment

The modifications are Docker-compatible. To deploy to VPS:

1. Build Docker image:
   ```bash
   docker build -t openalgo-us:latest .
   ```

2. Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Environment variables:
   - Copy `docker-compose.yaml` and modify environment variables
   - Ensure broker credentials are set

## Testing

Test US broker integrations:

1. **Interactive Brokers:**
   ```bash
   python -c "from ibapi.client import EClient; print('IB SDK installed')"
   ```

2. **Alpaca:**
   ```bash
   python -c "from alpaca.trading.client import TradingClient; print('Alpaca SDK installed')"
   ```

3. **Polygon:**
   ```bash
   python -c "from polygon import RESTClient; print('Polygon SDK installed')"
   ```

## Next Steps

To complete the implementation:

1. **Add Broker API Code:** The actual broker implementation code needs to be added to the `openalgo` Python package. You may need to fork/extend the openalgo package.

2. **Frontend Updates:** Update the React frontend to include US brokers in the broker selection dropdown.

3. **Documentation:** Add broker-specific setup guides to the documentation.

4. **Testing:** Thoroughly test each broker integration with paper trading accounts.

## Files Modified

1. `requirements.txt` - Added US broker SDKs
2. `utils/constants.py` - Added US exchanges and product types
3. `broker/interactive_brokers/` - Created plugin directory
4. `broker/alpaca/` - Created plugin directory
5. `broker/polygon/` - Created plugin directory

## Additional Resources

- Interactive Brokers API: https://www.interactivebrokers.com/en/trading/ibapi-starter.php
- Alpaca API: https://alpaca.markets/docs/
- Polygon API: https://polygon.io/docs/
- OpenAlgo Docs: https://docs.openalgo.in
