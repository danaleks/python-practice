import requests
import json

def inspect_request(url, method='GET', data=None, headers=None):
    """
    Makes HTTP request and shows complete information
    """
    print(f"\n{'='*42}")
    print(f"HTTP {method} Request Inspector")
    print(f"{'='*42}\n")
    
    try:
        # Prepare request
        request_headers = headers or {}
        
        # Make request based on method
        if method == 'GET':
            response = requests.get(url, headers=request_headers, timeout=5)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=request_headers, timeout=5)
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=request_headers, timeout=5)
        elif method == 'DELETE':
            response = requests.delete(url, headers=request_headers, timeout=5)
        else:
            print(f"Unsupported method: {method}")
            return
        
        # REQUEST DETAILS
        print("REQUEST SENT:")
        print(f"   Method: {method}")
        print(f"   URL: {url}")
        
        if data:
            print(f"   Body: {json.dumps(data, indent=6)}")
        
        print(f"\n   Headers:")
        for key, value in response.request.headers.items():
            print(f"      {key}: {value}")
        
        # RESPONSE DETAILS
        print(f"\nRESPONSE RECEIVED:")
        
        # Status
        status_marker = "[OK]" if 200 <= response.status_code < 300 else "[REDIRECT]" if 300 <= response.status_code < 420 else "[ERROR]"
        print(f"   Status: {status_marker} {response.status_code} {response.reason}")
        
        # Timing
        print(f"   Response Time: {response.elapsed.total_seconds():.3f} seconds")
        
        # Headers
        print(f"\n   Response Headers:")
        important_headers = ['content-type', 'content-length', 'server', 'date', 'cache-control']
        for key, value in response.headers.items():
            marker = "*" if key.lower() in important_headers else " "
            print(f"      {marker} {key}: {value}")
        
        # Body
        print(f"\n   Response Body:")
        try:
            # Try to parse as JSON
            body_json = response.json()
            print(f"      {json.dumps(body_json, indent=6, ensure_ascii=False)[:500]}...")
        except:
            # If not JSON, show as text
            print(f"      {response.text[:300]}...")
        
        # ANALYSIS
        print(f"\nANALYSIS:")
        print(f"   Protocol: HTTP/{response.raw.version // 10}.{response.raw.version % 10}")
        print(f"   Encoding: {response.encoding}")
        print(f"   Cookies: {len(response.cookies)} cookie(s)")
        
        if response.is_redirect:
            print(f"   Redirect: Yes -> {response.headers.get('Location')}")
        
        return response
        
    except requests.exceptions.Timeout:
        print(f"Timeout: server did not respond within 5 seconds")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error: could not connect to {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def compare_methods(url):
    """
    Compares different HTTP methods on the same URL
    """
    print("\n" + "="*42)
    print("Comparing HTTP Methods")
    print("="*42)
    
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    results = {}
    
    for method in methods:
        print(f"\n--- Testing {method} ---")
        test_data = {'test': f'{method}_data', 'timestamp': 'now'}
        response = inspect_request(url, method, data=test_data)
        
        if response:
            results[method] = {
                'status': response.status_code,
                'time': response.elapsed.total_seconds()
            }
    
    # Summary
    print("\n" + "="*42)
    print("SUMMARY:")
    print("="*42)
    for method, data in results.items():
        print(f"   {method:6} -> Status: {data['status']}, Time: {data['time']:.3f}s")

def main():
    print("=" * 42)
    print("HTTP Request Inspector v2.0")
    print("=" * 42)
    
    while True:
        print("\nMenu:")
        print("  1. Inspect GET request")
        print("  2. Inspect POST request")
        print("  3. Compare all methods (GET/POST/PUT/DELETE)")
        print("  4. Custom request")
        print("  5. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            url = input("URL: ").strip()
            if not url.startswith('http'):
                url = 'https://' + url
            inspect_request(url, 'GET')
            
        elif choice == '2':
            url = input("URL: ").strip()
            if not url.startswith('http'):
                url = 'https://' + url
            
            print("Data to send (JSON):")
            print("Example: {\"name\": \"test\", \"value\": 123}")
            data_str = input("Data: ").strip()
            
            try:
                data = json.loads(data_str) if data_str else {"test": "data"}
            except:
                print("Invalid JSON, using test data")
                data = {"test": "data"}
            
            inspect_request(url, 'POST', data=data)
            
        elif choice == '3':
            print("\nUsing httpbin.org for testing...")
            compare_methods("https://httpbin.org/anything")
            
        elif choice == '4':
            url = input("URL: ").strip()
            if not url.startswith('http'):
                url = 'https://' + url
            
            method = input("Method (GET/POST/PUT/DELETE): ").strip().upper()
            
            if method in ['POST', 'PUT']:
                data_str = input("Data (JSON): ").strip()
                try:
                    data = json.loads(data_str) if data_str else None
                except:
                    data = None
            else:
                data = None
            
            inspect_request(url, method, data=data)
            
        elif choice == '5':
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()