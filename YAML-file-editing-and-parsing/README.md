# THIS CODE IS TESTED ON PYTHON 3.8.10
# YAML-file-editing-and-parsing
Given a YAML file in a specific format, this program can update, create, and modify required values. The input values are assumed to be command line arguments.
This code takes care of all corner cases and provides explanations as to why the code failed - in the rare event that it went off the rails.
The value and key to be updated must be given as a single word separated by a colon with no spaces from the command line.

The input file is supposed to be entered as a command line argument which requires the file extention. The output is written to a different file with a prefix "output_" added to it.
