
import pysondb


def getBook(
    db: pysondb,
    book_code: str
) -> dict | None:
    """
    Check for a given book code:

    * test if book code is not None
    * test if book code exists in database and is exactly 1 record
    * if both conditions return that record as List[Dict]
    * if not any condition return None

    Return:

    * `dict(pysondb)` with found record
    * `None` if any condition is not met
    """
    if not book_code or not isinstance(book_code, str):
        return None # exit because not satisfying basic requirements
    # check to see if record exists and if then just select first got
    bk_rec = None
    bk_rec = db.getBy({"code":book_code})
    if bk_rec and isinstance(bk_rec, list):
        return bk_rec[0]
    return None

