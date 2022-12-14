from tkinter import *
from tkinter import font 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import subprocess


BACKGROUND = '#404040'
FOREGROUND = '#ffe6cc'
FONT = 'Arial 13'
ACTIVE_BACKGROUND = '#6600cc'
BAR_BACKGROUND = '#007acc'
BAR_FOREGROUND = '#595959'
filename = ''
gpath = ''



#File Functions

# New file
def _new(*args):
    editor.delete('1.0', END)

# Open file
def _open(*args):
    editor.delete('1.0', END)
    openfile = filedialog.askopenfilename(title='Բացել Ֆայլը', filetypes=(('Տեքստային Ֆայլեր', '*.txt'), ('Փայթնի Ֆայլեր', '*.py'),('Շեմի Ֆայլեր', '*.scm'), ('Բոլոր Ֆայլեր', '*.*')))
    if openfile:
        _file = open(openfile, 'r')
        data = _file.read()
        editor.insert(END, data)
        global gpath
        gpath = openfile
        _file.close()
    
    else:
        return

# Save file
def _save(*args):
        filename = "input.txt"
        filename = open(filename, 'w')
        filename.write(editor.get('1.0', END))
        filename.close()


# Save As
def _saveas(*args):
    filename = filedialog.asksaveasfilename(defaultextension='*.txt', title='Պահպանել Ֆայլը', filetypes=(('Տեքստային Ֆայլեր', '*.txt'), ('Փայթնի Ֆայլեր', '*.py'),('Շեմի Ֆայլեր', '*.scm'),  ('Բոլոր Ֆայլեր', '*.*')))
    if filename:
        filename = open(filename, 'w')
        filename.write(editor.get('1.0', END))
        filename.close()
# Exit
def _exit(*args):
    user = messagebox.askyesno('Զգուշացում', 'Դուք ցանկանում եք դուրս գալ՞')
    if user > 0:
        root.destroy()
    
    else:
        return



#Edit Functions

# Copy
def _copy(*args):
    editor.event_generate('<<Պատճենել>>')

# Cut
def _cut(*args):
    editor.event_generate('<<Կտրել>>')

# Paste
def _paste(*args):
    editor.event_generate('<<Տեղադրել>>')

# Undo
def _undo(*args):
    pass



#Run Functions

# run file
def _runfile():
    global gpath
    filer = "interpreter.py"
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Please save the file first")
        msg.pack()
        return
    command = f'python3 {filer}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    result.delete('1.0','end')
    result.insert('1.0',outputResult)
    result.insert('1.0',error)


#View Functions

# default theme
def _defaulttheme():
    BACKGROUND = '#ffffff'
    FOREGROUND = '#000000'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    result.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# atom dark theme
def _atomdark():
    BACKGROUND = '#282c34'
    FOREGROUND = '#ffffff'
    ACTIVE_BACKGROUND = '#3e4451'
    BAR_BACKGROUND = '#21252b'
    BAR_FOREGROUND = '#9da5b4'
    root.config(background=BAR_BACKGROUND)
    result.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# dark theme
def _darktheme():
    BACKGROUND = '#1e1e1e'
    FOREGROUND = '#d4d4d4'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    result.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# solarised light theme
def _solartheme():
    BACKGROUND = '#fdf6e3'
    FOREGROUND = '#333333'
    ACTIVE_BACKGROUND = '#eee8d5'
    BAR_BACKGROUND = '#eee8d5'
    BAR_FOREGROUND = '#586e75'
    root.config(background=BAR_BACKGROUND)
    result.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)

# hacker theme
def _hackertheme():
    BACKGROUND = '#0F0F0F'
    FOREGROUND = '#33FF33'
    ACTIVE_BACKGROUND = '#add6ff'
    BAR_BACKGROUND = '#007acc'
    BAR_FOREGROUND = '#ffffff'
    root.config(background=BAR_BACKGROUND)
    result.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    editor.config(background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND)
    statusbar.config(background=BAR_BACKGROUND, foreground=BAR_FOREGROUND)
# default font
def _defaultfont():
    FONT = 'Arial 13'
    editor.config(font=FONT)

# times font
def _timesfont():
    FONT = 'Times 13'
    editor.config(font=FONT)

# system font
def _systemfont():
    FONT = 'System 13'
    editor.config(font=FONT)
