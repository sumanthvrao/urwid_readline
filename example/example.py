import urwid
import urwid_readline

def show_or_exit(key):
    if key in ('ctrl q', 'ctrl Q'):
        raise urwid.ExitMainLoop()
    txt.set_text('unknown key: ' + repr(key))

txt = urwid_readline.ReadlineEdit('')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()