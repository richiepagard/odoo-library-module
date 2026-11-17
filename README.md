# Odoo Library Module

A custom Odoo 19 module for managing a small library's books and authors.

![Odoo](https://img.shields.io/badge/Odoo-19-714B67?style=for-the-badge&logo=odoo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## Features

- Manage books and their details
- Manage authors and their personal information
- Associate multiple authors with multiple books
- Track book availability as **Available** or **Lost**
- Automatically calculate a book's age from its publication year
- Prevent publication years from being set in the future
- Search books by title, ISBN, or author
- Filter books by availability
- Search authors by full name
- Automatically count the number of books associated with an author

## Models

### `library.book`

| Field | Type | Description |
|---|---|---|
| Title | Char | Book title |
| Authors | Many2many | Authors associated with the book |
| ISBN | Char | International Standard Book Number |
| Publication Year | Integer | Year the book was published |
| Age | Computed | Age calculated from the publication year |
| Pages | Integer | Number of pages |
| State | Selection | Available or lost |
| Active | Boolean | Whether the book record is active |
| Description | Text | Additional book information |

### `library.author`

| Field | Type | Description |
|---|---|---|
| Full Name | Char | Author's full name or nickname |
| Birth Year | Integer | Author's birth year |
| Active | Boolean | Whether the author is active |
| Books | Many2many | Books associated with the author |
| Books Count | Computed | Number of associated books |

## Requirements

- Odoo 19
- Python 3
- PostgreSQL
- A working Odoo development environment

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/richiepagard/odoo-library-module.git
   ```

2. Copy or add the module directory to an Odoo addons path:

   ```bash
   addons_path=/path/to/odoo/addons,/path/to/odoo-library-module
   ```

3. Restart the Odoo server:

   ```bash
   ./odoo-bin -c /path/to/odoo.conf
   ```

4. Enable developer mode from the Odoo settings.

5. Open **Apps**, update the apps list, search for **Library**, and install the module.

## Usage

After installation:

1. Open the **Library** application.
2. Create author records under **Library → Authors**.
3. Create book records under **Library → Books**.
4. Assign one or more authors to each book.
5. Use the available or lost filters to manage book status.

## Module Structure

```text
odoo-library-module/
├── library/
│   ├── models/
│   │   ├── author.py
│   │   └── book.py
│   ├── security/
│   │   └── ir.model.access.csv
│   ├── views/
│   │   ├── author_views.xml
│   │   └── book_views.xml
│   └── __manifest__.py
├── LICENSE
└── README.md
```

## Author

**Richie Pagard**

- GitHub: [@richiepagard](https://github.com/richiepagard)

## License

This project is licensed under the [MIT License](LICENSE).
