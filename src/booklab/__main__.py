"""Module "entry point" for `booklab` package.

Callable with `python -m` option and defined as executable script with the
package.

Usage:

``` bash
pip install booklab
booklab [options, commands, ...]
```
"""

import sys
from . import __version__ as sysver


def main():
    """Main entry point in Booklab application.
    """
    #TODO these are simply proof of concept tests
    print("I'm in booklab.__main__ module...")
    print(f"System version is: {sysver=}")
    return 0  # POSIX std exit code for success


if __name__ == "__main__":
    sys.exit(main())


