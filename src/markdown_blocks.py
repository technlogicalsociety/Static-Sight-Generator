from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []
    pieces = markdown.split("\n\n")

    for piece in pieces:
        cleaned = piece.strip()
        if cleaned != "":
            blocks.append(cleaned)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST ="undordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if len(lines) == 1:
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        if count >= 1 and count <= 6:
            if len(block) > count and block[count] == " ":
                return BlockType.HEADING

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False

    if is_quote:
        return BlockType.QUOTE

    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
    if is_unordered:
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for i in range(len(lines)):
        expected = f"{i + 1}. "
        if not lines[i].startswith(expected):
            is_ordered = False

    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

#def markdown_to_html_node(markdown):
 #   blocks = markdown_to_blocks(markdown)
  #  children = []
   # for block in blocks:
    #    html_node = block_to_block_type(block)
     #   children.append("div", children, None)

def block_to_html_nodes(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
         return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
         return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
         return code_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
         return olist_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
         return ulist_to_html_node(block)
    elif block_type == BlockType.QUOTE:
         return quote_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_nodes(block))
    return ParentNode("div", children)

def paragraph_to_html_node(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html_node(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    text = block[count + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{count}", children)

def code_to_html_node(block):
    text = block[4:-3]
    node = TextNode(text, TextType.TEXT)
    inner_node = text_node_to_html_node(node)
    return ParentNode("pre", [ParentNode("code", [inner_node])])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line[2:])
    text = "\n".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    lines = block.split("\n")
    new_lines =  []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        new_lines.append(ParentNode("li", children))
    return ParentNode("ul", new_lines)

def olist_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        text = line[line.find(". ") + 2:]
        children = text_to_children(text)
        new_lines.append(ParentNode("li", children))
    return ParentNode("ol", new_lines)

#            if block_type == BlockType.PARAGRAPH:
 #               return children.append(paragraph_to_html_node(block))
 #           elif block_type == BlockType.HEADING
  #              return children.append(heading_to_html_node(block))
   #         elif block_type == BlockType.CODE:
    #            return chidlren.append(code_to_html_node(block))
     #       elif block_type == BlockType.ORDERED_LIST:
      #          return children.append(olist_to_html_node(block))
       ##     elif block_type == BlockType.UNORDERED_LIST:
         #       return children.append(ulist_to_html_node(block))
          #  elif block_type == BlockType.QUOTE
           #     return children.append(quote_to_html_node(block))
#
# This part of the project I learned that i could have used a helper function instead of a chain of elifs
