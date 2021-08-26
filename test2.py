from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
import sys
import json
import multiprocessing

noise = 0
clean = 0

filename = 'data.json'

data = {}
data = ['sound']

# Input an existing mp3 filename
mp3File = input("Enter a mp3 filename: ")
# load the file into pydub
sound_file = AudioSegment.from_mp3(mp3File)
print("Playing mp3 file...")
# play the file
p = multiprocessing.Process(target = play(sound_file))
p.start()
inp = input('press n if noise or c if clean\n')
if(inp == "n"):
    p.terminate()
    noise += 1
    print(noise)
    #with open(filename, "r+") as file:
    #    data = json.load(file)
    data['sound'].append({
    "noise": sound_file
})
elif(inp == "c"):
    p.terminate()
    clean += 1
    print(clean)
    #with open(filename, "r+") as file:
    #    data = json.load(file)
    data['sound'].append({
    "clean": sound_file 

})

print("Noise is ", noise, "\n")
print("Clean voice is ", clean, "\n")



with open(filename, 'a') as file:
    json.dump(data, file)

"""import multiprocessing
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

    """
