import glob
from nbconvert import MarkdownExporter
from nbconvert.utils.exceptions import ConversionException
import os
import nbformat
import yaml
import sys
import subprocess
from hashlib import sha256
import concurrent.futures, traceback, re
from dataclasses import dataclass, asdict
from typing import Any, Optional

if __name__ == "__main__":
    from progress_bar import ProgressBar
else:
    from scripts.progress_bar import ProgressBar


###########################################
### Section for Constants and Patterns  ###
###########################################

"""
=============================================================
SIDE-BY-SIDE RUNNER LEGEND (Container Panel Composition)
=============================================================

Supported cell directives for side-by-side layout:
- CODE_RUNNER (python/javascript/java comment marker)
- UI_RUNNER   (HTML comment marker)
- GAME_RUNNER (javascript comment marker)

Shared panel options (append after `|` in directive comment):
- panel: <panel_id>       Required to opt into pairing.
- slot: left|right        Which side this runner occupies. Defaults:
                                                    CODE_RUNNER -> left, UI_RUNNER -> left, GAME_RUNNER -> right.
- layout: row|column      Panel direction. Default: row.
- ratio: A-B              Column/row split. Examples: 40-60, 1fr-2fr. Default: 50-50.
- gap: <css-size>         Spacing between sides. Default: 1rem.

Pairing behavior:
- Runners with the same panel id are queued until both left and right slots exist.
- When both slots are present, a single `container-panel.html` include is emitted.
- If only one slot is ever provided, content is emitted standalone at flush time.
- Last writer wins for layout/gap/ratio if options differ within the same panel id.

Examples:
- // CODE_RUNNER: Challenge text | panel: demo, slot: left, ratio: 35-65
- <!-- UI_RUNNER: Notes | panel: demo, slot: left -->
- // GAME_RUNNER: Arcade mode | panel: demo, slot: right, layout: row

Real pair example (Cookie Clicker):
- <!-- UI_RUNNER: How to Play panel | panel: cookie_intro_game, slot: left, layout: row, ratio: 20-80, gap: 1rem -->
- // GAME_RUNNER: Cookie Clicker Mini Game with large cookie | hide_edit: true, panel: cookie_intro_game, slot: right, layout: row, ratio: 20-80, gap: 1rem, width: 100%, height: 520px

Runner options:
- autostart: true|false  Auto-runs the game when the runner initializes. Default: false.

Game-runner specific options:
- hide_edit, width, height, editor_height

Notes on CodeFence and MermaidGraph:
- Plain markdown code fences and Mermaid markdown are not panel-aware by default.
- To place those side-by-side, wrap desired content in a panel-aware runner cell
    (for example, UI_RUNNER HTML shell plus panel options), then pair by panel id.
"""

notebook_directory = "_notebooks"
destination_directory = "_posts"
mermaid_output_directory = "assets/mermaid"

# Comment patterns for different languages
CODE_RUNNER_PATTERNS = {
    'javascript': r'^//\s*CODE_RUNNER:\s*(.+)$',
    'python': r'^#\s*CODE_RUNNER:\s*(.+)$',
    'java': r'^//\s*CODE_RUNNER:\s*(.+)$',
}

# UI_RUNNER pattern for HTML cells
UI_RUNNER_PATTERN = r'^<!--\s*UI_RUNNER:\s*(.+)\s*-->$'

# GAME_RUNNER pattern for GameEngine cells (JavaScript only)
GAME_RUNNER_PATTERN = r'^//\s*GAME_RUNNER:\s*(.+)$'

# PSEUDOCODE_RUNNER pattern for Pseudocode examples (raw or code cells)
PSEUDOCODE_RUNNER_PATTERN = r'^//\s*PSEUDOCODE_RUNNER:\s*(.+)$'


#########################################
### Section for Core Helper Functions ###
#########################################

# [rest of file unchanged]
