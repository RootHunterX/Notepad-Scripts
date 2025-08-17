# -*- coding: utf-8 -*-
"""
Format selected text (Windows path/UNC or file:// URL) into a clickable file:/// URL.
Usage:
 - Enable clickable links in Notepad++ Preferences → Cloud & Link.
 - Highlight a path and run this script from the PythonScript plugin (or via shortcut).
"""
from Npp import editor, notepad
import re

try:
    from urllib import quote  # Python 2.7
except ImportError:
    from urllib.parse import quote  # Fallback

def _encode_path(p):
    """Percent-encode unsafe characters but keep URL structural chars."""
    return quote(p, safe='/:._-~')

def to_file_url(text):
    s = text.strip().strip('"').strip("'")
    # Already a file URL? Normalize
    if s.lower().startswith('file:'):
        s = s.replace('\\', '/')
        # file://C:/... -> file:///C:/...
        if re.match(r'^file://[A-Za-z]:/', s):
            s = 'file:///' + s[7:]
        s = re.sub(r'^file:/{2,}([A-Za-z]:/)', r'file:///\1', s)
        return _encode_path(s)
    # UNC path
    if s.startswith('\\\\'):
        unc = s.lstrip('\\').replace('\\', '/')
        return 'file://' + _encode_path(unc)
    # Windows drive path
    if re.match(r'^[A-Za-z]:\\', s):
        norm = s.replace('\\', '/')
        return 'file:///' + _encode_path(norm)
    # Forward-slash drive or POSIX-like absolute
    if re.match(r'^[A-Za-z]:/', s) or s.startswith('/'):
        return 'file:///' + _encode_path(s.lstrip('/'))
    # Bare-ish path with spaces or slashes
    if re.search(r'[\\/\s]', s):
        norm = s.replace('\\', '/')
        return 'file:///' + _encode_path(norm.lstrip('/'))
    return s

def main():
    sel = editor.getSelText()
    if not sel:
        notepad.messageBox("Select a path or URL to format.", "Format as file:/// URL")
        return
    start = editor.getSelectionStart()
    url = to_file_url(sel)
    editor.beginUndoAction()
    try:
        editor.replaceSel(url)
    finally:
        editor.endUndoAction()
    # Reselect
    editor.setSelectionStart(start)
    editor.setSelectionEnd(start + len(url))

if __name__ == '__main__':
    main()
