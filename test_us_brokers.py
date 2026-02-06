#!/usr/bin/env python3
"""
Test script to validate US broker integrations for OpenAlgo
"""
import sys
import os

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing package imports...")
    
    # Test standard packages
    try:
        import flask
        print("✓ Flask installed")
    except ImportError:
        print("✗ Flask not installed")
        return False
    
    # Test Interactive Brokers
    try:
        from ibapi.client import EClient
        from ibapi.wrapper import EWrapper
        print("✓ Interactive Brokers API (ibapi) installed")
    except ImportError:
        print("✗ Interactive Brokers API (ibapi) not installed")
        print("  Install with: pip install ibapi")
    
    # Test Alpaca
    try:
        from alpaca.trading.client import TradingClient
        from alpaca.data.historical import StockHistoricalDataClient
        print("✓ Alpaca API installed")
    except ImportError:
        print("✗ Alpaca API not installed")
        print("  Install with: pip install alpaca-trade-api")
    
    # Test Polygon
    try:
        from polygon import RESTClient
        print("✓ Polygon API installed")
    except ImportError:
        print("✗ Polygon API not installed")
        print("  Install with: pip install polygon-api-client")
    
    # Test Kalshi
    try:
        import kalshi_python_sync
        print("✓ Kalshi API installed")
    except ImportError:
        print("✗ Kalshi API not installed")
        print("  Install with: pip install kalshi-python-sync")
    
    return True

def test_constants():
    """Test if US exchanges and products are defined"""
    print("
Testing constants...")
    
    try:
        from utils.constants import (
            EXCHANGE_NYSE, EXCHANGE_NASDAQ, EXCHANGE_AMEX, EXCHANGE_KALSHI,
            PRODUCT_CASH, PRODUCT_MARGIN, PRODUCT_BRACKET,
            VALID_EXCHANGES, VALID_PRODUCT_TYPES
        )
        
        # Check US exchanges
        assert EXCHANGE_NYSE in VALID_EXCHANGES, "NYSE not in VALID_EXCHANGES"
        assert EXCHANGE_NASDAQ in VALID_EXCHANGES, "NASDAQ not in VALID_EXCHANGES"
        assert EXCHANGE_KALSHI in VALID_EXCHANGES, "KALSHI not in VALID_EXCHANGES"
        print("✓ US exchanges (including Kalshi) defined in constants")
        
        # Check US product types
        assert PRODUCT_CASH in VALID_PRODUCT_TYPES, "CASH not in VALID_PRODUCT_TYPES"
        assert PRODUCT_MARGIN in VALID_PRODUCT_TYPES, "MARGIN not in VALID_PRODUCT_TYPES"
        print("✓ US product types defined in constants")
        
        return True
    except ImportError as e:
        print(f"✗ Could not import constants: {e}")
        return False
    except AssertionError as e:
        print(f"✗ Constants assertion failed: {e}")
        return False

def test_broker_plugins():
    """Test if broker plugin directories exist"""
    print("
Testing broker plugins...")
    
    brokers = ['interactive_brokers', 'alpaca', 'polygon', 'kalshi']
    
    for broker in brokers:
        plugin_path = f"broker/{broker}/plugin.json"
        if os.path.exists(plugin_path):
            print(f"✓ {broker} plugin exists")
        else:
            print(f"✗ {broker} plugin not found at {plugin_path}")
    
    return True

def test_env_variables():
    """Test if environment variables can be loaded"""
    print("
Testing environment variables...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check for US broker env variables
    us_brokers = {
        'IB_GATEWAY_HOST': 'Interactive Brokers',
        'ALPACA_API_KEY': 'Alpaca',
        'POLYGON_API_KEY': 'Polygon.io',
        'KALSHI_EMAIL': 'Kalshi'
    }
    
    for env_var, broker_name in us_brokers.items():
        value = os.getenv(env_var)
        if value:
            print(f"✓ {broker_name} environment variable set ({env_var})")
        else:
            print(f"○ {broker_name} environment variable not set ({env_var})")
    
    return True

def main():
    """Run all tests"""
    print("="*60)
    print("OpenAlgo US Broker Integration Test Suite")
    print("="*60)
    print()
    
    tests = [
        ("Package Imports", test_imports),
        ("Constants", test_constants),
        ("Broker Plugins", test_broker_plugins),
        ("Environment Variables", test_env_variables),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"
✗ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("
" + "="*60)
    print("Test Summary")
    print("="*60)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("
✓ All tests passed!")
        return 0
    else:
        print("
✗ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
