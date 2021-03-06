import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200 :
        raise RuntimeError(f'error code{res.status_code}')
    return res

def password_convert_check(password):
    hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    res = request_api_data(hash_password[0:5])
    count= check_count(res,hash_password[5:])
    if count == 0:
        print(password+' is safe to use')
    else :
        print(f'{password} is hacked {count} times')

def check_count(res,tail_pass):
    hw = (line.split(':') for line in res.text.splitlines())
    for tail, count in hw:
        if tail == tail_pass:
            return count
    return 0    
    
def check_password():
    while True:
        print(''' 1.Check Password \n 2.Exit \n Enter your option:''', end='')
        op = input()
        if int(op) == 2:
            break
        print('Enter password : ', end='')
        password = input()
        password_convert_check(password)
    print('Thanks')

if __name__ == "__main__":
    check_password()

