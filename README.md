
# Setup (before first request or payment)

1. Install
```
pipenv install
```
2. Acquire access_token
```
pipenv run python3 get_access_token.py [username] [password]
```
Note: username is often your phone number

3. Create a `.env` file by copying `.env.sample` and name the file `.env` 

4. Set the variable `ACCESS_TOKEN` with the access_token returned from step 2

5. Update `name_to_username` dictionary in `request.py` with a mapping of human-readable names to usernames. This will make it easier for you to make requests over time so you don't have to remember your friends' usernames.

# How to request money
```
pipenv run python3 request.py [name] [dollar amount] [description] request
```

# How to send money
```
pipenv run python3 request.py [name] [dollar amount] [description] send
```
