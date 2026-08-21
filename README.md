# BasicMemManip
*BasicMemManip*, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library).  

> This project is in use by **MPSS - Multi-platform shared storage**, a brand-new way to combine, share and access storage over LAN and WAN. Run servers, workstations and clients, multiple OSs and huge numbers of devices simultaneously.  
[Take a look here if that sounds interesting! \[core2000.com\]](https://core2000.com/software/mpss/)  

[Supporters](#now-for-the-boring-part) and contributors are welcome any day of the week! :)

## Basics
**Compatibility:**  
Basically: Windows and Unix-like on Python 3+.  
Here's a list of confirmed options:  

  | Name | Version | Description |
  |------|---------|-------------|
  | -- |
  | Windows 10 |      | ✅ should work   |
  | Windows 11 | 25H2 | ✅ confirmed working  |
  | RHEL/Rocky Linux  | 10        | ✅ confirmed working |
  | -- |
  | Python  | 3.14.2        | ✅ confirmed working |

**Status:** *public beta*.  
The current functions are tested on compatible platforms and evertything should be ready for full release, but I want the community to have a look at it.  

**Install** **Use** the library in your project by importing with `import BasicMemManip`.

**Built** on W11 25H2 with python 3.14.2, pip 26.2.1, build 1.5.0, twine 7.0.0. Standard settings.

*BasicMemManip* is especially useful when dealing with *ctypes* for C/C++ libraries.  
If you don't understand what we're talking about, it's best if you leave this library alone, you can seriously damage things. With *BasicMemManip* it's quite easy to overcome python's buffer overflow protection.

## Installation

  | Type | Details |
  |------|---------|
  | **venv** highly recommended. Please adapt the commands below to your needs. |
  | **Auto install**<br>(preferred, easiest) | run `pip install BasicMemManip`, it will download and install from pypi.org |
  | **Manual install from source** | 1. Download the entire source from GitHub<br>2. unpack from ZIP<br>3. run e.g `python -m pip install "/path/to/folder/BasicMemManip/" --no-cache-dir` |

## Usage
Import with `import BasicMemManip`.
Your main frend is the **`/samples/BasicMemManip_sample1.py`** file which, on purpose, serves as documentation and example.  
Just **open up and run** **`/samples/BasicMemManip_sample1.py`**. All functions, all details are explained inside. How smart is that!

## Documentation
This library is too small for a separate documentation. We'll scramble one together when needed, no fear!  
<br>
**Source file structure:**  
```
    <root>
        /samples        -> sample files
        /src            -> source code: main folder
            /P          -> source code: python
        LICENSE         -> LICENSE
        README.md       -> README
        setup.py        -> pip installer mandatory setup file
```
<br>

**Source code structure:**  
`/src/P/BasicMemManip/__init__.py` is the main file which contains all functions.  
There is no universal main entry point: The user imports the library `import BasicMemManip` and calls it's functions. There is no initialization.
<br>
<br>

## Official Sources

  | Site | URL |
  |------|---------|
  | **GitHub** | [github.com/core2000-eU/BasicMemManip](https://github.com/core2000-eU/BasicMemManip) |
  | **pypi.org** | [pypi.org/core2000/BasicMemManip](https://pypi.org/core2000/BasicMemManip) |
  | core2000.com (Website/info only, no release) | [core2000.com/software](https://core2000.com/software/) |

## Now for the boring part
**This library is created and maintained free of cost by a real human being /bla /bla /bla ...** You know the deal by now.  
But seriously, monetary support a serious subject and without some income, I cannot continue to publish and maintain.  

Not that anyone needs my gibberish anyways, but if you find it helpful, **please consider the below. Thanks :)**  
--> [**buymeacoffee.com/core2000**](https://buymeacoffee.com/core2000)

## About
Created on 08.2026 and happily maintained since by **core2000** and it's owner, Benjamin Winter.  
For more details, you can pay us a visit over on [**core2000.com**](https://core2000.com/).
