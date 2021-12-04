import requests

def get_idea():
  response = requests.get("https://www.cfsl.net/poule-de-cristal/api.php?nature=idee")
  return (response.text)
