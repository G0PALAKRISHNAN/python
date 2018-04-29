from pywinauto.application import Application
import time

app = Application().start('notepad.exe')
time.sleep(4)
app.UntitledNotepad.menu_select("Help->About Notepad")
time.sleep(4)
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto works!", with_spaces= True)
time.sleep(4)
app.UntitledNotepad.menu_select("File->Save")
time.sleep(3)
app.SaveAs.Edit.type_keys("Welcome.txt")
time.sleep(3)
app.SaveAs.Save.click()
time.sleep(3)
app.UntitledNotepad.menu_select("File->Exit")
time.sleep(3)