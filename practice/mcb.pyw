# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw remove - Deletes all keywords.
import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'clear':
        mcbShelf.clear()
    elif sys.argv[1].lower() in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()