import requests
from bs4 import BeautifulSoup as bs
import re

def checkIfNumber(value):
  try:
    floatVal = float(value)
    print(floatVal)
    intVal = int(value)
  except:
    return False
  return True