# OpenAlgo - US Markets Support

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp env-us-template.txt .env
# Edit .env with your broker credentials
```

3. Run OpenAlgo:
```bash
uv run app.py
# or
python app.py
```

Access at: http://127.0.0.1:5000

## Supported US Brokers

### Interactive Brokers
- Install IB Gateway or TWS
- Enable ActiveX/Socket clients on port 7497 (paper) or 7496 (live)
- Update .env with your credentials

### Alpaca
- Create account at alpaca.markets
- Get API keys from dashboard
- Add credentials to .env

### Polygon.io
- Sign up at polygon.io
- Get API key from dashboard
- Add to .env

## Docker Deployment

```bash
docker-compose -f docker-compose-us.yaml up -d
```

## Symbol Formats

US Stocks: AAPL, TSLA, MSFT
US Options: AAPL25011700150000C
Crypto: X:BTCUSD

## API Example

```bash
curl -X POST http://127.0.0.1:5000/api/v1/placeorder \
  -H "Content-Type: application/json" \
  -d '{
    "apikey": "your_key",
    "strategy": "Test",
    "symbol": "AAPL",
    "exchange": "NASDAQ",
    "action": "BUY",
    "quantity": 10,
    "pricetype": "MARKET",
    "product": "MARGIN"
  }'
```

## Testing

Run the test suite:
```bash
python test_us_brokers.py
```

## Troubleshooting

See US_MARKET_BROKER_GUIDE.md for detailed troubleshooting.
