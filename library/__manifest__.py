{
    ### Module information ###
    "name": "library",
    "summary": "Manage books in a small library",
    "description": """
        Small library to manage books and its properties
        such as its authors.
        """,
    "application": True,

    ### Author information and License ###
    "author": "Richie Pagard",
    "website": "https://github.com/richiepagard",
    "license": "LGPL-3",

    ### Necessary modules ###
    "depends": ["base", "base_location", "markdown_field"],

    ### Module category and version ###
    "category": "Uncategorized",
    "version": "19.0.1.0.0",

    ### Data Loaded ###
    "data": [
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/author_views.xml",
    ],

}
