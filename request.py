import sys
import os

from venmo_api import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

access_token = os.environ['ACCESS_TOKEN']

venmo = Client(access_token=access_token)

name_to_username = {
  "Jane Doe": "Jane-Doe-123", # replace with real people
  "John Smith": "johnsmith456"
}

def get_user_id(username):
  user = venmo.user.get_user_by_username(username)
  if user:
    return user.id
  else:
    raise Exception(f"User {username} not found")

def send_money(username, amount, description):
  user_id = get_user_id(username)

  # Send money
  result = venmo.payment.send_money(amount, description, user_id)
  print(f"Sent ${amount} to {username} with description [{description}]", result)
  return True

def request_money(username, amount, description):
  user_id = get_user_id(username)

  # Request money
  result = venmo.payment.request_money(amount, description, user_id)
  print("Requested {} from {}".format(amount, username), result)
  return result

if __name__ == "__main__":
  names = sys.argv[1].split(',')
  amount = float(sys.argv[2])
  description = sys.argv[3]
  sendOrReceive = sys.argv[4]

  for name in names:
    if name not in name_to_username and not get_user_id(name_to_username[name]):
      raise Exception("Unknown name: {}".format(name))

  for name in names:
    if sendOrReceive == "send":
      send_money(name_to_username[name], amount, description)
    elif sendOrReceive == "request":
      request_money(name_to_username[name], amount, description)
    else: 
      raise Exception(f"Unknown sendOrReceive: {sendOrReceive}")
