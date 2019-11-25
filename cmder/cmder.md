# Cmder

ConEmu is a Terminal (aka Console Window) for different Shells (aka Console
Applications).

## General

The new_console command in ConEmu supports many switches:
- `a`: run as admin
- `r`: run as restricted user
- `b`: create background tab, meaning it is not activated
- `d:"<dir>"`: Specify working directory
- `c`: Enable "Press Enter or Esc" after termination
- `n`: Disable "Press Enter or Esc" after termination
- `h<height>`: Number of lines in scrolling buffer. 0 disables scrolling.
- `t:"<name>"`: Tab name
- `s[<SplitTab>T][<Percents>](H|V)`: Select which tab via number T


## How to create multi-window applications with Cmder

- Create new tab `cmd -new_console:n`
