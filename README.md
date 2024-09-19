# PyQt5 Application for Maua Jr

## Installation

### Prerequisites

- Python 3.x
- Packages inside requirements.txt

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Run the application

```bash
py app.py
```

### Build de EXE using Pyinstaller:

windows:

```
pyinstaller --name MyAppName --icon assets/icons/icon.ico --onefile --windowed --add-data "assets;assets" app.py
```

linux/mac:

```
pyinstaller --name MyAppName --icon assets/icons/icon.ico --onefile --windowed --add-data "assets:assets" app.py
```

## Contributors

- [@Thiago-Heleno](https://github.com/Thiago-Heleno) - Frontend
