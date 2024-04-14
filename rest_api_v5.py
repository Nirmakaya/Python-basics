from sqlalchemy import MetaData,Table, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from aiohttp import web
import pandas as pd
import numpy as np
import json



engine = create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

people_table = Table("people", metadata, autoload=True)



app = web.Application()

async def get_people(request):
    people_data = session.query(people_table).all()
    # output = []
    # for row in people_data:
    #     data = {"firstname":row['firstname'],
    #             "gender": row['gender'],
    #             "age": row['age']}
    #     output.append(data)
    # Or use the below code for simplification
    user_data = [{"firstname": user.firstname, "gender": user.gender, "age": user.age} for user in people_data]
    return web.Response(text=json.dumps(user_data), status=200)


async def get_people_data(name):

    people = session.query(people_table).filter_by(firstname=name.match_info.get('name')).first()
    if people is None:
        # using json_response() instead of Response.json.dumps() to return json
        return web.json_response({"error":"Invalid request"})
    people_data = {"ssn": people['ssn'],
                "firstname":people.firstname,
               "lastname":people.lastname,
                "gender": people.gender,
                "age": people.age}
    return web.Response(text=json.dumps(people_data), status=200)



# Api method of below datatype would be POST
async def process_data(request):
    data = await request.json()
    df = pd.DataFrame(data['data'])
    print(df.head(5))
    mean_data = df.apply(lambda x: np.mean(x), axis=0)
    print(mean_data)
    # here to_dict() is used to convert int to dict
    return web.json_response({"mean": mean_data.to_dict()})
## Input :{
#     "data": [
#         [1,4,6,7,4,8,2,1,50],
#         [7,8,6,7,4,8,20,1,5],
#         [5,4,60,7,4,8,2,2,50]
#     ]
# }



async def add_people(request):
    try:
        data = await request.json()
        # Adding a new user to existing Database, data.get('ssn') is used, instead of data['ssn']
        # Although both can be used
        ssn = data['ssn']
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        gender = data.get('gender')
        age = data.get('age')

        #Check for null entries
        if ssn is None or firstname is None or lastname is None or gender is None or age is None:
            # using json_response() instead of Response.json.dumps() to return json
            return web.json_response({"error":"Invalid request"})

        # Here new sql_alchemy function of insert().values() and execute() is used
        # to save a new entries to DB coming from user
        new_user = people_table.insert().values(ssn=ssn, firstname=firstname,lastname=lastname,gender=gender,age=age)
        session.execute(new_user)
        session.commit()
        response_obj = {"status":"pass", "message": "User {} is successfully added to people table".format(firstname)}

        return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {"status":"failed", "error": str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


# Under Construction
async def delete_people(name):
    people = session.query(people_table).filter_by(firstname=name.match_info.get('name')).first()
    if people is None:
        # using json_response() instead of Response.json.dumps() to return json
        return web.json_response({"error":"Invalid request"})
    firstname = people.firstname
    session.delete(people)
    session.commit()
    response_obj = {"status": "Success", "message": "User {} is successfully deleted".format(firstname)}
    return web.Response(text=json.dumps(response_obj), status=200)



app.router.add_get('/', get_people)
app.router.add_get('/{name}', get_people_data)
app.router.add_post('/mean', process_data)
app.router.add_post('/people', add_people)
# app.router.add_delete('/{name}', delete_people)



if __name__ == '__main__':
    web.run_app(app)
