import os
import shutil
from copystatic import static_copy
from gencontent import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    static_copy("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

#def generate_pages_recursive(content_dir, template_path, dest_dir):
#    for each_entry in os.listdir(content_dir):
#        from_path = os.path.join(content_dir, filename)
#        dest_path = os.path.join(dest_dir, filename)
#
#        if os.path.isfile(from_path):
#            dest_path = Path(dest_path).with_suffix(".html")
#            generate_page(from_path, template_path, dest_path)
#        else:
#            generate_pages_recursive("./content", "./template.html", "./public")



main()
