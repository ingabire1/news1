from flask import render_template
from app import app
from .models import source,article
from .request import get_articles,get_source
Source=source.Source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = get_source('general')
    tech = get_source('technology')
    sciences = get_source('science')
    entertainment = get_source('entertainment')
    sports = get_source('sports')
    health = get_source('health')
    business = get_source('business')



    title="Home- Welcome to news highlight"
    return render_template('index.html',title=title, general=general, business = business, entertainment = entertainment, sports = sports, technology = tech, science = sciences, health = health)

@app.route('/articles/<source_id>')
def articles(source_id):
  '''
  View article page function that article source page
  '''

  articles=get_articles(source_id)
  title=f'{source_id}'
  
  return render_template('articles.html',title=title,articles=articles,name=source_id)
   
