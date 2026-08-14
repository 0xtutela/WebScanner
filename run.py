import directories_detector
import connection_scan
import headers_detector
import CMS_detector

def main():
    art = """




        █████                 █████                █████             ████           
      ███░░░███              ░░███                ░░███             ░░███           
     ███   ░░███ █████ █████ ███████   █████ ████ ███████    ██████  ░███   ██████  
    ░███    ░███░░███ ░░███ ░░░███░   ░░███ ░███ ░░░███░    ███░░███ ░███  ░░░░░███ 
    ░███    ░███ ░░░█████░    ░███     ░███ ░███   ░███    ░███████  ░███   ███████ 
    ░░███   ███   ███░░░███   ░███ ███ ░███ ░███   ░███ ███░███░░░   ░███  ███░░███ 
     ░░░█████░   █████ █████  ░░█████  ░░████████  ░░█████ ░░██████  █████░░████████
       ░░░░░░   ░░░░░ ░░░░░    ░░░░░    ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░  ░░░░░░░░                                                             



 
    """
    print(art)
    print("Scan Website y or n?")
    answer = input()
    if answer == "y":
        print("Input your website:")
        url = input()

        connection_scan.scan(url)
        headers_detector.scan(url)
        directories_detector.scan(url)
        CMS_detector.scan(url)

    elif answer == "n":
        exit()
main()