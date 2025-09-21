from fastapi import FastAPI, Response
from routes.user_routes import router as users

app=FastAPI()
app.include_router(users)

@app.get('/')
def default():
    return Response(content='Try /helloworld',status_code=200)

@app.get('/helloworld')
def helloworld():
    return Response(content='Hello World',status_code=200)

if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:app',host="127.0.0.1", port=8003, reload=True)