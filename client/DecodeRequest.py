import codecs
import json
import pip._vendor.requests 

# hex decimal value given on the questiom 0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38
#pload = {'encodedVal':'0x3839203530203730203438'}

#hex decimal value tested to validate the coversion is correct or not 
# 0x74657374206d657373616765 - decoded value will be test message
pload = {'encodedVal':'0x74657374206d657373616765'}

r = pip._vendor.requests .post('http://localhost:7878/post',json= pload)

print(f"Status Code: {r.status_code}, Decoded Result: {r.text}")

