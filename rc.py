percol.view.CANDIDATES_LINE_BASIC    = ("on_default", "default")
percol.view.CANDIDATES_LINE_SELECTED = ("underline", "on_blue", "white","bold")
percol.view.CANDIDATES_LINE_MARKED   = ("bold", "on_cyan", "black")
percol.view.CANDIDATES_LINE_QUERY    = ("green", "bold")
percol.view.FIELD_SEP = ' <> '
percol.view.FOLDED = '…'

percol.import_keymap({
    "C-h" : lambda percol: percol.command.delete_backward_char(),
    "C-d" : lambda percol: percol.command.delete_forward_char(),
    "C-k" : lambda percol: percol.command.kill_end_of_line(),
    "C-y" : lambda percol: percol.command.yank(),
    "C-t" : lambda percol: percol.command.transpose_chars(),
    "C-a" : lambda percol: percol.command.beginning_of_line(),
    "C-e" : lambda percol: percol.command.end_of_line(),
    "C-b" : lambda percol: percol.command.backward_char(),
    "C-f" : lambda percol: percol.command.forward_char(),
    "M-f" : lambda percol: percol.command.forward_word(),
    "M-b" : lambda percol: percol.command.backward_word(),
    "M-d" : lambda percol: percol.command.delete_forward_word(),
    "M-h" : lambda percol: percol.command.delete_backward_word(),
    "C-n" : lambda percol: percol.command.select_next(),
    "C-p" : lambda percol: percol.command.select_previous(),
    "C-v" : lambda percol: percol.command.select_next_page(),
    "M-v" : lambda percol: percol.command.select_previous_page(),
    "M-<" : lambda percol: percol.command.select_top(),
    "M->" : lambda percol: percol.command.select_bottom(),
    "C-m" : lambda percol: percol.finish(),
    "C-j" : lambda percol: percol.finish(),
    "C-g" : lambda percol: percol.cancel(),
    "C-d" : lambda percol: percol.command.toggle_date(),
    "C-r" : lambda percol: percol.command.toggle_command(),
    "C-w" : lambda percol: percol.command.toggle_execdir(),
    "C-l" : lambda percol: percol.command.cwd_filter(),
    "C-q" : lambda percol: percol.finish_f(field=1),
    "C-y" : lambda percol: percol.finish_f(field=2),
})    