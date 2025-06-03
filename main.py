from urllib import request
from time import sleep

while True:
  sleep(5)
  x = 10

  form_url = "".format(x)
  request.urlopen(form_url)
  print("All Good")
  
