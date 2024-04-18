headers = {
    "Content-Type": "application/json"
},
user_body = {
    user_body = get_user_body("Аа")
},

user_response = {
    user_response = sender_stand_request.post_new_user(user_body)
},

product_ids = {
    "ids": [1, 2, 3]
}