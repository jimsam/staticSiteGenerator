from inline_code import text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_html_node(markdown):
    markdown_list = markdown_to_blocks(markdown)
    html_string = "<div>"
    for block in markdown_list:
        match block_to_block_type(block):
            case "paragraph":
                parent_node = ParentNode("p", block_to_htmlnodes(block))
                html_string += parent_node.to_html()
            case "code":
                leaf_node = LeafNode("code", block[3:-3])
                html_string += leaf_node.to_html()
            case "quote":
                blockquote_list = blockquote_to_htmlnodes(block)
                for quote in blockquote_list:
                    html_string += quote.to_html()
            case "unordered_list":
                parent_node = ParentNode("ul", block_list_to_htmlnodes(block))
                html_string += parent_node.to_html()
            case "ordered_list":
                parent_node = ParentNode("ol", block_list_to_htmlnodes(block, True))
                html_string += parent_node.to_html()
            case "heading":
                header_counter = get_header_number(block)
                parent_node = ParentNode(
                    f"h{header_counter}",
                    block_to_htmlnodes(block[header_counter + 1 :]),
                )
                html_string += parent_node.to_html()

    return f"{html_string}</div>"


def block_to_htmlnodes(block):
    textnode_list = text_to_textnodes(block)
    htmlnode_list = []
    for txtnode in textnode_list:
        htmlnode_instance = txtnode.text_node_to_html_node()
        htmlnode_list.append(htmlnode_instance)
    return htmlnode_list


def get_header_number(block):
    counter = 0
    for el in block:
        if el == " " and 0 < counter <= 6:
            break
        elif el == "#" and counter < 6:
            counter += 1

    return counter


def blockquote_to_htmlnodes(block):
    block_list = block.split("\n")
    htmlnode_list = []
    for quote in block_list:
        quote_content_list = block_to_htmlnodes(quote[2:])
        htmlnode_list.append(ParentNode("blockquote", quote_content_list))

    return htmlnode_list


def block_list_to_htmlnodes(block, is_ordered=False):
    block_list = block.split("\n")
    htmlnode_list = []
    for li in block_list:
        text = li[2:] if not is_ordered else li[3:]
        parent_node = ParentNode("li", block_to_htmlnodes(text))
        htmlnode_list.append(parent_node)

    return htmlnode_list


def markdown_to_blocks(markdown):
    block_list = []
    tmp_string = ""
    for line in markdown.split("\n"):
        line = line.strip()
        if line == "" and tmp_string == "":
            continue
        elif line == "":
            block_list.append(tmp_string.strip())
            tmp_string = ""
        else:
            tmp_string = f"{tmp_string}\n{line}"
    if tmp_string != "":
        block_list.append(tmp_string.strip())

    return block_list


def block_to_block_type(str_block):
    if is_heading(str_block[:6]):
        return "heading"
    elif is_code(str_block[:3], str_block[-3:]):
        return "code"
    elif is_quote(str_block):
        return "quote"
    elif is_unordered_list(str_block):
        return "unordered_list"
    elif is_ordered_list(str_block):
        return "ordered_list"
    return "paragraph"


def is_heading(str_to_check):
    counter = 0
    for el in str_to_check:
        if el == " " and 0 < counter <= 6:
            return True
        elif el == "#" and counter < 6:
            counter += 1
        else:
            return False
    return False


def is_code(part1_to_check, part2_to_check):
    return part1_to_check == "```" and part1_to_check == part2_to_check


def is_quote(str_block_to_check):
    for block in str_block_to_check.split("\n"):
        if block[0] != ">":
            return False
    return True


def is_unordered_list(str_block_to_check):
    for block in str_block_to_check.split("\n"):
        if block[:2] == "* " or block[:2] == "- ":
            return True
    return False


def is_ordered_list(str_block_to_check):
    counter = 1
    for block in str_block_to_check.split("\n"):
        if block[:3] != f"{counter}. ":
            return False
        counter += 1
    return True
