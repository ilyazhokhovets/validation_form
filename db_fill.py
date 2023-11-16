from tinydb import TinyDB

db = TinyDB('database.json')


RECORDS = [

    {
        "name": "Order Form",
        "lead_email": "email",
        "lead_phone": "phone"
    },

    {
        "name": "Delivery Form",
        "delivery_date": "date",
        "courier_phone": "phone",
        'additional_info': "text"
    },

    {
        "name": "Best Company",
        "CEO_email": "email",
        "CEO_phone": "phone"
    },

    {
        "name": "Biography Form",
        "user_name": "text",
        "biography": "text"
    },

    {
        "name": "CV Form",
        "soft_skills": "text",
        "user_phone": "phone",
        "user_email": "email",
        "birthday": "date"
    },

    {
        "name": "School Form",
        "student_name": "text",
        "student_email": "email",
    },

]

db.truncate()
for record in RECORDS:
    db.insert(record)