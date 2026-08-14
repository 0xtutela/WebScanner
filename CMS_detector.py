import requests

def scan(url):

    global found
    fingerprints = {"/wp-json/wp/v2/" : "Wordpress", "/core/install.php" : "Drupal",
                "/administrator/manifests/files/joomla.xml" : "Joomla", "/manager/assets/modext/modx.js" : "Modex", "/checkout" : "Shopify",
                "/tildacdn.com" : "Tildcdn", "/index.php?route=common/home" : "Opencart", "/admin/index.php?route=common/login" : "Opencart",
                "/errors/local.xml.sample" : "Magento"}
    footprints = {"rest_cannot_access": "Wordpress", "Drupal": "Drupal", "<author>Joomla!": "Joomla",
                          "<extension>": "Joomla", "MODx.": "Modex", "Shopify.checkout": "Shopify",
                          "tildcdn.com": "Tildcdn", "catalog/view/theme/": "Opencart", "route=common/login": "Opencart",
                          "<config>": "Magento", "<layout>": "Magento"}
    for fingerprint in fingerprints.keys():
        request = requests.get(url + fingerprint, allow_redirects=False, timeout=10)
        found = False
        for footprint in footprints.keys():
            if footprint in request.text:
                print(footprints.get(footprint) + ": Avaliable")
                found = True

        if not found:
            print(fingerprints[fingerprint] + ": Not Avaliable")


    request = requests.get(url + "/bitrix/services/main/ajax.php", allow_redirects=False, timeout=10)
    if request.status_code == requests.codes.ok or request.status_code == 403:
        print("CMS: Bitrix")