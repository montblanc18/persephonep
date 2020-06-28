
# PersephoneP

PersephoneP is a web browser written by Python3 and [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/).
This browser is based on Chromium,
 which is an open source web browser engine included in PyQt5.
The data from web pages gotten by Chromium is drawn on PyQt Widgets.
PyQt is one of the most popular Python bindings for the Qt cross-platform C++ framework.
Utilizing the characteristics of Qt as cross-platform framework,
 PersephoneP is able to run on multi-platform if python is installed.

## Requirement

- PyQt5 >= 5.12
- PyQtWebEngine >= 5.12

## Install

Please use ```git clone & python setup.py install``` , ```pip install persephonep```,
 or download from this page.

## How to Use

Type below and Persophonep starts.

```python
>> import persephonep
>> persephonep.browser()
```

If you call persephonep via python shell ( ```persephonep.browser()``` ), your python shell will exit just after the persephonep browser is closed.
That is because calling ```sys.exit()``` in ```persephonep.browser()```.

## How to Test

This browser is tested by pytest & pytest-qt.
Please type below commands if you want to execute those tests.

```text
$ python -m venv venv
$ source venv/bin/activate
$ pip install -U pip
$ pip install -e . -r requirements.txt
$ export QT_DEBUG_PLUGINS=1
$ pytest
```

<!--
```text
$ pytest --no-xvfb
```
-->

## The reasons of Development

Some people say that making browser is reinventing the wheel,
 however, there are two reasons.

1. Understanding the way to get data from web page and to draw it on our PC.
1. Some workers are forced to use the IE at work. BUT,
 we wanna use other than IE!!

### History of Development

1. I got a job with a japanese company.
1. This company prohibited my using browsers except IE.
1. I decided to develop my browser.
1. That company forced me to submit applications before installing software or libraries which I want.
1. PyQt5 based on only sip module and sip run with PurePython.
1. I decided to use PyQt5.

## Notice

This program's original name was "persephone",
 however, there were a lot f program which have same name.
![Window of Persephone](https://github.com/montblanc18/persephonep/blob/master/img/window_of_persephonep.png "Window_of_Persephone")

## Constitution of PersephoneP

This browser is consisted by 3 items.

- PersephonepMainWidget (```QMainWindow```)
- PersephonepTableWidget(```QWidget```)
- PersephonepWindow(```QWidget```)

### PersephonepMainWindow(```QMainWindow```)

This item is a main frame of Persephonep.
The role of this item is very simple.

- Handling the initial parameters of this browser, such as position, size, and so on.
- Call PersephonepTableWidget and display it in own frame.

### PersephonepTableWIdget(```QWidget```)

This item control the tab system of this browser. It handles the standard functions of tab, such as adding tabs, closing tabs, and so on.

### PersephonepWindows(```QWidget```)

This item is a main viewer of this browser.