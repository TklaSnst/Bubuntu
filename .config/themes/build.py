from pathlib import Path
import yaml

BASE = Path.home() / ".config/themes"
OUT = Path.home() / ".config/waybar/style.css"

theme = yaml.safe_load(open(BASE / "current.yaml"))

css = f"""
* {{
    border: none;
    font-family: "JetBrainsMono Nerd Font", "Font Awesome 6 Free", Roboto, sans-serif;
    font-size: 12px;
    color: {theme["fg"]};
}}

window#waybar {{
    background: {theme["bg_panel"]};
    border-radius: 7px;
    min-height: 26px;
}}

/* === WORKSPACES === */

#workspaces button {{
    padding: 2px 8px;
    margin: 0 3px;
    background: transparent;
    color: {theme["fg_dim"]};
    border-radius: 8px;
}}

#workspaces button:hover {{
    background: {theme["bg_window"]};
    color: {theme["fg"]};
}}

#workspaces button.active {{
    background: {theme["accent"]};
    color: {theme["bg"]};
    font-weight: bold;
}}

/* === MODULES === */

#clock,
#battery,
#cpu,
#memory,
#temperature,
#network,
#pulseaudio,
#custom-media,
#tray,
#mode,
#custom-power,
#idle_inhibitor {{
    padding: 2px 10px;
    margin: 0 2px;
    border-radius: 8px;
    background: {theme["bg_window"]};
    color: {theme["fg"]};
}}

#clock:hover,
#battery:hover,
#cpu:hover,
#memory:hover,
#temperature:hover,
#network:hover,
#pulseaudio:hover,
#tray:hover,
#custom-power:hover {{
    background: {theme["bg_menu"]};
}}

/* === STATES === */

#mode {{
    color: {theme["red"]};
    background: {theme["bg_window"]};
}}

#idle_inhibitor.activated {{
    color: {theme["green"]};
}}

#pulseaudio.muted {{
    color: {theme["red"]};
}}

#battery.charging {{
    color: {theme["green"]};
}}

#battery.warning:not(.charging) {{
    color: {theme["yellow"]};
}}
"""

OUT.write_text(css)
print("waybar theme generated")

# === SWAY COLORS ===

sway = f"""
set $bg {theme["bg"]}
set $fg {theme["fg"]}
set $accent {theme["accent"]}
set $red {theme["red"]}
set $bg_alt {theme["bg_window"]}

client.focused          $accent $accent $fg $accent $accent
client.focused_inactive $bg_alt $bg_alt $fg $bg_alt $bg_alt
client.unfocused        $bg_alt $bg_alt $fg $bg_alt $bg_alt
client.urgent           $red $red $fg $red $red
"""

(Path.home() / ".config/sway/colors.conf").write_text(sway)

kitty = f"""
font_family JetBrains Mono
font_size 12.0

cursor {theme["accent"]}
cursor_trail 3

background {theme["bg"]}
foreground {theme["fg"]}

background_opacity 0.95

selection_background {theme["accent"]}
selection_foreground {theme["bg"]}

# base colors
color0 {theme["bg"]}
color1 {theme["red"]}
color2 {theme["green"]}
color3 {theme["yellow"]}
color4 {theme["blue"]}
color5 {theme["purple"]}
color6 {theme["cyan"]}
color7 {theme["fg_dim"]}

# bright colors
color8 {theme["bg_window"]}
color9 {theme["red"]}
color10 {theme["green"]}
color11 {theme["yellow"]}
color12 {theme["blue"]}
color13 {theme["purple"]}
color14 {theme["cyan"]}
color15 {theme["fg"]}

window_padding_width 15
"""

(Path.home() / ".config/kitty/theme.conf").write_text(kitty)

wofi = f"""
@define-color bg {theme["bg"]};
@define-color bg_window {theme["bg_window"]};
@define-color fg {theme["fg"]};
@define-color fg_dim {theme["fg_dim"]};
@define-color accent {theme["accent"]};
@define-color border {theme["border"]};
"""

(Path.home() / ".config/wofi/colors.css").write_text(wofi)

