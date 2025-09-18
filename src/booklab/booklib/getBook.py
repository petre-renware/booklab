
import pysondb


def getBook(
    db: pysondb,
    book_code: str
) -> list[dict] | None:
    """
    Check for a given book code:

    * test if book code is not None
    * test if book code exists in database and is exactly 1 record
    * if both conditions return that record as List[Dict]
    * if not any condition return None

    Return:

    list of dictionary wiyh found record
    """
    pass  # code from here ...




