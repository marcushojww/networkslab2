# Networks Lab 2 - REST API

Marcus Ho Jun Wei 1004271

## Setup

Make sure you have [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed. I used VSCode as my editor of choice for this lab.

Run `docker-compose up` and make sure you see a pink background UI with the title "Welcome to the Dating App Users Database!" by going to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Walkthrough

The `.http` files are located in the `checkoff` folder and they are named `delete_requests.http`, `get_requests.http` and `post_requests.http` respectively. 

With VSCode as the IDE of choice and the installed extension named REST Client, you would be able to send each request declared within the `.http` files. The response of each request would also be displayed after a request is submitted.

### Part 1 - Let's POST

As the database is empty, let's head over to the `post_requests.http` to fire the POST requests as listed below to the route `http://127.0.0.1:8000/users` and create our Dating App users. Also, there's a request header parameter named `password` which serves as the authorization for POST requests and in this case, the `password` assigned for successful authorization is `123`.

```
### Create male Marcus user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Marcus",
    "id": 0,
    "gender": "M",
    "height_in_cm": 180,
    "looking_for": "F",
    "bio": "Last time I was someone's type, I was donated blood."
}

### Create male Justin user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Justin",
    "id": 1,
    "gender": "M",
    "height_in_cm": 182,
    "looking_for": "F",
    "bio": "Here for a good time, not a long time."
}

### Create male Victor user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Victor",
    "id": 2,
    "gender": "M",
    "height_in_cm": 175,
    "looking_for": "F",
    "bio": "I'm Marcus's dad lol."
}

### Create female Yong Qing user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Yong Qing",
    "id": 3,
    "gender": "F",
    "height_in_cm": 162,
    "looking_for": "M",
    "bio": "Current relationship status: Made dinner for two. Ate both."
}

### Create female Alice user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Alice Cheng",
    "id": 4,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
}

### Create dog user
POST http://127.0.0.1:8000/users HTTP/1.1
Content-Type: application/json
password: 123

{
    "name": "Mocha",
    "id": 5,
    "gender": "M",
    "height_in_cm": 101,
    "looking_for": "F",
    "bio": "Will do anything for treats."
}
```

### Part 2 - Let's GET

Now, let's head over to `get_requests.http` and retrieve our data. 

**Please take note that the id field of each user will be randomly generated hence, the response from the GET requests may differ.**

GET request with no query parameters
```
### Get all users
GET http://127.0.0.1:8000/users HTTP/1.1
```

Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 11:47:51 GMT
server: uvicorn
content-length: 783
content-type: application/json
connection: close

[
  {
    "name": "Yong Qing",
    "id": 93509,
    "gender": "F",
    "height_in_cm": 162,
    "looking_for": "M",
    "bio": "Current relationship status: Made dinner for two. Ate both."
  },
  {
    "name": "Victor",
    "id": 471982,
    "gender": "M",
    "height_in_cm": 175,
    "looking_for": "F",
    "bio": "I'm Marcus's dad lol."
  },
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  },
  {
    "name": "Marcus",
    "id": 81203,
    "gender": "M",
    "height_in_cm": 180,
    "looking_for": "F",
    "bio": "Last time I was someone's type, I was donated blood."
  },
  {
    "name": "Justin",
    "id": 219921,
    "gender": "M",
    "height_in_cm": 182,
    "looking_for": "F",
    "bio": "Here for a good time, not a long time."
  },
  {
    "name": "Mocha",
    "id": 788053,
    "gender": "M",
    "height_in_cm": 101,
    "looking_for": "F",
    "bio": "Will do anything for treats."
  }
]
```

GET request with a `sortBy` query parameter to transform the order of the items returned
```
### Get users sorted by height
GET http://127.0.0.1:8000/users?sortBy=height_in_cm HTTP/1.1
```
Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 11:52:41 GMT
server: uvicorn
content-length: 783
content-type: application/json
connection: close

[
  {
    "name": "Mocha",
    "id": 788053,
    "gender": "M",
    "height_in_cm": 101,
    "looking_for": "F",
    "bio": "Will do anything for treats."
  },
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  },
  {
    "name": "Yong Qing",
    "id": 93509,
    "gender": "F",
    "height_in_cm": 162,
    "looking_for": "M",
    "bio": "Current relationship status: Made dinner for two. Ate both."
  },
  {
    "name": "Victor",
    "id": 471982,
    "gender": "M",
    "height_in_cm": 175,
    "looking_for": "F",
    "bio": "I'm Marcus's dad lol."
  },
  {
    "name": "Marcus",
    "id": 81203,
    "gender": "M",
    "height_in_cm": 180,
    "looking_for": "F",
    "bio": "Last time I was someone's type, I was donated blood."
  },
  {
    "name": "Justin",
    "id": 219921,
    "gender": "M",
    "height_in_cm": 182,
    "looking_for": "F",
    "bio": "Here for a good time, not a long time."
  }
]
```
GET request with a `count` query parameter to limit the number of items returned
```
### Get users with limit 3
GET http://127.0.0.1:8000/users?count=3 HTTP/1.1
```
Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 12:02:43 GMT
server: uvicorn
content-length: 400
content-type: application/json
connection: close

