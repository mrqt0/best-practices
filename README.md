# Best practices

## General

This project represents a central reference point for best practices in python
(later possibly other languages as well). Such, it provides templates and
enforces a common style in other projects.

This may encompass:
- Shebang
- Formatting
- The use of standard modules
  - logger
  - argparse
  - etc.
- Doctrings
- Project layouts

Where there is no such thing as "best", we will decide on one option.


### Standard Tools

## Cmder

Nice way to get UNIX shell and git for windows: http://cmder.net

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


## Sublime Text

Preferred editor: http://www.sublimetext.com/3

### Edit

- Indent: `Ctrl + ´`
- Unident: `Ctrl + ß`
- Delete line: `Ctrl + Shift + K`

### Select

Multiple selection:
- Select word (add instance) `Ctrl + D`
- Skip instance `Ctrl + K`
- De-select instance `Ctrl + U`
- Select whole line `Ctrl + L`
- Split selection into lines `Ctrl + Shift + L`

Column selection:
- Column selection `Shift + Right mouse button`
- Column add `Shift + Ctrl + Right mouse button`

Move:
- Move line / selection up / down `Ctrl + Shift + Up / Down`
- Swap two words or letters `Ctrl + T`

### Search and replace

Search:
- Search `Ctrl + F`
- Incremental Search (closes) `Ctrl + I`
- Search in multiple files `Ctrl + Shift + F`
- Regular expression `Alt + R`
- Case sensitive `Alt + C`
- Exact match `Alt + W`

### Tools

Command palette:
- Open command palette `Ctrl + Shift + P`

Run build:
- Run build `Ctrl + B`
- Run specific build system `Ctrl + Shift + B`

Create own build system:
- Tools -> Build System -> New Build System...
- e.g. `Cmder.sublime-build` to open Cmder for file directory:
```
{
    "cmd": ["C:\\Program Files\\Cmder\\Cmder.exe", "/SINGLE", "$file_path"],
}
```

### Projects and Files

Side bar:
- Open side bar `Ctrl + K, Ctrl + B`
- Focus side bar `Ctrl + 0`

Go to:
- Go to anything `Ctrl + P`
- Go to symbol `Ctrl + R` or `Ctrl + P, @`
- Go to line `Ctrl + G` or `Ctrl + P, :`
- Go to fuzzy `Ctrl + Ü` or `Ctrl + P, #`
- Go to definition `F12`

### View

- Open two-column layout `Alt + Shift + 2`
- Focus groups `Ctrl + 1` or `Ctrl + K, Ctrl + Left` etc.
- Move file to new group `Ctrl + K, Ctrl + Up`
- Close group `Ctrl + K, Ctrl + Up`

### Settings

User:
```json
{
    // Default is also good
    "theme": "Monokai Pro.sublime-theme",
    // Monokai or
    "color_scheme": "Monokai Pro.sublime-color-scheme",
    "ignored_packages":
    [
        "Vintage"
    ],
    // Other good fonts are Ubuntu Mono, Source Code Pro or Consolas
    "font_face": "Hack",
    "font_size": 12,
    // Avoid distracting blinking, but still make caret visible
    "highlight_line": true,
    "caret_style": "solid",
    "wide_caret": true
    // Indentation hints
    "draw_white_space": "all",
    "indent_guide_options":
    [
        "draw_active"
    ],
    // Reduce distractions
    "fold_buttons": false,
    "scroll_past_end": true,
    // Optimized whitespace handling
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "ensure_newline_at_eof_on_save": true,
}
```

Syntax-specific Markdown:
```json
{
    "rulers": [79],
    "spell_check": true,
}
```

### Plugins

- [Advanced CSV](https://packagecontrol.io/packages/Advanced%20CSV)
- [Terminal](https://packagecontrol.io/packages/Terminal)
- [MarkdownPreview]()


## Git

Comes with Cmder. Basic setup:
```
git config --global user.name "Marco Weber"
git config --global user.email marco.weber@hotmail.de
git config --global core.editor "C:\Program Files\Sublime Text 3\subl.exe --wait --new-window"
git config --global credential.helper wincred
git config --global core.excludesfile %USERPROFILE%\.gitignore
```

[Commit messages](https://chris.beams.io/posts/git-commit/):
- Subject line:
  - starts with capital letter
  - uses imperative mode
  - does not end in a period
  - is max. 50 characters
  - is separated by blank line from rest
- Other lines:
  - are max. 72 characters
  - explain the *what* and *why*


## Python

Integrate MiniConda in Cmder:
- Under `Settings -> Startup -> Tasks` clone existing `cmd::Cmder` task
- Specify some name, e.g. `Conda`
- Copy into textbox: `cmd /k "%ConEmuDir%\..\init.bat"  " & "%Home%\AppData\Local\Continuum\Miniconda3\Scripts\activate.bat" "%Home%\AppData\Local\Continuum\Miniconda3\"`
