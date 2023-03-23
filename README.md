# library-API

**● How to use :**
# Getting the tokens :

1. to test the API open postman software.
2. make POST requests to /api/register/ with Json content :
```bash
{
    "username": "someone",
    "password": "strongPassword",
    "password2": "strongPassword",
    "email": "someone@something.com",
    "first_name": "someone",
    "last_name": "something"
}
```
3. make POST request to /api/token/ with Json content:
```bash
{
    "username": "someone",
    "password": "strongPassword"
}
```
4. copy your access token which is valid for one day and has to be refreshed using the refresh token.
5. TO refresh the access token make POST request to /api/token/refresh/ with Json content:
```bash
{
    "refresh": "YourRereshToken",
}
```
> This refresh token is valid as long as you are using the app once in a week. If not you have to sign in again.

**Summary:**

| Root | Method | Content | Headers | Response |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| [/api/token/](https://library-api-mustafa.herokuapp.com/api/token/)  | POST | username, password | No Headers | refresh, access Tokens |
| [/api/token/refresh/](https://library-api-mustafa.herokuapp.com/api/token/refresh/)  | POST | refresh token | No Headers | new access token, refresh token |
| [api/register/](https://library-api-mustafa.herokuapp.com/api/register/) | POST | username, password, password2, email, first_name, last_name | No Headers | 201 created |
> examples for Non Headers end points.. [see](https://github.com/mustafamordaa1/library-API/tree/main#getting-the-tokens-)
# playing with the Data :
> Note : in all the following requsts **You have to** include the access token in the authorization header, see the example below.
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0MjEyMDA5LCJpYXQiOjE2NjQxMjU2MDksImp0aSI6IjUwMWU4NjA4OGQyYTRmYjliOTA5NjcxYzIwNmI1Yzg0IiwidXNlcl9pZCI6MX0.a3oVrCh5S0AGoLKEvltuPmRCKTJy-h1praIausRorKI
```
1. To list All the books make GET request to /api/books/ the response would be like that :
```bash
[
    {
        "id": 2,
        "title": "The Hunger Games",
        "isbn": "439023483",
        "author": "Suzanne Collins",
        "year": 2008,
        "rate": 4.34,
        "image": "https://images.gr-assets.com/books/1447303603m/2767052.jpg"
    },

    ....
]
```
> **You can also add books using POST request, the content would be in the same format as the response but without brackets [ .. ] and accepts only one book for each request.**

2. To view one book details make GET request to /api/books/book_id and the response would be like :
```bash
{
    "id": 39,
    "title": "The Time Traveler's Wife",
    "isbn": "965818675",
    "author": "Audrey Niffenegger",
    "year": 2003,
    "rate": 3.95,
    "image": "https://images.gr-assets.com/books/1437728815m/14050.jpg"
}
```
> **You can also make PUT and DELETE requests.**

3. To view all the borrowed books make GET request to /api/borrow/
```bash
[
    {
        "user": {
            "id": 3,
            "username": "brianj",
            "first_name": "Brian",
            "last_name": "Juicy",
            "email": "brian@juicy.com"
        },
        "book": [
            {
                "id": 8,
                "title": "The Hobbit or There and Back Again",
                "isbn": "618260307",
                "author": "J.R.R. Tolkien",
                "year": 1937,
                "rate": 4.25,
                "image": "https://images.gr-assets.com/books/1372847500m/5907.jpg"
            },
            {
                "id": 9,
                "title": "The Catcher in the Rye",
                "isbn": "316769177",
                "author": "J.D. Salinger",
                "year": 1951,
                "rate": 3.79,
                "image": "https://images.gr-assets.com/books/1398034300m/5107.jpg"
            },
            {
                "id": 10,
                "title": "Angels & Demons ",
                "isbn": "1416524797",
                "author": "Dan Brown",
                "year": 2000,
                "rate": 3.85,
                "image": "https://images.gr-assets.com/books/1303390735m/960.jpg"
            }
        ],
        "date": "2022-09-23",
        "expDate": "2022-09-30"
    },

    ...

]
```
4. You can borrow books by making POST request to /api/borrow/, the content should be like :
```bash
   {
       "user": 3,
       "book": ["93", "62", "74"],
       "date": "2022-09-23",
       "expDate": "2022-09-30"
   }
```
