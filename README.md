# How to code

*External memory for everything related to software.*

We forget things much more easily than we are willing to accept:
anything but the most trivial routine tasks are susceptible to out leaky memory.
In this repository, I want to collect everything I learn about software development:
how-tos, best practices, dotfiles, configuration settings, etc.

It shall serve as a central reference point to 
- quickly set up new projects
- reuse already found solutions
- encourage a common style.

The goal is less to list every possible alternative,
but more to provide an opinionated guide.


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
