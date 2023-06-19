# NOPQRSTUVWXYZ
Level - Medium

Description:
```
You can't use any of the last 13 letters of the alphabet EXCEPT for the first 4 letters

OH and don't make it too long

nc byuctf.xyz 40004

[nopqrstuvwxyz.py]
```

## Writeup
The following solution works - `exec("\160\162i\156\164(\157\160e\156('flag.\164\170\164').\162ead())")`
`exec("\160\162\151\156\164\050\157\160\145\156\050\047\146\154\141\147\056\164\170\164\047\051\056\162\145\141\144\050\051\051")`

**Flag** - `byuctf{1_l0v3_c0nnected_ch4llz}`

## Hosting
This challenge should be a Docker container that runs the Python script `nopqrstuvwxyz.py` every time someone connects on port 40004. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t nopqrstuvwxyz .
sudo docker network create -d bridge nopqrstuvwxyz
```

The command to start the challenge is:

```bash
sudo docker run -p 40004:40000 --detach --name nopqrstuvwxyz --network nopqrstuvwxyz nopqrstuvwxyz:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop nopqrstuvwxyz
```