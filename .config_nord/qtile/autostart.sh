#!/bin/sh
lxsession &
picom --experimental-backends &
dunst &
feh --bg-scale --randomize ~/.config/wallpapers/* &