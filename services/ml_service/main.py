from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(flat_id: int, item_features: dict):
    prediction = app.handler.predict( item_features)


    return ({
             'price': str(prediction),
             'flat_id': flat_id
            })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