# helvetica font
def _helveticafont():
    FONT = 'Helvetica 13'
    editor.config(font=FONT)

# fixedsys font
def _fixedsysfont():
    FONT = 'fixedsys 13'
    editor.config(font=FONT)


#Help Functions

def _about():
    pass


#Shorcuts function
def shortcuts():
    editor.bind('<Control-n>', _new)
    editor.bind('<Control-o>', _open)
    editor.bind('<Control-s>', _save)
    editor.bind('<Control-k>', _saveas)
    editor.bind('<Control-c>', _copy)
    editor.bind('<Control-x>', _cut)
    editor.bind('<Control-v>', _paste)
    editor.bind('<Control-u>', _undo)


root = Tk()
root.title('Sheme compiler')
root.geometry('1200x600+200+50')

statusbar = Label(root, text='x,y\tScheme\t', anchor=E)
statusbar.pack(fill=X, side=BOTTOM)

main_frame = Frame(root)
main_frame.pack(padx=(5,460), pady=(5,5))
 

 
res_frame = Frame(root, bg="#f5f5f5")
res_frame.place(relx=0.5, rely=0.01, relheight=0.94, relwidth=0.37, x =150)


scrollbar_ = Scrollbar(res_frame)
scrollbar_.pack(side=RIGHT, fill=Y)

scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT, fill=Y)

result = editor = Text(res_frame, width=500, height=550, font=FONT, background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND, yscrollcommand=scrollbar.set)
editor.pack(expand=True, fill=BOTH)
shortcuts()

editor = Text(main_frame, width=500, height=550, font=FONT, background=BACKGROUND, foreground=FOREGROUND, selectbackground=ACTIVE_BACKGROUND, selectforeground=FOREGROUND, yscrollcommand=scrollbar.set)
editor.pack(expand=True, fill=BOTH)
shortcuts()

scrollbar_.config(command=result.yview)

scrollbar.config(command=editor.yview)

menu_bar = Menu(root)
'''
File Menu
'''
def _file():
    file = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Ֆայլ', menu=file)
    file.add_command(label='Նոր', accelerator='Ctrl+N', command=_new)
    file.add_command(label='Բացել', accelerator='Ctrl+O', command=_open)
    file.add_command(label='Պահպանել', accelerator='Ctrl+S', command=_save)
    file.add_command(label='Պահպանել ինչպես', accelerator='Ctrl+K', command=_saveas)
    file.add_separator()
    file.add_command(label='Դուրս գալ', command=_exit)

'''
Edit Menu
'''
def _edit():
    edit = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Խմբագրել', menu=edit)
    edit.add_command(label='Հետ', accelerator='Ctrl+U', command=_new)
    edit.add_separator()
    edit.add_command(label='Կտրել', accelerator='Ctrl+X', command=_cut)
    edit.add_command(label='Պատճենել', accelerator='Ctrl+C', command=_copy)
    edit.add_command(label='Տեղադրել', accelerator='Ctrl+V', command=_paste)
    edit.add_separator()

'''
Run Menu
'''
def _run():
    run = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Աշխատացնել', menu=run)
    run.add_command(label='Աշխատացնել', accelerator='F5', command=_runfile)


'''
View Menu
'''
def _view():
    view = Menu(menu_bar, tearoff=0)

    appear = Menu(view, tearoff=0)
    appear.add_command(label='Լռելայն', command=_defaulttheme)
    appear.add_command(label='Ատոմի մութ', command=_atomdark)
    appear.add_command(label='Մութ', command=_darktheme)
    appear.add_command(label='Արևային լույս', command=_solartheme)
    appear.add_command(label='Հաքեր', command=_hackertheme)

    fonts = Menu(view, tearoff=0)
    fonts.add_command(label='Լռելայն', command=_defaultfont)
    fonts.add_command(label='Թայմս', command=_timesfont)
    fonts.add_command(label='Սիստեմ', command=_systemfont)
    fonts.add_command(label='Հելվետիկա', command=_helveticafont)
    fonts.add_command(label='Ֆիքսդսիս', command=_fixedsysfont)

    view.add_cascade(label='Ոճ', menu=appear)
    view.add_cascade(label='Տառաչափեր', menu=fonts)

    menu_bar.add_cascade(label="Տեսք", menu=view)

# call functions
_file()
_edit()
_run()
_view()
root.config(menu = menu_bar)
root.mainloop()
