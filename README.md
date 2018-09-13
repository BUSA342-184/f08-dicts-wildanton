# f08-dicts

Write a Python program, `fromto.py` that reads through the [e-mail file from the text](http://www.py4e.com/code/mbox-short.txt), `mbox-short.txt`, finds all of the lines that start with `From:` and `To:,` processes the e-mail addresses, and prints output as described below.

Your program should "grab" the e-mail address, which you may assume are the second word of the lines beginning with `From:` and `To:` (To accomplish this you may find it helpful to "convert" the lines that begin with `From:` and `To:` into a list).  You may also assume that there is only one e-mail address in the To: field.

Your program should do the "second split:" separate the e-mail address into the username and the hostname (FQDN) hostname portion.

Finally, your program should use dictonaries to count the following:

1. usernames in the From: field
2. hosts in the From: field
3. usernames in the To: field
4. hosts in the To: field

NOTE:  The text discusses the `.get()` method for `dict` objects.  Using this simplification may help.

For each of the four `dict`s, your program should print-out a brief header followed the key and value pairs in the `dict` in the format of a `csv` (*c*omma *s*eparated *v*alues) in alphabetical order of the key as follows:
```
--- FROM USER ---
antranig,1
cwen,5
david.horwitz,4
gopal.ramasammycook,1
gsilver,3
louis,3
ray,1
rjlowe,2
stephen.marquard,2
wagnermr,1
zqian,4
--- FROM HOST ---
caret.cam.ac.uk,1
gmail.com,1
iupui.edu,8
media.berkeley.edu,4
uct.ac.za,6
umich.edu,7
--- TO USER ---
source,27
--- TO HOST ---
collab.sakaiproject.org,27
```

One way that you could accomplish this is by using the `csv.writerows()` method, after connecting the filehandle to the `STDOUT` as follows:
```
# to access STDOUT
import sys
# to access .writerows()
import csv

...

# connect a csv.writer filehandle to STDOUT
cw = csv.writer(sys.stdout)

# write an output header
print('--- FROM USER ---')
# assume that dict_fr_user is a dict() whose key and value pairs are usernames and counts
cw.writerows(sorted(dict_fr_user.items())
...

```

## Rubric
|  Criteria                                         | Possible | Actual  | Notes |
|:--------------------------------------------------|:--------:|:-------:|:------|
| Identify lines beginning with `From:` and `To:`   |     2    |         |    |
| Separate e-mail addresses                         |     2    |         |    |
| Correctly count source usernames & hostnames      |     2    |         |    |
| Correctly count destination usernames & hostnames |     2    |         |    |
| DOCSTRING                                         |     1    |         |    |
| Comments                                          |     1    |         |    |
| TOTAL                                                  10    |         |    |

