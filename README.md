spritz-cmd
==========

[Demo](https://asciinema.org/a/7882)

The command-line version of implementation which is inspired by a cool reading tool, Spritz.

## install

via setup.py:

```shell
git clone https://github.com/littleq0903/spritz-cmd
cd spritz-cmd
python setup.py install
```

via pip:

```shell
pip install spritz
```

## Usage

Read from files:

```shell
spritz.py [wpm] [<file1>, <file2>, ...]
```

Read from stdin:

```shell
cat sample/1-company.txt | spritz.py [wpm]
```

or 

```shell
pbpaste | spritz.py [wpm]
```

If the wpm is not given, default value of wpm is **250**.

## About Spritz

[Spritz](http://www.spritzinc.com/)
