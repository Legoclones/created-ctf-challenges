# Command
Level - Medium

Description:
```
Don't overcomplicate it

http://command.byuctf.xyz/
```

## Writeup
The idea for this challenge comes from [this article](https://www.bleepingcomputer.com/news/security/dont-copy-paste-commands-from-webpages-you-can-get-hacked/). Just because you copy and paste doesn't necessarily mean that you're copying and pasting what you *think* you're copying and pasting. When you copy this text, the obfuscated JavaScript present has you actually copy completely different text, which will print out everything in `/bin/`, clear your screen, and print out some messages for you! 

If the user is cautious and examines the code before copying, they may catch it. However, the long hex path is changed from what's shown. If they don't inspect and realize the path is different, they won't get the flag until they catch the discrepancy and correct it. 

Yes, this challenge is intended to be awful. 

You can also reverse engineer the JavaScript to figure out what the `setup()` function does, but that's the hard path.

**Flag** - `byuctf{n3v3r_r4nd0mly_copy_&_paste_1nput_fr0m_the_1nt3rn3t}`

## Hosting
Create a new nginx subdomain called `command.byuctf.xyz`, then copy and paste all the files from `src/*` to that folder.

## Notes
This is what bootstrap.min.js should look like after deobfuscation:
```javascript
function setup() {
    document.getElementById('command').innerText = "curl 'http://command.byuctf.xyz/d19f8d375094df38afe701712cf2066b6b464ea2ca4fc5acd201692879a420b963fb05b720755437ba15fb520d0e64a53c6b?8f868aadfda34d6daa2241cf=a61adf81ddb862bbfc18fb46' -X POST -H 'User-Agent: d5c57b98faa647623de5afba' --data='pin=0000'";
    document.getElementById('command').addEventListener('copy', function(e) {
        e.clipboardData.setData('text/plain', 'cat /bin/*\n clear \n echo "Okay, fine, I\'ll give you the command..." \n curl \'http://command.byuctf.xyz/d19f8d375094df38afe701712cf2066b6b464ea2ca4fc5acd201692879a420b963fb05b720745437ba15fb520d0e64a53c6b?8f868aadfda34d6daa2241cf=a61adf81ddb862bbfc18fb46\' -X POST -H \'User-Agent: d5c57b98faa647623de5afba\' --data=\'pin=0000\' \n clear \n echo "Hmmm you made a mistake..." \n echo "Maybe try again?" \n');
        e.preventDefault();
    });
}
```