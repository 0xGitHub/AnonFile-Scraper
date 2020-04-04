import string
import random
import proxy_requests
import threading
import sys

def id_generator(size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def build_url():
    base_url = "https://anonfile.com/"
    file_id = id_generator(10)
    final_url = base_url + file_id
    return final_url

def check_url(outfile):
    try:
        url = build_url()
        request = proxy_requests.ProxyRequests(url)
        request.get()
        if request.get_status_code() == 200:
            print(url)
            handle = open(outfile, 'a')
            handle.write(url+'\n')
        else:
            print("Nope. Response Code: "+request.get_status_code())
    except Exception as e:
        print(e)
        return

try:
    threads = int(sys.argv[1])
    for x in range(threads):
         threading.Thread(target=check_url).start()
except Exception as e:
    print(f"{sys.argv[0]} [threads]\n")
