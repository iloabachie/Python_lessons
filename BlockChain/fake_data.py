from faker import Faker
import sys
sys.path.append('BlockChain')

from chain_objects import Trader

# Create a Faker instance
fake = Faker()

# Function to generate a random trader
def generate_random_trader():
    name = fake.name()
    age = fake.random_int(min=18, max=80)
    location = fake.country()
    deposit = fake.random_int(min=100, max=1000)
    return Trader(name, age, location, deposit)

