
# PersephoneP

PersephoneP is a web browser written by Python3 and PyQt5.
This browser is based on Chromium,
 which is an open source web browser engine included in PyQt5.
The data from web pages gotten by Chromium is drawn on PyQt Widgets.
PyQt is one of the most popular Python bindings for the Qt cross-platform C++ framework.
Utilizing the characteristics of Qt as cross-platform framework,
 PersephoneP is able to run on multi-platform if python is installed.

## Install

Please use ```git clone``` , ```pip install persephonep```,
 or download from this page.

This browser depends on PyQt5.
This browser needs only PyQt5 if you use PyQt 5.11.3 or earlier,
 however, this browser needs PyQt5 and PyQtWebEngine library
 if you wanna use PyQt 5.12 or later.

## How to Use

Type below and Persophonep starts.

``` bash
$ python persephonep.py
etc...
```

## How to Test

This browser is tested by pytest & pytest-qt.
Please type below commands if you want to execute those tests.

```text
$ pytest
etc...
```

## The reasons of Development

Some people say that making browser is reinventing the wheel,
 however, there are two reasons.

1. Understanding the way to get data from web page and to draw it on our PC.
1. Some workers, including me, are forced to use the IE at work. BUT,
 we wanna use other than IE!!

## Notice

This program's original name was "persephone",
 however, there were a lot f program which have same name.
![Window of Persephone](https://github.com/montblanc18/persephonep/blob/master/img/window_of_persephonep.png "Window_of_Persephone")