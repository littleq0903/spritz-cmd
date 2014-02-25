spritz-cmd
==========

[Demo](https://asciinema.org/a/7882)

The command-line version of implementation which is inspired by a cool reading tool, Spritz.

## Usage

Read from files:

```shell
./spritz.py [wpm] [<file1>, <file2>, ...]
```

Read from stdin:

```shell
cat sample/1-company.txt | ./spritz.py [wpm>]
```

or 

```shell
pbpaste | ./spritz.py [wpm]
```

If the wpm is not given, default value of wpm is **250**.

## About Spritz

[Spritz](http://www.spritzinc.com/)
