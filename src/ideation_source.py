import requests
import json
import random

#using a french api
def get_word_idea_or_sentence(nature: str="") -> str:
  if not nature:
    natures = ["mot","idee","phrase"]
    nature = natures[random.randint(0, 2)]
  response = requests.get("https://www.cfsl.net/poule-de-cristal/api.php?nature="+nature)
  return ("{0}: {1}".format(nature, response.text))

#using an english api
def get_quote() -> str:
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "“{0}” — {1}".format(json_data[0]['q'], json_data[0]['a'])
  return (quote)

def get_daily_ideation() -> str:
  return ("~Daily~\n{0}\n{1}\n".format(get_word_idea_or_sentence(), get_quote()))