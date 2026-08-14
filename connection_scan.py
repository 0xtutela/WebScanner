import requests
def scan(url):
    global request
    try:
        request = requests.get(url, stream=True, timeout=10)

    except requests.exceptions.ConnectionError:
        print("Connection error\n")
    except requests.exceptions.Timeout:
        print("Timeout error\n")
    except requests.exceptions.RequestException:
        print("Invalid url\n")

    print("Response Time:   ", request.elapsed, "\n" )

    if request.status_code == requests.codes.ok:
        print("url is working\n")
        print("SSL is alright!\n", request)
