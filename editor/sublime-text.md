# Sublime Text

Preferred editor: http://www.sublimetext.com/3

- [Usage](#usage)
- [Settings](#settings)
- [Plugins](#plugins)
- [Integrations](#integrations)

## Usage

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

- Force line wrap at 79 chars: regex search and replace
  - find: `(.{79})`
  - replace: `$1\n`
- Use "Arithmetic" from command palette as a calculator.
  You can either mark text or enter it interactively.
  It basically evaluates any Python code.
- Use "View package file" to show package source code.


## Settings

User:
```
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
    "wide_caret": true,
    // Indentation hints
    "draw_white_space": "selection",
    "indent_guide_options":
    [
        "draw_active"
    ],
    // Reduce distractions
    "fold_buttons": false,
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


## Plugins

Install Package Control behind company proxy:
- Copy code snippet from https://packagecontrol.io/installation
- Replace empty Proxy Handler with `urllib.request.ProxyHandler({"http":"http://username:password@url:port"}))`
- "View" -> "Show Console"
- Paste and execute

Configure Package Control:
```json
{
	  "http_proxy": "url:port",
	  "https_proxy": "url:port",
	  "proxy_password": "password",
	  "proxy_username": "username"
}
```

Recommended Packages:
- [Advanced CSV](https://packagecontrol.io/packages/Advanced%20CSV)
- [Terminal](https://packagecontrol.io/packages/Terminal)
- [MarkdownPreview](https://facelessuser.github.io/MarkdownPreview/)
- [Terminus](https://packagecontrol.io/packages/Terminus)
- [Monokai Pro](https://monokai.pro/sublime-text)
- [InsertDate](https://packagecontrol.io/packages/InsertDate)

The "View Package File" command help you find the package files.
The "PackageResourceViewer" lets you look into the files.

With Monokai Pro: set minimal mode in user setings:
```json
    "monokai_pro_minimal": true,
```

### Timestamps

With `InsertDate`, you can insert timestamps:

- `ctrl+shift+f5`, `ctrl+shift+d`: Insert date `YYYY-MM-DD`
- `ctrl+shift+f5`, `ctrl+shift+t`: Insert time `HH:MM:SS`

### Writing plugins

See [community guide](https://docs.sublimetext.io/guide/extensibility/plugins/):

- Open "Tools" -> "Developer" -> "New Plugin...".
- Save under "Packages/User/<name>.py".
- Choose a class name.
  The `Command` suffix will be stripped.
  You can execute the command in the console with `view.run_command("<name>")`.
- Add to the comand palette

```json
[
    {"caption": "Execute my command", "command": "<name>"}
]

You can write commands that affect the "view" (text), the window or the input.
More info in the [API reference](https://www.sublimetext.com/docs/3/api_reference.html).


## Integrations

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

### Launch terminal

With `Terminal`, add user settings:

```json
{
    "terminal": "wt.exe",
    "parameters": ["-d", "."]
}
```

- Launch terminal in current directory: `ctrl+shift+t`
- Launch terminal in project directory: `ctrl+shift+alt+t`

### Git integration

Add keyboard shortcut to launch Sublime Merge:
```json
    {
        "keys": ["alt+z"], "command": "sublime_merge_open_repo"
    }
```
