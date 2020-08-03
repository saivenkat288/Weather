from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from configurations.config import weather_url_start,api_key,weather_url_end
from serializers.transformer import OutputTransformer
import requests
import json
import concurrent.futures

app = FastAPI()

#To accept city name as input, if user doesn't give any input by default it takes London as input
class Weather(BaseModel):
    city_name:Optional[str]="London"

#Method to hit endpoint of open weather map to get 5 days weather
def hitEndpoint(weather):
    final_url=weather_url_start+str(weather.city_name)+weather_url_end+str(api_key)
    response=requests.post(final_url,data=weather.city_name,headers={"Content-Type":"application/json"})
    return response
#route is weather
@app.post("/weather")
#creating instance of Weather class
def getWeather(weather:Weather):
    #Hitting open weather map endpoint in seperate thread to achieve MultiTasking
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(hitEndpoint,weather)
        response= future.result()
    data=response.json()
    #Error Handling if open weather api is not
    if response.status_code!=200:
        res_json=OutputTransformer().error_handling_transformer()
        return res_json
    #If success, writing output to a file
    else:
        with open('./output/result.json', 'w') as f:
            json.dump(data, f)
        return data