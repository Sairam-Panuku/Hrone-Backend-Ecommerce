from pymongo import MongoClient

uri = "mongodb+srv://sairampanuku:Sairam%40123@ecommerce.nwuoyeh.mongodb.net/?retryWrites=true&w=majority&appName=ecommerce&tls=true"

client = MongoClient(uri)
print(client.server_info())  # This will force a connection
