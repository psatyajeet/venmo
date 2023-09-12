import sys

from venmo_api import Client

# Get your access token. You will need to complete the 2FA process
def get_access_token(username, password):
  return Client.get_access_token(username=username,
                                          password=password)
  

if __name__ == "__main__":
  username = sys.argv[1]
  password = sys.argv[2]

  token = get_access_token(username, password)
  print(token)
  