# Cmder

ConEmu is a Terminal (aka Console Window) for different Shells (aka Console
Applications): http://cmder.net

### Shortcuts

- Summon from taskbar (anywhere): `` Ctrl + ` (Strg + Ö)``
- New tab with options: `Ctrl + T`
- New CMD tab: `Shift + Alt + 1`
- Close tab: `Ctrl + W`
- Go up one directory level: `Ctrl + Alt + U`
- Enter fullscreen mode: `Alt + Enter`
- Open path: `Ctrl + Left Click`, customize via "Settings..." -> "Keys & Macro" -> "Highlight" -> `#"C:\Program Files\Sublime Text 3\subl.exe" -n%1 "%3"`

### Alias

- Define alias and pass all command line arguments: `alias p3=<path/to/python3> $*`

### Scripts

- Deploy scripts that can be run from anywhere here: `<CMDER_ROOT>\vendor\conemu-maximus5\ConEmu\Scripts`

### Splitscreen

- Open tab in splitscreen mode, 50 percent to the bottom: `-new_console:s50h`

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
