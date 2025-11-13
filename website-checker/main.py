# first_program.py

import requests
from datetime import datetime

def save_results(url, status, filename="check_history.txt"):
    """Saving check results to the file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_text = "+ works" if status else "x unavalable"
    
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {url} - {status_text}\n")

def check_website(url):
    """Checking site accesability"""
    print(f"Checking {url}...")
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"+ {url} works! (code {response.status_code})")
            print(f"   Time of response: {response.elapsed.total_seconds():.2f} sec")
            save_results(url, True)  # НОВОЕ: сохраняем результат
            return True
        else:
            print(f"! {url} returned code {response.status_code}")
            save_results(url, False)  # НОВОЕ
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"x {url} unavalable")
        print(f"   Reason: {e}")
        save_results(url, False)  # НОВОЕ
        return False

def show_history():
    """Shows the checks history"""
    try:
        with open("check_history.txt", 'r', encoding='utf-8') as f:
            print("\n=== Check history ===")
            print(f.read())
    except FileNotFoundError:
        print("\n History is empty")

def main():
    print("=== Checking site accesability ===")
    print("Comands: URL for checking, 'history' to see request history, 'quit' to exit\n")
    
    while True:
        user_input = input("Enter the command: ").strip()
        
        if user_input.lower() == 'quit':
            print("Bye! ")
            break
        
        if user_input.lower() == 'history':
            show_history()
            print()
            continue
        
        url = user_input
        if not url.startswith('http'):
            url = 'https://' + url
        
        check_website(url)
        print()

if __name__ == "__main__":
    main()