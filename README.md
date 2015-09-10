# download-files.py
This is a really small and simple utility I wrote for myself to download a given
list of files. The list should reside in plain text, and each line should
be one URL. You can also specify a directory for files to be downloaded to.

This utility is written for Python 3.x and has not been tested with Python 2.x.

## Usage
Simply download and call:
```
python3 download-files.py
```

Without any arguments it will use the default `urls.txt` file in this repository,
and download the files to `<CURRENT_DIR>/downloads`.

### Arguments

- `-i` (`--input-file`): The file containing your list of URLs.
- `-d` (`--download-dir`): The directory you want files downloaded to.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
