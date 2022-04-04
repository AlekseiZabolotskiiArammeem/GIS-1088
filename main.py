import os
import tempfile
import requests

#import catboost as cb
from fastapi import FastAPI
from fastapi.responses import JSONResponse
#from tortoise.contrib.fastapi import register_tortoise
import RandomForest2
#import services
#from config import get_settings
#from schemas import  HealthCheck , OrderPredictOut OrderPredictIn,
from RandomForest2 import main,predictions,read_data
from RandomForest2 import save_data
#from schemas import HealthCheck
import typing as t
from pydantic import BaseModel, ValidationError, root_validator, Field

#settings = get_settings()

app = FastAPI(title='Predict ETA service', version='0.0.1',
              description="Copyright © 2019-2022 Aram Meem Company Limited. All Rights Reserved.",
              contact={"email": "admin@arammeem.com"})

#DB_URL = f"postgres://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"


# loading model data
#s3_client = boto3.client('s3')
#tf = tempfile.NamedTemporaryFile(mode='wb', delete=False)
#s3_client.download_file(settings.s3_bucket, settings.s3_path, tf.name)
#cbr = cb.CatBoostRegressor()
#cbr.load_model(tf.name)
#os.unlink(tf.name)



@app.get('/')
async def pr():
    """Get order predict ETA in seconds"""
    datasetttt = read_data()
    pr = predictions()
    datas = save_data()
    return JSONResponse({'predicted_orders': pr,'data':datas})



    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True, log_level='debug')
