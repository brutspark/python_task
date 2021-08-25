import multiprocessing
from playsound import playsound
import sys
import json

noise = 0
clean = 0

filename = 'data.json'

data = {}
data['sound'] = []


p = multiprocessing.Process(target = playsound, args = (sys.argv[1],))
p.start()
inp = input('press n if noise or c if clean\n')
if(inp == "n"):
    p.terminate()
    noise += 1
    with open(filename, "r") as file:
        data = json.load(file)
    data["sound"].append({
    "noise": sys.argv[1]
})
elif(inp == "c"):
    p.terminate()
    clean += 1
    with open(filename, "r") as file:
        data = json.load(file)
    data["sound"].append({
    "clean": sys.argv[1] 

})



print("Noise is ", noise, "\n")
print("Clean voice is ", clean, "\n")



with open(filename, "w") as file:
    json.dump(data, file)