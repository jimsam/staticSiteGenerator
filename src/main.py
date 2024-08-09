import os
import shutil

from generator import generate_page, generate_page_recursive


def prepare_public(source_str, dest_str):
    shutil.rmtree(dest_str)
    copy_recursively(source_str, dest_str)


def copy_recursively(source_str, dest_str):
    os.mkdir(dest_str)
    for item in os.listdir(source_str):
        if os.path.isfile(f"{source_str}/{item}"):
            shutil.copy(f"{source_str}/{item}", dest_str)
        else:
            new_source = f"{source_str}/{item}"
            new_dest = f"{dest_str}/{item}"
            copy_recursively(new_source, new_dest)


def main():
    prepare_public("static", "public")
    generate_page_recursive("context", "template.html", "public")


if __name__ == "__main__":
    main()
