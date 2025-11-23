def timer(funct):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        funct(*args, **kwargs)
        print(f'{funct.__name__} ran in {time() - start} seconds')
    return wrapper

import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# create a binary tree...
def generate_tree(num_nodes):
    if num_nodes == 0:
        return None
    value = random.randint(1, num_nodes)
    left_size = random.randint(0, num_nodes - 1)
    right_size = num_nodes - 1 - left_size
    return Node(value, generate_tree(left_size), generate_tree(right_size))

node = generate_tree(90000)  # generate a binary tree with 1000 nodes


a = dict.fromkeys('hello', 14)
print(a)
print(a.pop('e'))
a.clear()

print(a)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Optional: Set your API key in an environment variable
# os.environ["SENDGRID_API_KEY"] = 'your_api_key_here'

message = Mail(
    from_email='udemezue@gmail.com',
    to_emails='udemezue@gmail.com',
    subject='Hello from SendGrid',
    html_content='<strong>This is a test email sent via SendGrid</strong>'
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(f"Status Code: {response.status_code}")
    print(f"Body: {response.body}")
    print(f"Headers: {response.headers}")
except Exception as e:
    print(f"Error: {e}")
