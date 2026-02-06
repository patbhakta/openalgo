# OpenAlgo US Markets - Quick Start

## Setup Steps

1. Install dependencies:
   pip install -r requirements.txt

2. Configure environment:
   cp env-us-template.txt .env
   # Edit .env with your broker credentials

3. Run tests:
   python test_us_brokers.py

4. Start OpenAlgo:
   python app.py

5. Access at: http://127.0.0.1:5000

## Docker Deployment

docker-compose -f docker-compose-us.yaml up -d
