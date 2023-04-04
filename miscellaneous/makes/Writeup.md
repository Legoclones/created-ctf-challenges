# Makes Writeup
You can extract the names of all of the targets from the `Makefile` using the command: 

```bash
cat Makefile | grep ":" | cut -d':' -f1 > makefile_targets.txt
```

Then, you can make a list of what all of the make targets print out by using the wonderful bash loop:

```bash
touch makefile_output; for entry in `cat makefile_targets.txt`; do (make $entry | grep -v "Leaving directory" | grep -v "echo" | grep -v "make" | tr '\n' '' >> output.txt); echo "" >> makefile_output.txt; done;
```

Please note that you will have to remove targets `Ja56c77a6`, `n103193b0`, and `l6f83d9ad`, since those will get you caught in an infinite loop of make targets that call each other/themselves. 

Then, you can use the command `grep "1111111l11lll1ll11l11111111l" -n makefile_output.txt` to find the line number that the target is on in `makefile_targets.txt`. This command will give you `720`, and the 720th make target is `y2f45206c`.

**Flag** - `byuctf{y2f45206c}`