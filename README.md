# Mozio Backend (POSTGIS)

##

## Overview

In this Django project, I am using PostGIS to store the geometries of the polygons in the database. There is only one application named `main`. In the `main`, there are 3 urls with total 9 endpoints and 3 views. I really enjoyed exploring GIS and PostGIS. I was interested when I knew about it but never had the chance to use it. I tried to name the functions and classes as much elaborately as possible so that extra comments are not needed unless it is necessary. Also, I added cache functionality only in the `get` request of `Service Area` model because this is the model that can get heavier over the time. Here are the detailed endpoints:

##

## `Endpoints`

1. http://127.0.0.1:8000/api/v1/main/provider

   - `GET`:
     - Parameters: `id:int`
     - If greater than zero, it will return the provider with the given id. Else it will return all the providers.
   - `POST`:

     - Parameters: `name:str`, `email:str`, `phone_number:str`, `language:choices`, `currency:choices`.
     - > Language Choices:
       - `bn`: Bengali
       - `en`: English
       - `es`: Spanish
       - `fr`: French
       - `de`: German
       - `it`: Italian
       - `pt`: Portuguese
       - `ru`: Russian
       - `ja`: Japanese
       - `zh`: Chinese
     - > Currency Choices:

       - `bdt`: BDT
       - `usd`: USD
       - `eur`: EUR
       - `gbp`: GBP
       - `cny`: CNY
       - `jpy`: JPY
       - `rub`: RUB

     - Upon successful creation, it will return the newly created provider.

   - `DELETE`:
     - Parameters: `id:int`
     - It will delete the provider with the given id.
   - `PUT`:
     - Parameters: `id:int`, `name:str`/`email:str`/`phone_number:str`/`language:choices`/`currency:choices`
     - Upon successfully finding the provider, it will update the attribute with the given id.

2. http://127.0.0.1:8000/api/v1/main/service_area

   - `GET`:
     - Parameters: `id:int`
     - If greater than zero, it will return the service area with the given id. Else it will return all the service areas.
   - `POST`:

     - Parameters: `provider:int`, `name:str`, `price:float`, `location:PolygonField` .

     - Upon successful creation, it will return the newly created service area.

   - `DELETE`:
     - Parameters: `id:int`
     - It will delete the service area with the given id.
   - `PUT`:
     - Parameters: `id:int`, `provider:int`/`name:str`/`price:float`/`location:PolygonField`.
     - Upon successfully finding the service area, it will update the attribute with the given id.

3. http://127.0.0.1:8000/api/v1/main/check
   - `GET`:
     - Parameters: `lat:float`, `lng:float`
     - It will return all the service areas that contains the point.

##
