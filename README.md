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

### Windows Terminal integration

Add a profile:
```
{
    "guid": "{267ee24c-e8f1-4f69-86c9-dbd7943e20ca}",
    "commandline" : "cmd.exe /k C:/Users/marco/tools/cmder/vendor/init.bat",
    "name" : "cmder",
    "icon" : "C:/Users/marco/tools/cmder/icons/cmder.ico",
    "startingDirectory" : "%USERPROFILE%",
    "fontFace": "Cascadia Code",
    "fontSize": 14,
    "useAcrylic": false,
    "acrylicOpacity": 0.9,
    "backgroundImage": "https://bing.nanxiongnandi.com/201405/ObservatoryFabra_1366x768.jpg",
    "backgroundImageOpacity": 0.2,
    "colorScheme": "Monokai Night"
}
```

You might also want to make it the default profile:
```
    "defaultProfile": "{267ee24c-e8f1-4f69-86c9-dbd7943e20ca}",
    "requestedTheme": "dark",
```

Color schemes:
- [Monokai Night](
  https://github.com/NickSeagull/windows-terminal-monokai-night/blob/master/scheme.json)
- [Dracula](https://draculatheme.com/windows-terminal/)

Windows Terminal Shortcuts:
- Full screen: `Alt+Enter` or `F11`
- Search: `Ctrl+Shift+F`
- Split Panes horizontally: `Alt+Shift+-`
- Split Panes horizontally: `Alt+Shift++`
- Switch Focus: `Alt+Left` or other arrows
- New Tab: `Ctrl+Shift+T`
- Close Tab: `Ctrl+Shift+W`


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

### Tricks

Force line wrap at 79 chars: regex search and replace
- find: `(.{79})`
- replace: `$1\n`

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
    "draw_white_space": "selection",
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
    "remember_full_screen": true
}
```

Syntax-specific Markdown (you can toggle spell check with `F6`):
```json
{
    "rulers": [79],
    "spell_check": true,
}
```

Distraction-free:
```json
{
    "rulers": [],
    "draw_indent_guides": false
}
```

### Plugins

Install Package Control behind company proxy:
- Copy code snippet from https://packagecontrol.io/installation
- Replace empty Proxy Handler with `urllib.request.ProxyHandler({"http":"http://username:password@url:port"}))`
- "View" -> "Show Console"
- Paste and execute

Configure Package Control:
```json
{
	  "http_proxy": "url:port",
	  "https_proxy": "url:port,
	  "proxy_password": "password,
	  "proxy_username": "username"
}
```

Recommended Packages:
- [Advanced CSV](https://packagecontrol.io/packages/Advanced%20CSV)
- [Terminal](https://packagecontrol.io/packages/Terminal)
- [MarkdownPreview]()
- [Terminus](https://packagecontrol.io/packages/Terminus)
- [Monokai Pro]()

The "View Package File" command help you find the package files.
The "PackageResourceViewer" lets you look into the files.

With Monokai Pro: set minimal mode in user setings:
```json
    "monokai_pro_minimal": true,
```


### Terminal integration

With `Terminus`, you can use different shells from within Sublime Text.
Add the terminals to your user config by copying them from the default config:
```json
"default_config": "Cmder",
"shell_configs": [
    {
        "name": "Cmder",
        "cmd": ["cmd.exe", "/k", "%CMDER_ROOT%\\vendor\\init.bat"],
        "env": {},
        "enable": true,
        "platforms": ["windows"]
    },
]
```

Now you can launch the shells in the panel (bottom) or a view (tab) with
"Terminus: List Shells".

Add a keyboard shortcut to toggle the panel. Note that the terminal will not be
closed, but only disappear. To close, use `ctrl+shift+w` by default. If the
terminal is not open yet, a new default shell will be opened.
```json
{
    "keys": ["ctrl+`"], "command": "toggle_terminus_panel", "args": {
        "cwd": "${file_path:${folder}}"
    }
}
```

Add another command to open a new tab (view):
```json
{
    "keys": ["alt+`"], "command": "terminus_open", "args": {
        "cwd": "${file_path:${folder}}"
    }
}
```

You can make a build system be run by terminus by adding the following lines.
The two targets `terminus_exec` and `terminus_open` support the same arguments
(nearly all of the default Sublime Text target), but differ in their defaults;
most notably, whether they are executed in a panel or a view.
Note that the build keeps running when you close the panel (unlike builds in
views, which are stopped).
```json
    "target": "terminus_exec",
    "cancel": "terminus_cancel_build",
    "focus": true,
```

Some theme like Monokai Pro set the background of the panel. This will conflict
with the background color of the Terminus theme due to some Sublime Text issue.
You may either:
1. Create a Terminus color scheme that matches the background color of the
   Sublime Text theme
2. Adapt the theme. For Monokai pro, you copy the `.sublime-theme` file into
   you user config directory and overwrite the color of `text_output_control`.

### Git integration

Add keyboard shortcut to launch Sublime Merge:
```json
    {
        "keys": ["alt+z"], "command": "sublime_merge_open_repo"
    }
```


## Git

Comes with Cmder. Basic setup:
```sh
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

Diff between different files on different branches:
```
git diff branch1:path1 branch2:path2`
```
Note: Only seems to work with paths relative to repository (not current
directory).

Add only sections of file:
```
git add -p
```

Interactive rebase:
```
git rebase -i
```

Reset tags:
```
git push origin :refs/tags/v1.0
git tag -fa v1.0
git push origin master --tags
```
You might need to use `git fetch -f --tags` on other PCs.

Checkout only one file from other branch:
```
git checkout develop README.md
git checkout develop conf/*.ini
```

Print author email:
```
git --no-pager show -s --format="%ae"
```

## Sublime Merge

To be able to execute `smerge` from the command line,
add the directory to `%PATH` or create an alias:
```
alias smerge="C:\Program Files\Sublime Merge\smerge.exe" $*
```


## Python

Integrate MiniConda in Cmder:
- Under `Settings -> Startup -> Tasks` clone existing `cmd::Cmder` task
- Specify some name, e.g. `Conda`
- Copy into textbox: `cmd /k "%ConEmuDir%\..\init.bat"  " & "%Home%\AppData\Local\Continuum\Miniconda3\Scripts\activate.bat" "%Home%\AppData\Local\Continuum\Miniconda3\"`
