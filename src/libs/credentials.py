import re
from getpass import getuser
# This library is created for project merlin.
# This library is licensed under the GNU GPLv3 

def addHttp(url) -> str:
	# Check if the url contains http or https
	if "https://" in url or "http://" in url:
		return url
	else:
		url = list(url)
		url.insert(0,"https://")
		url = "".join(url)
		return url
def checkMail(mail) -> bool:
	mailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if re.fullmatch(mailRegex, mail):
		return True
	else:
		return False

def passwd(password) -> None:
	reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&/])[A-Za-z\d@$!#%*?&/]{6,20}$"
	comp = re.compile(reg)
	passwordRegex = re.search(comp, password)
	if passwordRegex:
		pass
	else:
		exit("The password you entered is not secure. Exiting.")

def checkUser() -> str:
	defaultUser = getuser()
	return defaultUser

# TODO: fix the special character thing
# TODO: Add e-mail regex:: check
# TODO: Add password regex:: check
