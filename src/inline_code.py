import re

from textnode import TextNode


def text_to_textnodes(text):
    textnode = TextNode(text, "text")
    response_list = split_nodes_delimiter([textnode], "`", "code")
    response_list = split_nodes_delimiter(response_list, "**", "bold")
    response_list = split_nodes_delimiter(response_list, "*", "italic")
    response_list = split_nodes_images(response_list)
    response_list = split_nodes_links(response_list)
    return response_list


def split_nodes_delimiter(old_node, delimiter, text_type):
    new_list = []
    for txtnode in old_node:
        if isinstance(txtnode, TextNode):
            inner_txt_list = txtnode.text.split(delimiter)
            if len(inner_txt_list) == 1:
                new_list.append(txtnode)
            else:
                for i in range(len(inner_txt_list)):
                    if i % 2 == 0:
                        new_list.append(
                            TextNode(inner_txt_list[i], txtnode.text_type, txtnode.url)
                        )
                    else:
                        new_list.append(
                            TextNode(inner_txt_list[i], text_type, txtnode.url)
                        )
        else:
            raise ValueError(f"This is what tried to evaluate: {txtnode}")
    return new_list


def split_nodes_images(old_nodes):
    new_list = []
    for txtnode in old_nodes:
        match_list = extract_markdown_images(txtnode.text)
        last_matched_item = match_list[-1:]
        parts = None
        if len(match_list) == 0:
            new_list.append(txtnode)
            continue
        for match in match_list:
            if parts is None:
                parts = txtnode.text.split(f"![{match[0]}]({match[1]})", 1)
            else:
                parts = parts.split(f"![{match[0]}]({match[1]})", 1)
            if parts[0] != "":
                new_list.append(TextNode(parts[0], "text"))
            new_list.append(TextNode(match[0], "image", match[1]))
            if len(parts) > 1:
                parts = parts[1]
        last_part = txtnode.text.split(
            f"![{last_matched_item[0][0]}]({last_matched_item[0][1]})", 1
        )
        if len(last_part) > 1 and last_part[1] != "":
            new_list.append(TextNode(last_part[1], "text"))
    return new_list


def split_nodes_links(old_nodes):
    new_list = []
    for txtnode in old_nodes:
        match_list = extract_markdown_links(txtnode.text)
        last_matched_item = match_list[-1:]
        parts = None
        if len(match_list) == 0:
            new_list.append(txtnode)
            continue
        for match in match_list:
            if parts is None:
                parts = txtnode.text.split(f"[{match[0]}]({match[1]})", 1)
            else:
                parts = parts.split(f"[{match[0]}]({match[1]})", 1)
            new_list.append(TextNode(parts[0], "text"))
            new_list.append(TextNode(match[0], "link", match[1]))
            parts = parts[1]
        last_part = txtnode.text.split(
            f"![{last_matched_item[0][0]}]({last_matched_item[0][1]})", 1
        )
        if len(last_part) > 1 and last_part[1] != "":
            new_list.append(TextNode(last_part[1], "text"))
    return new_list


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
