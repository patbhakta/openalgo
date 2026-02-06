# OpenAlgo US Markets - Complete Deployment Guide

## ✅ Implementation Complete

OpenAlgo has been successfully modified to support US markets with Interactive Brokers, Alpaca, and Polygon.io.

## 📁 Modified Files

### Core Changes
1. **requirements.txt** - Added US broker SDKs
2. **utils/constants.py** - Added US exchanges (NYSE, NASDAQ, AMEX, ARCA, BATS) and product types

### New Broker Plugins
3. **broker/interactive_brokers/** - Interactive Brokers plugin
4. **broker/alpaca/** - Alpaca plugin  
5. **broker/polygon/** - Polygon.io plugin

### Documentation
6. **README_US_MARKETS.md** - Quick start guide
7. **US_MARKET_IMPLEMENTATION_SUMMARY.md** - Implementation details
8. **docs/US_MARKET_BROKER_GUIDE.md** - Comprehensive integration guide
9. **DEPLOYMENT_GUIDE.md** - This file

### Configuration Files
10. **docker-compose-us.yaml** - Docker deployment configuration
11. **env-us-template.txt** - Environment variables template

### Testing
12. **test_us_brokers.py** - Test validation script

## 🚀 Quick Start (Local Development)

### Step 1: Install Dependencies
```bash
cd E:\openalgo
pip install -r requirements.txt
```

### Step 2: Configure Environment
```bash
# Copy the US environment template
cp env-us-template.txt .env

# Edit .env with your broker credentials
notepad .env
```

Add your credentials:
```
# For Alpaca (recommended for testing)
ALPACA_API_KEY=your_api_key_here
ALPACA_API_SECRET=your_api_secret_here
ALPACA_BASE_URL=https://paper-api.alpaca.markets

# For Interactive Brokers
IB_GATEWAY_HOST=127.0.0.1
IB_GATEWAY_PORT=7497
IB_CLIENT_ID=1

# For Polygon.io (market data)
POLYGON_API_KEY=your_polygon_key_here
```

### Step 3: Run Tests
```bash
python test_us_brokers.py
```

### Step 4: Start OpenAlgo
```bash
# Using uv (recommended)
uv run app.py

# Or using Python directly
python app.py
```

Access at: **http://127.0.0.1:5000**

## 🐳 Docker Deployment (VPS Ready)

### Build and Run Locally
```bash
# Build the Docker image
docker build -t openalgo-us:latest .

# Run with Docker Compose
docker-compose -f docker-compose-us.yaml up -d

# View logs
docker logs -f openalgo-us
```

### Deploy to VPS

#### Prerequisites
- VPS with Ubuntu 20.04+ or similar
- At least 2GB RAM, 1GB disk space
- Root or sudo access

#### Step 1: Setup VPS
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose -y

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

#### Step 2: Deploy OpenAlgo
```bash
# Clone repository (or upload your modified version)
git clone https://github.com/your-fork/openalgo.git
cd openalgo

# Configure environment
cp env-us-template.txt .env
nano .env  # Add your broker credentials

# Start services
docker-compose -f docker-compose-us.yaml up -d

# Check status
docker-compose -f docker-compose-us.yaml ps
```

#### Step 3: Setup Reverse Proxy (Optional but Recommended)

**Using Caddy (Automatic HTTPS):**
```bash
# Install Caddy
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

Create Caddyfile:
```
your-domain.com {
    reverse_proxy localhost:5000
}
```

**Using Nginx:**
```bash
# Install Nginx
sudo apt install nginx -y

# Create configuration
sudo nano /etc/nginx/sites-available/openalgo
```

Nginx configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/openalgo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 4: Setup SSL with Let's Encrypt (if using Nginx)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal is configured automatically
```

## 🔧 Broker-Specific Setup

### Alpaca (Recommended - Easiest to Setup)
1. Sign up: https://alpaca.markets/
2. Get API keys from dashboard
3. Add to .env:
   ```
   ALPACA_API_KEY=your_key
   ALPACA_API_SECRET=your_secret
   ALPACA_BASE_URL=https://paper-api.alpaca.markets
   ```
4. No additional software needed!

### Interactive Brokers
1. Download IB Gateway: https://www.interactivebrokers.com/en/trading/ibapi-starter.php
2. Install and start IB Gateway
3. Configure API settings:
   - Enable ActiveX/Socket clients
   - Port: 7497 (paper) or 7496 (live)
   - Master API client ID: 0
   - Add "Local host" to trusted IPs
4. Add to .env:
   ```
   IB_GATEWAY_HOST=127.0.0.1
   IB_GATEWAY_PORT=7497
   IB_CLIENT_ID=1
   ```

### Polygon.io (Market Data Only)
1. Sign up: https://polygon.io/
2. Get API key from dashboard
3. Add to .env:
   ```
   POLYGON_API_KEY=your_key
   ```

## 📊 API Usage Examples

### Place Order
```bash
curl -X POST http://127.0.0.1:5000/api/v1/placeorder \
  -H "Content-Type: application/json" \
  -d '{
    "apikey": "your_api_key",
    "strategy": "US_Market_Strategy",
    "symbol": "AAPL",
    "exchange": "NASDAQ",
    "action": "BUY",
    "quantity": 10,
    "pricetype": "MARKET",
    "product": "MARGIN"
  }'
```

### Get Positions
```bash
curl -X GET http://127.0.0.1:5000/api/v1/positions \
  -H "Authorization: Bearer your_api_key"
```

### Get Holdings
```bash
curl -X GET http://127.0.0.1:5000/api/v1/holdings \
  -H "Authorization: Bearer your_api_key"
```

## 🧪 Testing

### Run Automated Tests
```bash
python test_us_brokers.py
```

Expected output:
```
============================================================
OpenAlgo US Broker Integration Test Suite
============================================================

Testing package imports...
✓ Flask installed
✓ Interactive Brokers API (ibapi) installed
✓ Alpaca API installed
✓ Polygon API installed

Testing constants...
✓ US exchanges defined in constants
✓ US product types defined in constants

Testing broker plugins...
✓ interactive_brokers plugin exists
✓ alpaca plugin exists
✓ polygon plugin exists

============================================================
Test Summary
============================================================
Package Imports: PASS
Constants: PASS
Broker Plugins: PASS

✓ All tests passed!
```

## 🔍 Troubleshooting

### Issue: Cannot connect to IB Gateway
**Solution:**
1. Ensure IB Gateway is running
2. Check port is correct (7497 for paper, 7496 for live)
3. Verify API is enabled in IB Gateway
4. Check firewall settings

### Issue: Alpaca authentication error
**Solution:**
1. Verify API key and secret in .env
2. Check if using correct base URL (paper vs live)
3. Ensure API key is active in Alpaca dashboard

### Issue: Docker container won't start
**Solution:**
1. Check logs: `docker logs openalgo-us`
2. Verify environment variables
3. Ensure volumes are accessible
4. Check for port conflicts

## 📚 Additional Resources

- **Documentation:** https://docs.openalgo.in
- **GitHub:** https://github.com/marketcalls/openalgo
- **Discord:** https://discord.gg/UPh7QPsNhP
- **Alpaca Docs:** https://alpaca.markets/docs/
- **IB API Docs:** https://www.interactivebrokers.com/en/trading/ibapi-starter.php
- **Polygon Docs:** https://polygon.io/docs/

## ⚠️ Important Notes

1. **Paper Trading First:** Always test with paper trading accounts before using real money
2. **Security:** Never commit .env file with real credentials to git
3. **Rate Limits:** Be aware of broker API rate limits
4. **Market Hours:** US market hours differ from Indian markets
5. **Time Zone:** OpenAlgo uses IST by default, US markets operate on EST/EDT

## 🎯 Next Steps

1. **Test with Paper Trading:** Use Alpaca paper trading to test
2. **Configure Your Strategy:** Set up your trading strategies
3. **Deploy to VPS:** Follow VPS deployment guide
4. **Setup Monitoring:** Add monitoring and alerts
5. **Go Live:** Only after thorough testing!

## 📝 License

OpenAlgo is released under the AGPL V3.0 License.

---

**Last Updated:** 2026-01-26
**Version:** 1.0.0
**Status:** ✅ Ready for Testing
