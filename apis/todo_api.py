import requests
import os 
from dotenv import load_dotenv

load_dotenv()   # loads the env variables
BASE_URL = os.getenv("BASE_URL")

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    return response.json()

def create_todo(todo_detail):
    response = requests.post(
        f"{BASE_URL}/todos",
        json={
            'todo_detail' : todo_detail
        }
    )
    return response.json()

def update_todo(todo_id,todo_detail):
    response = requests.put(
        f"{BASE_URL}/todos",
        params= {'todo_id': todo_id},
        json={
            'todo_detail' : todo_detail
        }
    )
    return response.json()

def delete_todo(todo_id):
    response = requests.delete(
        f"{BASE_URL}/todos",
        params={'todo_id':todo_id}
    )
