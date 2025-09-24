
[TOC]


# README JSON format

Ref database: `books_catalog.json`

## PysonDB required format

```
{
    "data": [
        {
            "id": 0,
            "code": "BCAT",
            "short_desc": "bk_tmpl",
            "description": "Sablonul implicit pentru o carte noua",
            "created_date": "2023-08-01",
            "created_by": "system",
            "notes": "Inregistrare obligatorie de la instalare sistem. Non editabila."
        }
    ]
}
```

The format is a _dict_ with key _"data"_ which contain _array with records_.




## Pandas & table-reader plugin required format

The accepted format (for `orient='records'` Pandas spec of `read_json()` function) is:

```
[
    {
        "id": 0,
        "code": "BCAT",
        "short_desc": "bk_tmpl",
        "description": "Sablonul implicit pentru o carte noua",
        "created_date": "2023-08-01",
        "created_by": "system",
        "notes": "Inregistrare obligatorie de la instalare sistem. Non editabila."
    }
]
```



## Possible quick-dev solutions

### 1. let PysonDB format and convert before load table with `table-reader`

* before execute `{{ read_json('../data/books_catalog.json', orient='records') }}`
* insert a python static code to extract from PysonDB format just key `"data"` and
    * return its value to `read_json()` function instead reading from file
    * or create a temporary file with this string saved and use it in `read_json()` function


