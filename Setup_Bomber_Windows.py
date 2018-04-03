from distutils.core import setup
import py2exe

setup(
    data_files = ["Cenario_1"],
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "bundle_files": 3,
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False
                          }
               },
    zipfile = None,         
    windows = [
        {
            "script": 'Menu.py',
			"icon_resources": [(1, "Sprites\icon.ico")]
        }
    ],
)

