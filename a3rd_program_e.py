# first_program.py

import requests

def check_website(url):
    """Checking website's accesability..."""
    print(f"Checking {url}...")
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"VV {url} works fine! (code {response.status_code})")
            print(f"   Answer time: {response.elapsed.total_seconds():.2f} sec")
            return True
        else:
            print(f"!! {url} returned code {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"XX {url} unaccesable")
        print(f"   Reason: {e}")
        return False

def main():
    print("=== Checking website's accesability... ===\n")
    
    while True:
        url = input("Enter URL (or 'quit' to exit): ").strip()
        
        if url.lower() == 'quit':
            print("Bye!")
            break
        
        # Adding https:// if user forgot to do so
        if not url.startswith('http'):
            url = 'https://' + url
        
        check_website(url)
        print()
if __name__ == "__main__":
    main()