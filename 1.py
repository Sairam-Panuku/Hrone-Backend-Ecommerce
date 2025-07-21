
from urllib.parse import quote_plus

password = "Sairam@123"
encoded_password = quote_plus(password)
print(encoded_password)
