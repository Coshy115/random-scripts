#!/bin/bash

# Requires libnotify

# Updates System
sudo pacman -Syu --noconfirm

# Cleans Cache
sudo pacman -Sc --noconfirm

notify-send "System Update Complete."
