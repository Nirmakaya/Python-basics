

#### INTRO

# REST API : Representational State Transfer, communicates with the web/internet

# API endpoint : whatever you what to do with API,
# API endpoint : eg /drinks/<id>, a web address
# API endpoint : Web server either has a IP address or a domain name, so with domain name, web adress becomes : favoritedrinks/drinks/<id>


# API Methods :  eg GET, POST, DELETE, PUT. Used for CRUD operations on DB
# CRUD Operation : Create(post), read, Update, delete
# GET : to get info
# POST : to write (used to write new data), used to add a resource. eg address: /drinks
# PUT : usually to update/append (but you can write too), used to update a resource. eg : /drinks/<id>
# PUT is designed to give same result everytime if made the same request, same ID again and again.
# First request :/drinks/605, Second :/drinks/605, Third: /drinks/605
# Hence PUT is called idempotent
# DELETE : to delete
# PATCH : used to change small part of resources/DB


# Why use APIs, 4 reasons:-
# Security : API also acts as protection, so if in a model in which users are directly communicating with DB,
# it puts the DB at risk, as source file is available on dev tools
# Versatility : same API can be used by many software.
# Modularity : We use Server>API>Client model because
# We may change BE write it in different language and point it to same API endpoint, and FE would be the same unaffected
# Interoperability : an API endpoint can be made public, and by this we don't have to worry about authentication
# and authorisation and any new app would consume the same PUBLIC APIs, anybody can use,
# For example : Instagram has public APIs endpoint so you may change the FE/Interface and use the publically available API endpoints
# We may use oauth2 for some to create some authorisation on public APIs


# Website : would have webpages that user use or APIs.
# Website : APIs can be either on subdirectory eg : favoritedrinks/API/drinks/<id>
# Website : or APIs can be on subdomain eg : api.favoritedrinks/drinks/<id>


# Query Parameters : /2.3/questions?order=desc&sort=activity&site=stackoverflow,
# in this the ?variable=value&variable=value&, used to modify results of APIs


# JSON : Java Script object notation, in API response we get JSON, just like in website we request HTML.


