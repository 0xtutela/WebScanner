import requests

def scan(url):
    directories = ["/admin", "/login", "/uploads", "/config", "/backup", "/phpinfo.php"]

    files = ["robots.txt", "sitemap.xml"]
    for file in files:
        request = requests.get(url + file, allow_redirects=False, timeout=10)
        if request.status_code == 200 or request.status_code == 403:
            print(file + " is avaliable")
        else:
            print(file + " is not avaliable")

    for directory in directories:
        request = requests.get(url + directory, allow_redirects=False, timeout=10)
        if request.status_code == 200 or request.status_code == 403:
            print(directory + " is avaliable\n")
        if request.status_code == 404:
            print(directory + " is not avaliable\n")