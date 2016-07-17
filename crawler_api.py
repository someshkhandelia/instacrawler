import urllib.request
import json
from json import load
import urllib.parse


#new_python_object = json.loads(json_string)
#json_string = json.dumps(python_object)

#######################################################################################################################
access_token='' # access_token
userid = "" # user-id
url = "https://api.instagram.com/v1/users/"+userid+"/?access_token="+access_token

#######################################################################################################################

response = urllib.request.urlopen(url).read()
jsonobj = json.loads(response.decode('utf-8'))

#######################################################################################################################
print ("Followed by ",jsonobj["data"]["counts"]["followed_by"]," people")
print ("Follows ",jsonobj["data"]["counts"]["follows"]," people")



