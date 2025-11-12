#  Website Checker

Простая программа на Python для проверки доступности веб-сайтов.

##  What does it do:

-  Checks accesability
-  Checks answer timeing
-  Saves checks log
-  Interactive tool

## Launch instruction

### Requirements
- Python 3.7+
- lib `requests`

### Установка
```bash
# clone rep
git clone https://github.com/YOUR-USERNAME/python-practice.git
cd python-practice

# install dependencies
pip install requests

# Launch
python first_program.py
```

## Example
```
=== Checking site accesability ===
Comands: URL for checking, 'history' to see request history, 'quit' to exit

Enter the command: google.com
Checking https://google.com...
+ https://google.com works! (code 200)
   Time of response: 0.55 sec

Enter the command: www.umb.sk
Checking https://www.umb.sk...
+ https://www.umb.sk works! (code 200)
   Time of response: 0.20 sec

Enter the command: www.notexist.sk
Checking https://www.notexist.sk...
x https://www.notexist.sk unavalable
   Reason: HTTPSConnectionPool(host='www.notexist.sk', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x74746233c590>: Failed to resolve 'www.notexist.sk' ([Errno -2] Name or service not known)"))

Enter the command: quit
Bye! 
```

## What I learned here

- Practice with `requests`
- HTTP requests&server answers practice
- How Python works with files
- Building an interactive CLI program
- Usage of Git and GitHub


## Additional comment

My 1st project for my Python repository and portfolio. Built for studying and practicing purpose

---

**Created in** 12 november 2025
The funi day huh?