from flask import Flask
from helper import pets

app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
   return '''
   <h1>Adpot a Pet!</h1>
   <p>Browse through the links below to find your new furry friend: </p>
   <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
   </ul>
   '''

# Create Animal Routes
@app.route("/animals/<pet_type>")
def animals(pet_type):
  html = f'''<h1>List of {pet_type}</h1>'''
  
  for index, pet in enumerate(pets[pet_type]):
    html = html + f'<li><a href="/animals/{pet_type}/{index}">' + pet['name'] + '</a></li>'
  # loop thru each item within declared pet_type and return ul with data.
  return html

@app.route("/animals/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):

  pet = pets[pet_type][pet_id]
    
  return f'''
      <h1>{pet['name']}</h1>
      <img src={pet['url']} </img>
      <p>{pet['description']} </p>
      <ul>
        <li>{pet['age']}</li>
        <li>{pet['breed']}</li>
      </ul>
  '''
