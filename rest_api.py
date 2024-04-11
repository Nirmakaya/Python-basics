from aiohttp import web
# web for web module
import json
# For json responses


# GET API
async def handle(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj), status=200)



# POST API
async def new_user(request):
    try:
        # To collect name, from query parameter
        user = request.query['name']
        print("Creating a new user with name: ", user)
        response_obj = { 'status':'success', 'message':'user successfully created'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status':'failed', 'message': str(e)}
        # Setting status to 500, which is a bad or unsuccessful response
        return web.Response(text=json.dumps(response_obj), status=500)




# Defining Application
app = web.Application()
# registering base root with handle function : Base root would have a handle request
app.router.add_get('/', handle)
# For POST API
app.router.add_post('/user', new_user)

# Get the API running
web.run_app(app)



# In postman give the url
# For get request :  http://0.0.0.0:8080/
# For post request :  http://0.0.0.0:8080/user?name=Kia