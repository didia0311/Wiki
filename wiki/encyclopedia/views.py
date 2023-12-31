from django.shortcuts import render
from markdown2 import Markdown
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None 
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request,"encyclopedia/error.html", {
            "message: This entry does not exist"
        })
    else:
        return render (request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    