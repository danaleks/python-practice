import requests

def inspect_request(url, method='GET'):
    """
    Makes HTTP request and shows details
    """
    print(f"\n{'='*50}")
    print(f"Inspecting: {method} {url}")
    print(f"{'='*50}\n")
    
    try:
        # Make request
        if method == 'GET':
            response = requests.get(url, timeout=5)
        elif method == 'POST':
            response = requests.post(url, json={'test': 'data'}, timeout=5)
        
        # REQUEST INFO
        print("REQUEST:")
        print(f"   Method: {method}")
        print(f"   URL: {url}")
        print(f"   Headers sent:")
        for key, value in response.request.headers.items():
            print(f"      {key}: {value}")
        
        # RESPONSE INFO
        print(f"\nRESPONSE:")
        print(f"   Status Code: {response.status_code} {response.reason}")
        print(f"   Time: {response.elapsed.total_seconds():.3f} sec")
        
        print(f"\n   Headers received:")
        for key, value in response.headers.items():
            print(f"      {key}: {value}")
        
        print(f"\n   Body preview (first 200 chars):")
        print(f"   {response.text[:200]}...")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Test different sites
if __name__ == "__main__":
    print("=== HTTP Request Inspector ===")
    
    # GET request
    inspect_request("https://httpbin.org/get", "GET")
    
    # POST request
    inspect_request("https://httpbin.org/post", "POST")