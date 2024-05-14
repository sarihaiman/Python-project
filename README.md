# Pyhtonfinalproject

## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Routes](#routes)

## About <a name = "about"></a>

A Basic Project for final Python Project

### Installing

Download this package, and then run:

```
pip install fastapi
```
and the server side runs!


## Usage <a name = "usage"></a>

Server Base URI:  <b>http://127.0.0.1:8000</b>
Use this Basic url with the correct route listed below 
see the api: <b>http://127.0.0.1:8000/docs</b>
אם
### Available routes <a name = "routes"></a>

### User Routes

#### Log In  

```http
  POST /user/login
```  
Response: User Object

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `name`                |  user name the user entered at login |
| `id`                  |  user id the user entered at login |
| `password`            |  user password the user entered at login |

#### Sign Up - create User  

```http
  POST /user/signUp
``` 
Response: User Object 

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user`                |  full user object with all parameters, includes name, id and password|

#### Update User

```http
  PUT /user
``` 
Response: User Object 

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user`                |  full user object with all parameters, includes username, id and password|

### BudgetManagment Routes

#### Get BudgetManagment of user

```http
  GET /budget?userid={user_id}
```

Response: Object of budgetManagment

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user_id`                | id of the user to get budgetManagment|

#### Create budgetManagment

```http
  POST /budget
```

Response: budgetManagment

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `expenses`                | Amount of expenses|
| `revenues`                | Amount of revenues|
| `userId`                  | id of the business|

#### Update budgetManagment

```http
  PUT /budget
```

Response: budgetManagment

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `budgetManagment`             | full budgetManagment object |

#### Delete budgetManagment

```http
  DELETE /budget
```

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `id`                | id of the user|

Response: budgetManagment
