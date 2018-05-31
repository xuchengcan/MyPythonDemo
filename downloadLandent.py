import urllib.request
print ("downloading with urllib")
url = "https://raw.githubusercontent.com/getlantern/lantern-binaries/master/lantern-installer.exe"
#beiyong = "https://raw.githubusercontent.com/getlantern/lantern-binaries/master/"
f = urllib.request.urlopen(url) 
data = f.read() 
with open("C:/Users/chen/Desktop/MyPythonDemo/lantern-installer.exe", "wb") as code:
    code.write(data)