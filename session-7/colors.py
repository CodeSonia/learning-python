from pip._vendor.colorama import init, Fore, Back, Style

def say_name(name):
  print(Fore.GREEN + Back.MAGENTA + Style.BRIGHT + name)

say_name('Rosa')
