from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table
from aiohttp import web
import json


## SQL orm steps : when new tables are created:-
# Base table
# engine
# session/server
# Migrate : to create things in db using engine

## SQL orm steps : when existing tables from DB are being used, Base table is not imported:-
# metadata
# engine
# session/server
# Table() construct is used


engine = create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)

# Import Metadata and Table from sqlalchemy
metadata = MetaData(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# Use parameter autoload=True to get existing table
dlp_fpp = Table('dlp_indent', metadata, autoload=True)


# Using web from aiohttp
app = web.Application()

async def get_dlp_fpp(request):
    dlp_table = session.query(dlp_fpp).all()
    output = []
    for row in dlp_table:
        dlp_table_data = {"node": row.plant_code,
                          "material_code": row.vc_code,
                          "feasible_production_quantity": row.feasible_prod_qty}
        output.append(dlp_table_data)
    return web.Response(text=json.dumps(output), status=200)


app.router.add_get("/fpp", get_dlp_fpp)


if __name__ == '__main__':
    web.run_app(app)
