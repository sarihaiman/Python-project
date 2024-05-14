## PythonFinalProject!

### Project Overview

Our goal is to provide a seamless backend infrastructure for the "Balance" application, allowing users to handle their expenses and income effortlessly. While backend development is our primary focus, frontend development will be handled by our frontend team.

### System Specification

- **Database:** MongoDB will manage our data efficiently.
- **Server-side:** We're using Python for server-side development.
- **Client-side:** React will power our client-side interface.

### Application Features

- **User Routes:** Includes registration, login, and profile update functionalities.
- **Expense and Income Routes:** Supports creation, update, deletion, and retrieval of expense and income data.
- **Visualization Route:** Allows users to extract data suitable for visualization using matplotlib.

### Quality Assurance

We're committed to delivering a high-quality product. Our developers will write comprehensive tests to ensure the system's performance meets our standards.

### Documentation

Quality documentation is crucial for maintaining transparency and ensuring future scalability. Detailed documentation, including design specifications and usage guidelines, can be found in the `docs` directory.

### Contribution

We welcome contributions and feedback! If you encounter any issues or
have suggestions for improvement, please don't hesitate to create an issue in the repository.

## Tree
├── app\
│   ├── Models\
│   │   ├── budgetManagment.py\
│   │   └── user.py\
│   ├── routes\
│   │   ├── budgetManagment_Router.py\
│   │   ├── user_Router.py\
│   │   └── visualization_Router.py\
│   ├── services\
│   │   ├── budgetManagment_services.py\
│   │   ├── user_services.py\
│   │   └── visualization_services.py\
│   └── db\
├── tests\
│   ├── user_test.py\
│   └── budgetManagment_test.py\
├── README.md\
├── requirements.txt\
└── main.py
 

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
