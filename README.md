# generator

This project contains a Python module which can be imported by other Python files, in order to use the generateId function, which generates unique strings that are sortable, and could be used as IDs.

The function uses the method of generating a random 128 bit number, which is large enough to make collisions very unlikely. It then attaches this number to the current Unix Epoch Time, which makes it sortable based on creation order.

To use:
```bash
git clone https://github.com/kahyde/generator/ && cd generator
```
To run the test, generating 20 values:
```bash
python generatortest.py 20
```
