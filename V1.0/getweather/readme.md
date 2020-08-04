PreRequisites:
   -Python 3.x
   -Install all the dependency packages using "pip install -r requirements.txt"

Running Project:
   -Run project using "uvicorn weather:app --reload --port <port>"
   -Hit endpoint "http://localhost:<port>/weather" with a post method in any REST clients like postman, curl 
   -You can find postman collection in the scripts folder, Import it in postman and start hitting!
   -Result will be stored in "result.json" file in output folder or you can find response in the postman      response space itself.

Additional Info:
   -REST style of API is made using FASTAPI framework
   -Inside my api, Iam hitting api of "open weather app" to get response
   -If you need to hit different endpoint, you can change url of endpoint in config.py in configurations folder.