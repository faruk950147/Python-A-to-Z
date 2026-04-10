import requests
url = "https://www.cricbuzz.com/"

response = requests.get(url)

# get request with status code
# print(response.status_code)

# get request with status code ok
# print(response.status_code == requests.codes.ok)

# get request with text
# print(response.text)

# get request with headers
# print(response.headers)

# get request with content
# print(response.content)

# get request with json
# print(response.json())

# get request with url
# print(response.url)

# get request with history
# print(response.history)

# get request with elapsed time
# print(response.elapsed)

# get request with request
# print(response.request)

# get request with cookies
# print(response.cookies)

# get request with raw
# print(response.raw)

# using response.raw
# print(response.raw.read())


# using loop
for key, value in response.headers.items():
    print(f"Key: {key}, <-------> Value: {value}")
    