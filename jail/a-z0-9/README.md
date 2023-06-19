# a-z0-9
Level - Hard

Description:
```
You can't use any of the letters of the alphabet OR any numbers

OH and don't make it tooooo long

nc byuctf.xyz 40005

[a-z0-9.py]
```

## Writeup
The following solution works - `𝘦𝘹𝘦𝘤("𝘢=𝘤𝘩𝘳;𝘣=𝘰𝘳𝘥;𝘤=𝘣('൬');𝘥=𝘢(𝘤-𝘣('೸'));𝘱𝘳𝘪𝘯𝘵(𝘰𝘱𝘦𝘯(𝘢(𝘤-𝘣('ആ'))+𝘢(𝘤-𝘣('ഀ'))+𝘢(𝘤-𝘣('ഋ'))+𝘢(𝘤-𝘣('അ'))+'.'+𝘥+𝘢(𝘤-𝘣('೴'))+𝘥).𝘳𝘦𝘢𝘥())")`

**Flag** - `byuctf{urwelcome_4nd_th4nk_y0u_f0r_4tt3nding}`

## Hosting
This challenge should be a Docker container that runs the Python script `a-z0-9.py` every time someone connects on port 40005. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t az09 .
sudo docker network create -d bridge az09
```

The command to start the challenge is:

```bash
sudo docker run -p 40005:40000 --detach --name az09 --network az09 az09:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop az09
```

```
exec("𝘱𝘳𝘪𝘯𝘵(𝘰𝘱𝘦𝘯('flag.txt').𝘳𝘦𝘢𝘥())")

x = 𝘤𝘩𝘳(𝘰𝘳𝘥('~')-𝘪𝘯𝘵('൬'))
t = 𝘤𝘩𝘳(𝘰𝘳𝘥('{')-𝘪𝘯𝘵('᮷'))
a = 𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘛𝘳𝘶𝘦)
f = 𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘪𝘯𝘵('൬'))
l = 𝘤𝘩𝘳(𝘰𝘳𝘥('.')+𝘰𝘳𝘥('>'))
g = 𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘪𝘯𝘵('᮷'))


𝘢=𝘤𝘩𝘳;𝘣=𝘰𝘳𝘥;𝘤=𝘣('൬');
x = 𝘢(𝘤-𝘣('೴'))
t = 𝘢(𝘤-𝘣('೸'))
a = 𝘢(𝘤-𝘣('ഋ'))
f = 𝘢(𝘤-𝘣('ആ'))
l = 𝘢(𝘤-𝘣('ഀ'))
g = 𝘢(𝘤-𝘣('അ'))

188 = 𝘦𝘹𝘦𝘤("𝘱𝘳𝘪𝘯𝘵(𝘰𝘱𝘦𝘯(𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘪𝘯𝘵('൬'))+𝘤𝘩𝘳(𝘰𝘳𝘥('.')+𝘰𝘳𝘥('>'))+𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘛𝘳𝘶𝘦)+𝘤𝘩𝘳(𝘰𝘳𝘥('`')+𝘪𝘯𝘵('᮷'))+'.'+𝘤𝘩𝘳(𝘰𝘳𝘥('{')-𝘪𝘯𝘵('᮷'))+𝘤𝘩𝘳(𝘰𝘳𝘥('~')-𝘪𝘯𝘵('൬'))+𝘤𝘩𝘳(𝘰𝘳𝘥('{')-𝘪𝘯𝘵('᮷'))).𝘳𝘦𝘢𝘥())")

157 - 𝘦𝘹𝘦𝘤("𝘢=𝘤𝘩𝘳;𝘣=𝘰𝘳𝘥;𝘦=𝘢(𝘣('{')-𝘪𝘯𝘵('᮷'));𝘱𝘳𝘪𝘯𝘵(𝘰𝘱𝘦𝘯(𝘢(𝘣('`')+𝘪𝘯𝘵('൬'))+𝘢(𝘣('.')+𝘣('>'))+𝘢(𝘣('`')+𝘛𝘳𝘶𝘦)+𝘢(𝘣('`')+𝘪𝘯𝘵('᮷'))+'.'+𝘦+𝘢(𝘣('~')-𝘪𝘯𝘵('൬'))+𝘦).𝘳𝘦𝘢𝘥())")

130 - 𝘦𝘹𝘦𝘤("𝘢=𝘤𝘩𝘳;𝘣=𝘰𝘳𝘥;𝘤=𝘣('൬');𝘥=𝘢(𝘤-𝘣('೸'));𝘱𝘳𝘪𝘯𝘵(𝘰𝘱𝘦𝘯(𝘢(𝘤-𝘣('ആ'))+𝘢(𝘤-𝘣('ഀ'))+𝘢(𝘤-𝘣('ഋ'))+𝘢(𝘤-𝘣('അ'))+'.'+𝘥+𝘢(𝘤-𝘣('೴'))+𝘥).𝘳𝘦𝘢𝘥())")
```