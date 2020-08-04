from config import weather_url_start,api_key,weather_url_end
from transformer import OutputTransformer
import requests
import json
import concurrent.futures
import logging
from colorama import Fore, Back, Style
class Weather:
    def hitEndpoint(city_name):
        final_url=weather_url_start+str(city_name)+weather_url_end+str(api_key)
        response=requests.post(final_url,data=city_name,headers={"Content-Type":"application/json"})
        return response
    def getWeather(city_name):
        #Hitting open weather map endpoint in seperate thread to achieve MultiTasking
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(hitEndpoint,city_name)
            response= future.result()
        data=response.json()
        #Error Handling if open weather api is not success
        if response.status_code!=200:
            res_json=OutputTransformer().error_handling_transformer()
            print(res_json)
        #If success, writing output to a file
        else:
            with open('./result.json', 'w') as f:
                json.dump(data, f)
            print(Back.GREEN+"Check result.json file in output folder to view result")
            print(data)