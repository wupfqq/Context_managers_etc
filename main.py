#without context managers or 'with'
def editf(fname,text):
    assert type(fname) is str
    openf=open(fname,'wr')
    try:
        openf.write(str(text))
        openf.read()
    finally:
        openf.close()

#with threads and threading lock
from threading import Lock

def tl_editf(fname,text):
    lfile=Lock()
    lfile.acquire()  #close thread
    try:
        lfile.write(str(text))
        lfile.read()
    finally:
        lfile.release()




