#without context managers or 'with'
def editf(fname,text):
    assert type(fname) is str
    openf=open(fname,'w')
    try:
        openf.write(str(text))
    finally:
        openf.close()

        fname.release()

#with 'with'
def w_editf(fname,text):
    with(open(fname,'w+')) as ff:
        ff.write(str(text))

#with context_manager
class CM_openf:
    def __init__(self,fname,text):
        assert type(fname) is str
        self.fname=fname
    def __enter__(self):
        self.tfile=open(self.fname,'w')
        return self.tfile
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fname:
           self.tfile.close()

def cm_editf(fname, text):
    with CM_openf(fname, text) as cmf:
       cmf.write(str(text))

#with CM decorator
from contextlib import contextmanager
@contextmanager #позволяет вызывать с with
def d_editf(fname,text):
    try:
        fo=open(fname,'w')
        yield fo
    finally:
        fo.close()

def dec_editf(fname, text):
    with d_editf(fname, text) as cmf:
       cmf.write(str(text))

cm_editf('example.txt',"I like pumpkin pie!")
a=open('example.txt')
print(a.read())