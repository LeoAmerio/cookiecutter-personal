import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR =  "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET = "\x1b[0m"

if project_slug.startswith("x"):
  print(f"{MESSAGE_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET}")
  
  sys.exit()
  
print(f"{MESSAGE_COLOR}Let's do it! You're going to  create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET}")
