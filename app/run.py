from core import create_app
from models import Actor  
from controllers.actor import add_actor
app = create_app()


def mydefault(): 
    res = 0
    for i in range(1, 10000):
        if Actor.query.filter_by(id=i).first() == None:
            res = i
            break
    return res

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8000)
    
    #print(mydefault())