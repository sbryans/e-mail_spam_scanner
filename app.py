import requests
from bs4 import BeautifulSoup

print("Enter an e-mail address:")

email = input()
request = requests.get("https://cleantalk.org/email-checker/"+email)
content = request.content
soup = BeautifulSoup(content, "html.parser")
object = soup.find("span", {"text-warning"})
if object is None:
        print(email + " looks like a clean e-mail address.")
else:
        output = (object.text.strip())
        print(output)

# "None" type comes back in the "object" if the e-mail does not show up in the CleanTalk database because the html tag & class pair are not found after parsed.
