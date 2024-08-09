import os

from block_code import markdown_to_html_node


def extract_title(markdown):
    if markdown[0] != "#":
        raise ValueError("No title found!")
    return markdown[2:]


def generate_page(from_path, template_path, dest_path):
    dest_directory = os.path.dirname(dest_path)
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, mode="r") as f:
        from_content = f.read()
    with open(template_path, mode="r") as f:
        template_content = f.read()

    header = extract_title(from_content.split("\n")[0])
    html_string = markdown_to_html_node(from_content)
    template_content = template_content.replace("{{ Title }}", header)
    template_content = template_content.replace("{{ Content }}", html_string)
    with open(f"{dest_directory}/index.html", mode="w") as f:
        f.write(template_content)


def generate_page_recursive(from_path, template_path, dest_path):

    if not os.path.exists(from_path):
        os.mkdir(from_path)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for item in os.listdir(from_path):
        if os.path.isfile(f"{from_path}/{item}"):
            generate_page(f"{from_path}/{item}", template_path, f"{dest_path}/{item}")
        else:
            new_source = f"{from_path}/{item}"
            new_dest = f"{dest_path}/{item}"
            generate_page_recursive(new_source, template_path, new_dest)
