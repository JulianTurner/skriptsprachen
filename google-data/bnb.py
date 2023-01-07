#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import os.path

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # regex to find the year
  year_re = re.compile(r'<h3 align="center">Popularity in (\d+)<\/h3>')

  # regex to find the name and rank
  name_re = re.compile(r'<tr align="right"><td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<\/td>')

  # 1. Open and read file steam
  with open(filename, "r") as file:
    year = None
    names = {}
    for line in file:
      if not year:
        if result := year_re.search(line):
          year = result[1]
      else:
        if result := name_re.search(line):
          rank = result[1]
          male = result[2]
          female = result[3]

          for name in [male, female]:
            names.setdefault(name, rank)
          

  # 3. Get the names and rank in a dictionary and print it
  # 4. Build a list and print it
  return [year] + [f"{name} {rank}" for name, rank in sorted(names.items())]



def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print("usage: [--summaryfile] file [file ...]")
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  for arg in args:
    print(arg)
    names = extract_names(arg)
    if summary:
      filename = arg + ".summary"
      # delete file if exists
      if os.path.isfile(filename):
        os.remove(filename)
      with open(filename, "x", encoding='utf-8') as file:
        file.write("\n".join(names))

    else:
      print(names)
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
