import re

def markdown_to_html(text):
    lines = text.split("\n")
    result = []
    in_list = False
    for line in lines:
        match = re.match(r"^\d+\. (.*)", line)
        if match:
            if not in_list:
                result.append("<ol>")
                in_list = True

            result.append("<li>" + match.group(1) + "</li>")
        else:
            if in_list:
                result.append("</ol>")
                in_list = False
            if line.startswith("### "):
                line = "<h3>" + line[4:] + "</h3>"
            elif line.startswith("## "):
                line = "<h2>" + line[3:] + "</h2>"
            elif line.startswith("# "):
                line = "<h1>" + line[2:] + "</h1>"
            line = re.sub(
                r"!\[(.*?)\]\((.*?)\)",
                r'<img src="\2" alt="\1"/>',
                line )

            line = re.sub(
                r"\[(.*?)\]\((.*?)\)",
                r'<a href="\2">\1</a>',
                line )

            line = re.sub(
                r"\*\*(.*?)\*\*",
                r"<b>\1</b>",
                line )

            line = re.sub(
                r"\*(.*?)\*",
                r"<i>\1</i>",
                line)

            result.append(line)
    if in_list:
        result.append("</ol>")

    return "\n".join(result)


#testes
print(markdown_to_html("# Exemplo"))
print(markdown_to_html("Este é um **exemplo**."))
print(markdown_to_html("Este é um *exemplo*."))
print(markdown_to_html("[Google](https://google.com)"))
print(markdown_to_html("![coelho](imagem.jpg)"))

print(markdown_to_html(
    "1. Primeiro item\n2. Segundo item\n3. Terceiro item"
))
