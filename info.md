# Cos'è, come si installa e come si usa Git
## E come contribuire ai repository su GitHub

Breve guida pratica all'uso di Git e a come contribuire ai repository su GitHub.

La guida è in **inglese** (perché mi era più semplice prepararla così, dato che tutto il materiale che ho letto io stesso per informarmi è in inglese). Questa guida non ha la pretesa di essere completa, ma da le principali informazioni necessarie per iniziare.

(Per gli esterni che leggessero questo file, esso è stato pensanto solo per uso *inter nos*, tra me e i miei compagni di corso. Tuttavia, può risultare utile a chi sia un totale principiante di GitHub e Git in generale, come io stesso ero fino a poco tempo fa.)

***

## General information
**Git** is a decentralized (or "distributed") Version Control System (VCS) designed to handle everything from small to very large projects with speed and efficiency.
Git is Free and Open Source Software (license: GNU GPL v2).

Website: https://git-scm.com/

Unlike many Version Control Systems, Git works with **snapshots**, not differences.
This means that it does not track the difference between two versions of a file, but takes a snapshot of the current state of the project (the repository).

This is why Git is very fast compared to other distributed VCSs; it is also why switching between versions and branches is so fast and easy.

## Install Git
First of all, you need to install Git on your computer. The process varies depending on your operating system.

### Linux
On Debian, Ubuntu and derivatives (Linux Mint, Pop!_OS, ...)
```bash
sudo apt update
sudo apt install git
```

On Fedora and derivatives
```bash
sudo dnf install git
```

### ChromeOS
_(@ Diletta) più o meno, si segue la stessa procedura che hai usato per installare Python._

First, you need to "Turn on Linux": open "Settings", then open the "Advanced" menu and go to "Developers". 

![](https://chromeos-dev.imgix.net/develop/linux/getting-started/enable-linux.png?auto=format,compress&fit=fillmax&w=1500)

You may find more information [at this webpage](https://chromeos.dev/en/linux/setup): 

Then open the newly-installed Terminal app, and issue the following commands:
```bash
sudo apt update
sudo apt install git -y
```
Git should have being successfully installed in your Linux container inside ChromeOS.

### Windows
You can download the installer from: https://git-scm.com/download/win and then execute it,

or use this command in a Command prompt or PowerShell window: 
```
winget install --id Git.Git -e --source winget
```

### MacOS
Since I don't own a MacBook, I can't give you any advice. You'll need to figure it out by yourself.

Here you may find useful information: https://git-scm.com/download/mac

## Create a GitHub account
Sing up (for free) at: https://github.com/signup

## Basic configuration
Once installed, Git can be used through the terminal/command line. 
For Windows, after installation, you get a special terminal called "Git bash"; it's a terminal that tries to emulate a Unix-like shell on Windows.

Linux and MacOS come with a Unix-like shell preinstalled.
In ChromeOS, use the Terminal app.



...

***

## Extras

## GitHub CLI (`gh`)
Website: https://cli.github.com/

Repo: https://github.com/cli/cli

...

### Windows:
```
winget install --id GitHub.cli
```

### Linux:
More information: https://github.com/cli/cli/blob/trunk/docs/install_linux.md

From official sources,
**Debian/Ubuntu repo**:
```
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

or through the [release binaries](https://github.com/cli/cli/releases).

## Caching GitHub credentials in Git
...

*this document is work-in-progress*
