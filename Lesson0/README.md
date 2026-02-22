# Lesson 0 - Installing Python and Basic VSCode Setup

Before we begin our workshop, lets make sure you have python and VSCode
installed on your local machine.

## Installing Python

You can download python itself [here](https://www.python.org/downloads/windows/).

Search Python 3.11.9 and download the `Windows installer (64-bit)`, or desired
version. The VFX industry is largely on python 3.11 or earlier at the moment.

<img src="https://i.imgur.com/5dXicqH.png">

Run the downloaded installer and make sure to check `Add python.exe to PATH`.

<img src="https://i.imgur.com/bzQPBlF.png">

## Installing VSCode

VS Code is an `Integrated Developer Environment` application, or IDE. In other
words: a program specifically for writing software.

<img src="https://i.imgur.com/m2YLblI.png">

You can download VSCode [here](https://code.visualstudio.com/download).

## Python Extension for VSCode

Next, lets enable the python extension for VS code. This will give us some
visual feedback to our code, highlighting warnings and errors, in addition to
other useful features.

To install an extension in VSCode click on the extensions button on the left
hand column (the one that looks like 4 squares). Next, search `python` in the
search box and select the extension provided by Microsoft. Finally, click the
`install` button in the main pane by the extension logo.

<img src="https://i.imgur.com/Idlrw9F.png">

## Did we get it right?

Make a folder somewhere on your computer. This will be the project folder we
will use for the workshop.

Open this folder in VS Code and make a folder *inside* that called `workshop`.
Next, make a file inside our workshop folder called `confirm.py`
(<project_path>/workshop/confirm.py).

Inside our `confirm.py` file write out `print("hello world")`. Then, right-click
somewhere in the text editor and look for `Run Python` -> `Run Python File in Termianl`.

<img src="https://i.imgur.com/AuYYYWQ.png">

If we did everything correctly, we should see the terminal open with `hello world`
printed out.

<img src="https://i.imgur.com/MI04vt4.png">

If you got this far then you are ready for the Python Workshop!

## Bonus: VFX Reference Platform

The [VFX Reference Platform](https://vfxplatform.com/)
defines a set of tool and library versions to establish a consistent build
target for software providers in the VFX industry. Many studios reference it
but do not follow it completely, but it is a good place to get a general sense
of where langauge and build-tool versions should be at across the industry.
