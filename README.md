# Odoo Library Module Collection

A collection of custom Odoo 19 addons that work together to manage a library and provide reusable location, Markdown, and Persian font support.

![Odoo](https://img.shields.io/badge/Odoo-19-714B67?style=for-the-badge&logo=odoo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## Modules

| Module | Purpose |
|---|---|
| `library` | Main library application for books and authors |
| `base_location` | Reusable country, state, and city records |
| `markdown_field` | Markdown toolbar and rendering support for text fields |
| `web_farsi_font` | Persian/Farsi font support in the Odoo backend |

## Library Features

- Manage books and authors
- Link multiple authors to books
- Track books as available or lost
- Calculate book age from publication year
- Store Markdown descriptions and biographies
- Add author country, state, and city information
- Search and filter books and authors

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/richiepagard/odoo-library-module.git
   ```

2. Add the repository directory to the Odoo `addons_path`.

3. Restart Odoo and update the Apps list.

4. Install **Library**. Its required addons—`base_location` and `markdown_field`—will be used automatically.

`web_farsi_font` installs automatically as a hidden backend addon.

## Module Structure

```text
odoo-library-module/
├── library/
├── base_location/
├── markdown_field/
├── web_farsi_font/
├── LICENSE
└── README.md
```

## Requirements

- Odoo 19
- Python 3
- PostgreSQL

## Author

**Richie Pagard** — [@richiepagard](https://github.com/richiepagard)

## License

Licensed under the [MIT License](LICENSE).
