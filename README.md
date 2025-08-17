# FormatSelectionAsFileURL – Notepad++ PythonScript

Convert highlighted Windows or UNC paths into clickable `file:///...` links directly inside Notepad++.

## Overview
This script formats selected text—Windows drive paths like `C:\...`, UNC paths like `\\server\share\...`, or existing `file://` URLs—into a normalized, percent‑encoded `file:///...` URL that Notepad++ recognizes as clickable. Double‑click the link to open the target file with its associated application.

## Features
- Converts backslashes to forward slashes and encodes spaces as `%20`.
- Supports Windows drive paths, UNC network paths, and existing `file://` URLs.
- Compatible with Python 2.7 (default in many Notepad++ PythonScript setups).

## Requirements
- Notepad++
- PythonScript plugin
- Clickable links enabled: **Settings → Preferences → Cloud & Link → Clickable Link Settings → Enable**

## Installation
1. In Notepad++: **Plugins → Plugins Admin → Python Script → Install** (then restart).
2. Create a new script: **Plugins → Python Script → New Script…**, name it `FormatSelectionAsFileURL.py`.
3. Paste the code from `FormatSelectionAsFileURL.py` (included in this repo) and save.
4. (Optional) Add to menu and assign a shortcut:
   - **Plugins → Python Script → Configuration…** → move script into *Menu items* → **OK** → restart.
   - **Settings → Shortcut Mapper… → Plugin commands** → select your script → **Modify** → choose keys.

## Usage
1. Paste or type a file path (e.g., `C:\Users\You\My File.txt`).  
2. Select the path text.  
3. Run the script (menu or shortcut).  
4. The selection becomes a clickable `file:///...` URL.  
5. Double‑click to open.

## Example
**Before**  
```
C:\Users\sprin\OneDrive - supersprinkle.com\Documents\UMGC\VSCode\message.py
```

**After**  
```
file:///C:/Users/sprin/OneDrive%20-%20supersprinkle.com/Documents/UMGC/VSCode/message.py
```

## License
MIT — see `LICENSE` or add your preferred license.

## Notes
- If you encounter `SyntaxError: Non-ASCII character '\xe2'` on Python 2.7, ensure the first line of the script declares UTF‑8: `# -*- coding: utf-8 -*-`.
