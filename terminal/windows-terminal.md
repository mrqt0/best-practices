# Windows Terminal

Add Cmder

```json
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

```json
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
- Change size: `Alt+Shift+arrows`
- Switch Focus: `Alt+Left` or other arrows
- New Tab: `Ctrl+Shift+T`
- Close Tab: `Ctrl+Shift+W`