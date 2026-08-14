import requests

def scan(url):

    request = requests.get(url, stream=True, timeout=5)
    headers = request.headers
    headers_list = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    print("\n")

    for header in headers_list:
        if header in headers:
            i = headers.get(header)
            print(header, ": " + "✅")
        elif header not in headers:
            print(header, ": ❌")

    print("\n")