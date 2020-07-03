# Copyright Fixer

Fix copyrights for a specific folder.
If there is already a copyright statement on the file, this script will remove all comments from the start of the file/copyright notice all the way to the end of the file/start of code (no comments)!

#### Requirements

The python script requires Python 3.0 or higher.

#### Run

The command-line parameters to run the fixCopyright.py scripts are as follow:
<0=TCL, 1=C++, 2=ALLfiles> <recursiveTrue?>

```
python3 fixCopyright  [path_to_check]
                      [file_types]
                      [recursive_flag]
```

- ```path_to_check``` Requires a valid path to the root folder that you want to be check.
- ```file_types``` Defines if you want to treat TCL files (0) C++ files (1) or both (2).
- ```recursive_flag``` Sets wheather or not folders are checked recursively.

An example of how to use the command is found below:

```
python3 fixCopyright home/myFolder 2 1
```

You can also modify the ```cpp_copyright_block.txt``` or ```tcl_copyright_block.txt``` file to change the copyright format (currently BSD 3).
