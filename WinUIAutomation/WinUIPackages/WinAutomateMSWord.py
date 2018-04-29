import win32com.client as win32
from time import sleep

RANGE = range(3,8)

def Word():
    xl = win32.gencache.EnsureDispatch("Word.Application")
    doc = Word.Documents.Add()
    Word.Visible =True
    sleep(1)

    rng = doc.Range(0,0)
    rng.InsertAfter("Hacking word with Python\r\n\r\n")
    sleep(1)
    for i in RANGE:
        rng.InsertAfter("Line %d\r\n"%i)
        sleep(1)
    rng.InsertAfter("\r\nPython rules!\r\n")

    doc.Close(False)
    Word.Applicatiom.Quit()
if __name__ == '__main__':
    Word()