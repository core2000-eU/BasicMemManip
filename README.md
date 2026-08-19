# BasicMemManip
*BasicMemManip*, a Python module that extends Python with some low-level, C/C++ -related features (intended to be used in combination with Pythons ctypes library).

## Basics
**Compatibility:**  
Basically: Windows and Unix-like on Python 3+.  
Here's a list of confirmed options:  

<div style="margin-left: 20px;">

  | Name | Version | Description |
  |------|---------|-------------|
  | -- |
  | Windows 10 |      | ✅ should work   |
  | Windows 11 | 25H2 | ✅ confirmed working  |
  | RHEL/Rocky Linux  | 10        | ✅ confirmed working |
  | -- |
  | Python  | 3.14.2        | ✅ confirmed working |

</div>

**Status:** *public beta*.  
The current functions are tested on compatible platforms and evertything should be ready for full release, but I want the community to have a look at it.  

**Install** by running `pip install BasicMemManip`, **venv** highly recommended because of the low-level stuff happening. See section Installation below for details.  

**Use** the library in your project by importing with `import BasicMemManip`.

*BasicMemManip* is especially useful when dealing with *ctypes* for C/C++ libraries.

If you don't understand what we're talking about, it's best if you leave this library alone, you can seriously damage things. With *BasicMemManip* it's quite easy to overcome python's buffer overflow protection.

## Installation

<div style="margin-left: 20px;">

  | Type | Details |
  |------|---------|
  | **venv** highly recommended. Please adapt the commands below to your needs. |
  | **Auto install**<br>(preferred, easiest) | run `pip install BasicMemManip`, it will download and install from pypi.org |
  | **Manual install from source** | 1. Download the entire source from GitHub<br>2. unpack from ZIP<br>3. run e.g `python -m pip install "/path/to/folder/BasicMemManip/" --no-cache-dir` |

</div>

## Usage
Your main frend is the **`/samples/BasicMemManip_sample1.py`** file which, on purpose, serves as documentation and example.  
Just **open up and run** **`/samples/BasicMemManip_sample1.py`**. All functions, all details are explained inside. How smart is that!

## Documentation
This library is too small for a separate documentation, please use the source code and examples for documentation. We'll scramble one together if needed, no fear!

## Now for the boring part
**This library is created and maintained free of cost by a real human being /bla /bla /bla ...** You know the deal by now.  
But seriously, monetary support a serious subject and without some income, I cannot continue to publish and maintain.  
Not that anyone needs my gibberish anyways, but if you find it helpful, **please consider the below. Thanks :)**  
--> [**buymeacoffee.com/core2000**](https://buymeacoffee.com/core2000)

## About
Created on 08.2026 and happily maintained since by **core2000** and it's owner, Benjamin Winter.  
For more details, you can pay us a visit over on [**core2000.com**](https://core2000.com/).
