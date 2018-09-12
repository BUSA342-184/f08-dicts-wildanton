# f08-lists

Write a Python program, `fromto.py` that reads through the [e-mail file from the text](http://www.py4e.com/code/mbox-short.txt), `mbox-short.txt`, and finds all of the lines that start with `From:` and `To:`.

Your program should "grab" the e-mail address, which should be in the second space of those `From:` and `To:` lines.

Your program should split the e-mail address into the username and the hostname (FQDN) and store these into a tiny list with two elements:

|position|data item|
|:------:|:-------:|
|   0    | username |
|   1    | hostname |

Put these tiny lists into  one of two larger lists: either addresses that appeared in lines that began with `From:` or that appeared in lines that began with `To:`.

NOTE:  If the e-mail address and hostname pair is already on the `From:` list or `To:` list, take care to NOT add it again!

Finally, before your program exits, simply traverse both lists and print the following information to the screen:  From or To, the username, and the hostname all on one line per "tiny list" separated by a comma.  Your final output should have about 40 lines.

## Rubric
|  Criteria               | Possible | Actual  | Notes |
|:------------------------|:--------:|:-------:|:------|
| From: entries           |     4    |         |    |
| To: entries             |     4    |         |    |
| DOCSTRING               |     1    |         |    |
| Comments                |     1    |         |    |
| TOTAL                        10    |         |    |

