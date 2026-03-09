import sys
import requests

def brute(site,wordlist):
    for word in wordlist:
        try:
            site_final = "{}/{}".format(site,word.strip())
            response = requests.get(site_final)
            code = response.status_code
            if code != 404:
                print("{} -- {}".format(site_final,code))
        
        except KeyboardInterrupt:
            sys.exit(0)
        
        except Exception as error:
            print(error)
            pass

if __name__ == "__main__":
    site = sys.argv[1]
    wordlist = sys.argv[2]

    with open (wordlist, "r") as file:
        wordlist = file.readlines()
        brute(site,wordlist)