[
  {
    "name": "Yong Qing",
    "id": 93509,
    "gender": "F",
    "height_in_cm": 162,
    "looking_for": "M",
    "bio": "Current relationship status: Made dinner for two. Ate both."
  },
  {
    "name": "Victor",
    "id": 471982,
    "gender": "M",
    "height_in_cm": 175,
    "looking_for": "F",
    "bio": "I'm Marcus's dad lol."
  },
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  }
]
```
GET request with a `offset` query parameter to to "skip" ahead by a number of items
```
GET http://127.0.0.1:8000/users?offset=2 HTTP/1.1
```
Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 11:59:16 GMT
server: uvicorn
content-length: 523
content-type: application/json
connection: close

[
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  },
  {
    "name": "Marcus",
    "id": 81203,
    "gender": "M",
    "height_in_cm": 180,
    "looking_for": "F",
    "bio": "Last time I was someone's type, I was donated blood."
  },
  {
    "name": "Justin",
    "id": 219921,
    "gender": "M",
    "height_in_cm": 182,
    "looking_for": "F",
    "bio": "Here for a good time, not a long time."
  },
  {
    "name": "Mocha",
    "id": 788053,
    "gender": "M",
    "height_in_cm": 101,
    "looking_for": "F",
    "bio": "Will do anything for treats."
  }
]
```
GET request with a combination of the above query parameters
```
### Get users sorted by name, count and offset
GET http://127.0.0.1:8000/users?sortBy=height_in_cm&count=2&offset=1 HTTP/1.1
```
Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 12:04:10 GMT
server: uvicorn
content-length: 140
content-type: application/json
connection: close

[
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  }
]
```

### Part 3 - Let's DELETE

Now, let's head over to `delete_requests.http` and delete a user based on their specified `id`.

**Please take note that you may view the user id based on `id` field of the users retrieved above. It is important to know the available user ids to test the DELETE request**

Before DELETE request, the users available are as follows:
```
[
  {
    "name": "Yong Qing",
    "id": 93509,
    "gender": "F",
    "height_in_cm": 162,
    "looking_for": "M",
    "bio": "Current relationship status: Made dinner for two. Ate both."
  },
  {
    "name": "Victor",
    "id": 471982,
    "gender": "M",
    "height_in_cm": 175,
    "looking_for": "F",
    "bio": "I'm Marcus's dad lol."
  },
  {
    "name": "Alice Cheng",
    "id": 991526,
    "gender": "F",
    "height_in_cm": 159,
    "looking_for": "M",
    "bio": "I'm Marcus's mom. Just here to expose my son."
  },
  {
    "name": "Marcus",
    "id": 81203,
    "gender": "M",
    "height_in_cm": 180,
    "looking_for": "F",
    "bio": "Last time I was someone's type, I was donated blood."
  },
  {
    "name": "Justin",
    "id": 219921,
    "gender": "M",
    "height_in_cm": 182,
    "looking_for": "F",
    "bio": "Here for a good time, not a long time."
  },
  {
    "name": "Mocha",
    "id": 788053,
    "gender": "M",
    "height_in_cm": 101,
    "looking_for": "F",
    "bio": "Will do anything for treats."
  }
]
```

Now, let's try to delete user **Justin** with the `id` **219921**.
```
### Delete user based on specified user id
DELETE http://127.0.0.1:8000/users/219921 HTTP/1.1
```
Expected response:
```
HTTP/1.1 200 OK
date: Wed, 06 Oct 2021 12:10:27 GMT
server: uvicorn
content-length: 53
content-type: application/json
connection: close

"User id: 219921 successfully deleted from database."
```
We've successfully deleted the user with the `id` 219921 so this id should not exist in our database.
Let's try deleting a user with the `id` 219921 again which should not work.
Expected response:
```
HTTP/1.1 500 Internal Server Error
date: Wed, 06 Oct 2021 12:12:04 GMT
server: uvicorn
content-length: 58
content-type: application/json
connection: close

"User id: 219921 not found in database. Please try again."
```
### Part 4 - Two Challenges Completed

**Challenge 1: Have a route in your application that returns a content type that is not plaintext**

Heading to [http://127.0.0.1:8000](http://127.0.0.1:8000) will return a HTML response rather than the usual plaintext.

**Challenge 2: Some form of authorization through inspecting the request headers**

As seen from **Part 1** where we begin POSTing requests, we will begin to inspect the POST request headers first to see if the `password` header parameter matches the assigned `password` in the function before validating the request.

## Routes which are idempotent

All the GET and DELETE routes are idempotent. The GET and DELETE routes are idempotent as these requests can be made once or several times in a row with the same effect while leaving the server in the same state. For example, submitting the request `GET http://127.0.0.1:8000/users HTTP/1.1` multiple times would not alter the state of the server. Similarly, for `DELETE` request such as `DELETE http://127.0.0.1:8000/users/219921 HTTP/1.1`, the first request would remove the user with the specified id from the database but subsequent requests would not change the state of the server as the user id no longer exists.

## Analysis on performance
I chose to store the users in a hashset with the user_id as the field to improve the time complexity in retrieving a user from the database. It would be O(1) in time as compared to traversing through a set of users to find the matching user_id which would take O(n) time complexity.
