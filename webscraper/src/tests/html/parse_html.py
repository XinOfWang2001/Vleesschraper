from zipfile import ZipFile

def get_html() -> str:
    location_html = "product.html"
    location_zip = "src/tests/html/html.zip"
    html = ""
    with ZipFile(location_zip, mode="r") as zip:
        with zip.open(location_html, mode="r") as file:
            html = file.read()
    return html