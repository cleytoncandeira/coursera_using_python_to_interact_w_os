#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))

print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))


#o módulo 'os' puxa algo do env, de nome Home, Shell e Fruit

