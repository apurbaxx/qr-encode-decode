Problem statement
-----------------
People often need a quick, local tool to create and read QR codes without relying on online services. Existing solutions may be heavier than necessary or require graphical environments; a lightweight, terminal-based app that generates and decodes QR codes is useful for simple workflows and scripting.

Scope of the project
--------------------
- Provide an interactive, terminal-based application to generate (encode) and read (decode) QR codes.
- Support saving generated QR codes as PNG files with auto-generated filenames.
- Support decoding QR codes from common image formats and returning their text content.
- Keep the implementation lightweight: use `qrcode`, `Pillow`, and `pyzbar` only.
- Keep the UX simple and focused on local usage (no networking, no GUI required).

Target users
------------
- Developers and power users who need a quick CLI tool to generate or scan QR codes.
- Students or hobbyists learning about QR codes and simple Python tooling.
- Scripters who want to automate QR generation or decoding as part of local workflows.

High-level features
-------------------
- Interactive terminal menu with options to Generate, Read, or Exit.
- QR generation from arbitrary text with PNG output and optional image preview.
- QR decoding from an image file; supports multiple QR codes in one image.
- Minimal dependency list and simple installation via `requirements.txt`.
- Clear, concise messages and prompts for easy use in the terminal.