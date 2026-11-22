{
    "name": "Farsi Font",
    "summary": "Loads the Farsi font for Persian text in the Odoo backend",
    "version": "19.0.1.0.0",
    "category": "Hidden",
    "author": "Richie Pagard",
    "website": "https://github.com/richiepagard",
    "license": "LGPL-3",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "web_farsi_font/static/src/css/farsi_font.css",
        ],
    },
    "installable": True,
    "auto_install": True,
}
