### Yeamin Faiaj ; Started Working on 6th May 2022

### Imports

import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile

### variables

mod = "mod4"
terminal = "alacritty"

### keybindings

keys = [
    
    # Applications
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "z", lazy.spawn("pcmanfm"), desc="Launch pcmanfm"),
    Key([mod], "x", lazy.spawn("telegram-desktop"), desc="Launch telegram-desktop"),
    Key([mod], "c", lazy.spawn("discord"), desc="Launch discord"),
    Key([mod], "v", lazy.spawn("subl"), desc="Launch rofi"),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn("rofi -show drun"), desc="Launch rofi"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='Toggle floating'), 
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    # System
    Key([mod, "control"], "w", lazy.spawn(["bash", "-c", "feh --bg-scale --randomize ~/.config/wallpapers/*"])),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # Media keys
    Key([], "Print", lazy.spawn("sh /home/yeamin/.config/qtile/screenshot.sh")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@  -1.5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +1.5%")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 5%")),
]

### Workspaces

groups = [
    Group("1", label="", layout="columns", matches=[Match(wm_class="firefox")]),
    Group("2", label="", layout="columns", matches=[Match(wm_class="subl"), Match(wm_class="code")]),
    Group("3", label="", layout="columns"),
    Group("4", label="", layout="columns", matches=[Match(wm_class="pcmanfm")]),
    Group("5", label="", layout="floating", matches=[Match(wm_class="mpv")]),
    Group("6", label="", layout="columns", matches=[Match(wm_class="telegram-desktop"), Match(wm_class="discord")]),
    Group("7", label="", layout="columns", matches=[Match(wm_class="okular")]),
    Group("8", label="", layout="columns"),
    Group("9", label="", layout="columns", matches=[Match(wm_class="qbittorrent")]),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

### Layout

layout_theme = {
    "border_width": 2,
    "border_on_single": 2,
    "margin": 8,
    "margin_on_single": 6,
    "border_focus": "#FFFFFF",
    "border_normal": "#333333"
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Floating(**layout_theme),
]

###### Bar ######

widget_defaults = dict(
    font="Fira Code Nerd Font",
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth = 0,
                       padding = 1,
                       background = "#000000"
                       ),
                widget.CurrentLayoutIcon(
                    scale = 0.7,
                    padding = 2
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 4,
                       background = "#000000"
                ),
                widget.CPU(
                    background = "#333333",
                    foreground = "#FFFFFF",
                    format = " {load_percent}%",
                    fontsize = 13,
                    full_char = "100%",
                    padding = 5
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = "#000000"
                ),
                widget.Memory(
                    background = "#333333",
                    foreground = "#FFFFFF",
                    format = " {MemUsed:.0f}{mm}",
                    fontsize = 13,
                    padding = 5
                ),
                widget.Spacer(),
                widget.GroupBox(
                    fontsize=20,
                    disable_drag=True,
                    inactive="#999999",
                    active="#FFFFFF",
                    highlight_method="line",
                    block_highlight_text_color="#000000",
                    borderwidth=1,
                    highlight_color="#FFFFFF",
                    background = "#000000",
                    padding_x = 6,
                    center_aligned = True
                ),
                widget.Spacer(),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = "#000000"
                       ),
                widget.Volume(
                    background = "#333333",
                    foreground = "#FFFFFF",
                    fmt=" {}",
                    fontsize = 13,
                    padding = 5
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = "#000000"
                ),
                widget.Battery(
                    background = "#333333",
                    foreground = "#FFFFFF",
                    low_foreground = "#8f0000",
                    format = " {percent:2.0%}",
                    fontsize = 13,
                    low_percentage = 0.25,
                    padding = 5
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = "#000000"
                ),
                widget.Clock(
                    background = "#333333",
                    foreground = "#FFFFFF",
                    padding = 6,
                    fontsize = 13,
                    format = ' %H:%M'
                ),
                widget.Sep(
                   linewidth = 0,
                   padding = 6,
                   background = "#000000"
                ),
                widget.Systray(
                   background = "#333333",
                   icon_size = 13,
                   padding = 6
                   ),
                widget.Sep(
                   linewidth = 0,
                   padding = 6,
                   background = "#333333"
                ),
                widget.TextBox(
                    padding = 7,
                    text = '',
                    fontsize = 13,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('sh /home/yeamin/.local/bin/rofi-wifi-menu.sh')},
                    background = "#333333",
                    foreground = "#FFFFFF",
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 2,
                       background = "#333333"
                ),
                widget.TextBox(
                    text = '',
                    padding = 7,
                    fontsize = 13,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('sh /home/yeamin/.local/bin/rofipowermenu.sh')},
                    background = "#333333",
                    foreground = "#FFFFFF",
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 4,
                       background = "#333333"
                ),
            ],
            size=21,
            border_color="#000000",
            border_width=5,
            background="#000000",
            margin=[3, 8, 0, 8],
        ),
    ),
]

### Mouse keybinds
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(title='Confirmation'),      # tastyworks exit box
        Match(title='Qalculate!'),        # qalculate-gtk
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    ], **layout_theme
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

### autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

wmname = "Monochromic_Life"