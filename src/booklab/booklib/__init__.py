"""
Module aimed for `booklab` general purpose functions usable across all its (sub)modules.

**Notes**:

- Functions / code defined in this module is agnostic to web application context or CLI application context.
In cases where a context is needed this will be _trasparent_ applied locally, meaning that once exit from that function, previous context is fully restored (no side-effects).

- Some functions could run in background and return control immediatelly after call. These will accept a _callback endpoint_ to be called when finish run.

- Some functions could have a "lazy / delayed" run behavior and these will be accordingly documented to avoid false expectations.

Author: Petre Iordanescu (petre.iordanescu@gnail.com)
"""



