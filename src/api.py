from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load('D:/Yusma/project_obesity/models/obesity_model.pkl')

# Initialize FastAPI
app = FastAPI()

# Define input schema (16 features expected)
class PredictionRequest(BaseModel):
    features: list[float]  

@app.post('/predict')
def predict(request: PredictionRequest):
    # Validate input length
    if len(request.features) != 16:
        return {"error": f"Expected 16 features, but got {len(request.features)}"}

    # Reshape features and make prediction
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)[0]
    return {'prediction': prediction}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
