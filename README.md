# Git Commenter

[![](https://img.shields.io/travis/skmatz/git-commenter)](https://travis-ci.org/skmatz/git-commenter)

```txt
   ____     ____    ____  _
U /"___|uU /"___|U /"___||"|        ___
\| |  _ /\| | u  \| | uU | | u     |_"_|
 | |_| |  | |/__  | |/__\| |/__     | |
  \____|   \____|  \____||_____|  U/| |\u
  _)(|_   _// \\  _// \\ //  \\.-,_|___|_,-.
 (__)__) (__)(__)(__)(__|_")("_)\_)-' '-(_/
```

## Overview

The **Git Commenter** is a tool to make your git commit message **colorful**.

![demo](https://i.imgur.com/qQYynv0.gif)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fgit-commenter.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fgit-commenter?ref=badge_shield)

## Get Started

```bash
pip install git-commenter --user
```

## Usage

Usage is so simple.  
Instead of `git commit`, all you have only to run `git-commenter`.

```bash
git add foo.txt
git-commenter
git push origin master
```

There are several modes.

### Normal Mode

```bash
git-commenter
```

Normal mode is the simplest use.  
You only run `git-commenter`, all interactively create commit messages.

### Clipboard Mode

```bash
git-commenter --clipboard
```

Clipboard mode paste created commit messages to the clipboard, instead of committing.  
This is useful for example when you want to input commit messages on the GitHub website.

### Message Mode

```bash
git-commenter --message MESSAGE
```

Message mode is the closest use to the actual `git commit -m`.  
You input messages as arguments and select only emoji with the CLI.

### Template Mode

```bash
git-commenter --template
```

Template mode is the easiest way for creating commit messages.  
You only select all messages from the template at once, including emoji.

### Others

| argument     | description        |
|--------------|--------------------|
| --clean      | Clean use history. |
| --version    | Show version.      |
| -h / --help  | Show help.         |

## Development

I use [Poetry](https://poetry.eustace.io) for a Python virtual environment.  
If you are not familiar with it, see the official documentation.

```bash
git clone https://github.com/skmatz/git-commenter.git
cd git-commenter
poetry install
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fgit-commenter.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fgit-commenter?ref=badge_large)