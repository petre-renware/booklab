"""
Booklab CLI module to assure system operatins as command line.

Usage:

    booklab -v
    booklab setup <options>
    booklab init <options>
    booklab server (run|stop|restart)
    booklab catalog
    booklab status <my-book>
    booklab new
    booklab build <my-book>
    booklab preview <my-book>
    booklab deploy <my-book>
    booklab page-edit <my-book>
    booklab page-upload <my-book>
    booklab page-upload <my-book>
    vooklab edit-nav[igation] <my-book>
    booklab pack <my-book>

Options:

    -l, --list    List books catalog
    -s, --status  Display detailes about a book
    -v, --version Display booklab application version

Architecture; Linux standard (POSIX) CLI implemented over "Typer" framework.

Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from booklab import __version__
from booklab.booklabd import api_app
import booklab.booklabd.routes as bksrv
import booklab.my_books.books_manager as mybkmgr
#TODO.dbg... nxt is just an exampla with a fake oaram
from .param_types import param_x
from .param_types import UserId  # param ... used for ...


#... test 4dbg
a: param_x = f"Test of param_x"
print(f"{a=} which is of {type(a)=}")


#TODO when use param UserId (TupeNew) 
#TODO is important to:
#    with api_app.app_context():
#  in order to use functions mapped on api/xxx/ routes
#  call as bksrv.<func(...)>
