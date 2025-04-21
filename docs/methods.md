TODO: Methods - Postman
########################## GET #########################
http://127.0.0.1:5000/categoria/

http://127.0.0.1:5000/categoria/

http://127.0.0.1:5000/categoria/1

########################## POST #########################
PASOS POST ADD
http://127.0.0.1:5000/categoria/

body->raw

{
    "cat_nombre": "New Product",
    "cat_obs": "New Obs"
}

########################## PUT #########################
PASOS PUT UPDATE
http://127.0.0.1:5000/categoria/3

body->raw

{
    "cat_nombre": "New Product Update",
    "cat_obs": "New Obs Update"
}

########################## DELETE #########################
PASOS DELETE
http://127.0.0.1:5000/categoria/4
