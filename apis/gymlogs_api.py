import requests

BASE_URL = "http://127.0.0.1:8000"

def create_week():
    response = requests.post(url=f"{BASE_URL}/gym/weeks")
    if response.status_code == 200:
        return response.json()
    
    return {"message" : "Unable to create new week"}

def fetch_week():
    response = requests.get(url=f"{BASE_URL}/gym/weeks")
    if response.status_code == 200:
        return response.json()
    return response.json()


def fetch_logs(week_number, workout_name):
    response = requests.get(url=f"{BASE_URL}/gym/weeks/logs",
                            params={"week_number" : week_number,
                                    "workout_name" : workout_name})
    if response.status_code == 200:
        return response.json()
    
def add_logs(week_number, workout_type,workout_name, weight, reps, set):
    response = requests.post(url=f"{BASE_URL}/gym/weeks/logs",
                             json={"workout_type" : workout_type,
                                   "workout_name" : workout_name,
                                   "weight" : weight,
                                   "reps" : reps,
                                   "set" : set},
                             params={"week_number" : week_number})
    if response.status_code == 200:
        return response.json()
    
def update_logs(id,workout_type,workout_name,weight,reps,set):
    response = requests.put(url=f"{BASE_URL}/gym/weeks/logs",
                            params={"id" : id},
                            json={"workout_type" : workout_type,
                                  "workout_name" : workout_name,
                                  "weight" : weight,
                                  "reps" : reps,
                                  "set" : set})
    if response.status_code == 200:
        return response.json()

def delete_logs(id):
    response = requests.delete(url=f"{BASE_URL}/gym/weeks/logs",
                               params={"id" : id})
    if response.status_code == 200:
        return response.json()


# ------------------------------------------------------------------------



