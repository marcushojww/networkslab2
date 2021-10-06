import pickle
import random
import json
from typing import Optional

import redis
from fastapi import Depends, FastAPI, Response, Header
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    id: int
    gender: str
    height_in_cm: int
    looking_for: str
    bio: Optional[str]


def get_redis_client():
    return redis.Redis(host="redis")

#POST: Add user
@app.post("/users")
def create_user(response: Response, user: User, password: str = Header(None), r: redis.Redis = Depends(get_redis_client)): 
    #Check if password is correct by inspecting request headers
    if (password != '123'):
        response.status_code = 401
        return "Unauthorized access. Please key in the password again."
    #Generate unique user id
    user_id = random.randint(1,1000000)
    while r.hexists("/users", user_id):
        user_id = random.randint(1,1000000)
    user.id = user_id
    #Add to hash set
    r.hset("/users", f'{user_id}', pickle.dumps(user))
    response.status_code = 200

#GET: Home page
@app.get("/", response_class=HTMLResponse)
def read_root(r: redis.Redis = Depends(get_redis_client)):
    return """
        <html>
            <head>
                <title>Dating Users Database</title>
            </head>
            <body style="background-color:#F7CAC9">
                <h1 style="text-align:center;margin-top: 50px">
                    Welcome to the Dating App Users Database!
                </h1>
                <h4 style="text-align:center">
                    Query, delete, or set up your profile today!
                </h4>
                <div style="display:flex;justify-content:center">
                    <img src="https://i.pinimg.com/originals/80/6c/1a/806c1ad90a0fb4eabde59ef58206c7e8.png" style="width: 300px">
                    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6017b074-6684-40e4-a369-97529c5c8640/dd5r4o6-cba29562-cd8c-41aa-8701-356390110b37.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzYwMTdiMDc0LTY2ODQtNDBlNC1hMzY5LTk3NTI5YzVjODY0MFwvZGQ1cjRvNi1jYmEyOTU2Mi1jZDhjLTQxYWEtODcwMS0zNTYzOTAxMTBiMzcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.sXH_oW7Cckxrbm5M2jckUEzl9b2gMsjyvUUztLYgKmU" style="width: 300px">
                    <img src="https://64.media.tumblr.com/ee5e3e246c2813745f2a46c7466dd29b/tumblr_pb605zmPoj1wizutho1_1280.png" style="width: 350px">
                </div>
            </body>
        </html>
    """

#GET: Get users
@app.get("/users")
def get_all_users(response: Response, r: redis.Redis = Depends(get_redis_client), sortBy: Optional[str] = None, count: Optional[int] = None, offset: Optional[int] = None):

    users_array = [pickle.loads(user) for user in r.hvals("/users")]

    #Sorting function
    if sortBy:
        if sortBy == "name":
            users_array.sort(key=lambda x: x.name)
        elif sortBy == "gender":
            users_array.sort(key=lambda x: x.gender)
        elif sortBy == "height_in_cm":
            print("entered here")
            users_array.sort(key=lambda x: x.height_in_cm)
        elif sortBy == "looking_for":
            users_array.sort(key=lambda x: x.looking_for)
        elif sortBy == "bio":
            users_array.sort(key=lambda x: x.bio)

    #Limit number of items based on count
    if count and count <= len(users_array):
        count_array = []
        for i in range(count):
            count_array.append(users_array[i])
        users_array = count_array  
    #Return empty array if count equals to 0
    elif count == 0:
        response.status_code = 200
        return []

    #Skip ahead of items based on offset
    if offset and offset < len(users_array):
        users_array = users_array[offset:]
    #Return an empty array if offset is more than or equal than the length of the list
    elif offset and offset >= len(users_array):
        return []           

    response.status_code = 200
    return users_array


#GET: Get users based on their id
@app.get("/users/{user_id}")
def get_user_by_id(response: Response, user_id: int, r: redis.Redis = Depends(get_redis_client)):
    if r.hexists("/users", user_id):
        user = pickle.loads(r.hget(f'/users', f'{user_id}'))
        return user
    else:
        response.status_code = 500
        return f'User id: {user_id} not found in database. Please try again.'
        

#GET: Get all user ids
@app.get("/ids")
def get_all_user_ids(r: redis.Redis = Depends(get_redis_client)):
    user_ids = r.hkeys("/users")
    return user_ids

#DELETE: Delete user based on user id
@app.delete("/users/{user_id}")
def delete_user_by_id(response: Response, user_id: int, r: redis.Redis = Depends(get_redis_client)):
    #Delete user data if user id exist in database
    if r.hexists("/users", user_id):
        r.hdel(f'/users', user_id)
        response.status_code = 200
        return f'User id: {user_id} successfully deleted from database.'
    else:
        response.status_code = 500
        return f'User id: {user_id} not found in database. Please try again.'
            
    