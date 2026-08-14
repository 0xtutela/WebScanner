import requests

def scan(url):
    directories = ["/admin", "/login", "/uploads", "/config", "/backup", "/phpinfo.php"]

    files = ["robots.txt", "sitemap.xml"]
    for file in files:
        request = requests.get(url + file, allow_redirects=False, timeout=10)
        if request.status_code == 200:
            print(file + ": ✅")
        elif request.status_code == 404:
            print(file + ": ❌")
        elif request.status_code == 403:
            print(file + ": Access is forbidden")
        elif request.status_code == 301:
            print(file + ": returned status 301")

    for directory in directories:
        request = requests.get(url + directory, allow_redirects=False, timeout=10)
        if request.status_code == 200:
            print("\n" + directory + ": ✅")
        elif request.status_code == 404:
            print(directory + ": ❌")
        elif request.status_code == 403:
            print(directory + ": Access is forbidden")
        elif request.status_code == 301:
            print(directory + ": returned status 301")