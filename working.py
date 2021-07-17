from fastapi import FastAPI

app = FastAPI()

inventory = {
   1: {
      "name": "Milk",
      "price": 3.99,
      "brand": "Kirkland"
   }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path()):
   return inventory[item_id]

# @app.get("/")
# def home():
#    return {"Data": "Testing"}
#
# @app.get("/about")
# def about():
#    return{"Data": "About"}