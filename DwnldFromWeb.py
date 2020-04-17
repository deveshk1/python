# read from requests.readthedocs.org
#request module is 3rd party to download file from web
import requests

responseFromWebServer = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(responseFromWebServer.status_code)  # just to check status
print(len(responseFromWebServer.text))
# print(responseFromWebServer.text[:500])

# to check success

print(responseFromWebServer.raise_for_status())
# NON, no error
# wb = write-binary
PlayFile = open('D:\\RomeoAndJuliet.txt', 'wb')
# to write content to file

for chunk in responseFromWebServer.iter_content(10000000):
    PlayFile.write(chunk)
PlayFile.close()
