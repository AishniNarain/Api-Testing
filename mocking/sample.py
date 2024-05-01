import requests
# from mocking.dice import roll_dice

# def guess_number(number):
#     result = roll_dice()
#     if result == number:
#         return "You Won!"
#     else:
#         return "You lost!"

# guess_number(1)

def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']
    
result = get_ip()
print(result)