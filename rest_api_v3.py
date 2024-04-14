from aiohttp import web
import json
from sqlalchemy import create_engine, Integer, Column, String, CHAR, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Drink(Base):

    __tablename__ = 'drink'

    id = Column( "id", Integer, primary_key=True)
    name = Column("name", String(50))
    description = Column("description", String(50))

    def __int__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"({self.id}) {self.name} -- {self.description}"



engine = create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


## Initial DB Entries
# d1 = Drink(name='Cola', description='tastes like cola')
# d2 = Drink(name='grapes', description='tastes like grapes')
# session.add_all([d1,d2])
# session.commit()
# result = session.query(Drink).all()
# print(result)




async def get_drinks(request):

    drinks = session.query(Drink).all()
    output = []

    for drink in drinks :
        drink_data = { 'name' : drink.name, 'description' : drink.description}
        output.append(drink_data)

    return web.Response(text=json.dumps({"drinks" : output}), status=200)


## ID on API endpoint
async def get_drink(id):
    # Use match_info.get() contains URL placeholder values of {id}, and also the sam at start ({id}.match..)
    drink = session.query(Drink).filter_by(id=id.match_info.get('id')).first()
    drink_data = {'name': drink.name, 'description': drink.description}

    return web.Response(text=json.dumps(drink_data), status=200)



async def add_drinks(request):
    try:
        # Use below code to take json as input from postman
        data = await request.json()
        # Below to get input from query builder
        # drinks = Drink(name=request.query['name'], description=request.query['description'])
        drinks = Drink(name=data['name'], description=data['description'])
        session.add(drinks)
        session.commit()
        response_obj = {'status': 'success', 'message': 'drink successfully added'}
        return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'error': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)



async def delete_drink(id):
    drink = session.query(Drink).filter_by(id=id.match_info.get('id')).first()
    if drink is None:
        response_obj = {'error' : 'not found'}
        return web.Response(text=json.dumps(response_obj), status=404)
    session.delete(drink)
    session.commit()
    response_obj = { 'message' : 'yeet!@'}
    return web.Response(text=json.dumps(response_obj), status=200)




# Creating aiohttp web application
app = web.Application()

app.router.add_get('/drinks', get_drinks)
app.router.add_get('/drinks/{id}', get_drink)
app.router.add_post('/drinks', add_drinks)
app.router.add_delete('/drinks/{id}', delete_drink)



if __name__ == '__main__':
    web.run_app(app)



