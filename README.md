# pyconng2024
This helps you understand mitmproxy to an extent. It will spur your interest and allow you to grow.

# Assumptions
- You are on a Linux kernel OS e.g. Ubuntu
- You have all the API credentials in your environment
- You have a cloudinary account
- You have mitmproxy active by copying what's inside the `processes.txt` to run on the terminal

# How to use
1. Create a virtualenv, activate it and `pip install -r requirements.txt`
2. `firstone.py` helps you to upload the file
3. `investigate.py` helps you call the upload to see the JSON
4. `routes.py` works to help you see what's being thrown to the API route. You need mitmproxy active.
