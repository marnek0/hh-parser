# hh_gradio.spec
# PyInstaller spec-файл для сборки hh_gradio.py под Windows

import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Собираем все статические файлы Gradio (JS, CSS, шаблоны)
gradio_datas = collect_data_files("gradio", includes=["**/*"])
gradio_client_datas = collect_data_files("gradio_client", includes=["**/*"])

datas = gradio_datas + gradio_client_datas

# Скрытые импорты — Gradio грузит много всего динамически
hiddenimports = (
    collect_submodules("gradio")
    + collect_submodules("gradio_client")
    + [
        "uvicorn",
        "uvicorn.logging",
        "uvicorn.loops",
        "uvicorn.loops.auto",
        "uvicorn.protocols",
        "uvicorn.protocols.http",
        "uvicorn.protocols.http.auto",
        "uvicorn.protocols.websockets",
        "uvicorn.protocols.websockets.auto",
        "uvicorn.lifespan",
        "uvicorn.lifespan.on",
        "fastapi",
        "starlette",
        "anyio",
        "anyio._backends._asyncio",
        "anyio._backends._trio",
        "httpx",
        "httpcore",
        "openpyxl",
        "openpyxl.styles",
        "openpyxl.utils",
        "playwright",
        "playwright.sync_api",
        "aiofiles",
        "orjson",
        "python_multipart",
        "websockets",
        "pydantic",
    ]
)

a = Analysis(
    ["hh_gradio.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "matplotlib", "numpy", "pandas", "PIL"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="HH_Parser",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # False = без чёрного окна консоли
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon="icon.ico",      # Раскомментируй и добавь icon.ico если нужна иконка
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="HH_Parser",
)
