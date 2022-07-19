import ampalibe
from conf import Configuration
from view.app import View
from model.app import Fetch
from model.Upload import Upload

Views = View()
Fetchs = Fetch(Configuration())

@ampalibe.command("/")
def start(sender_id, cmd, **extends):
    Views.option.start(sender_id)

@ampalibe.command("/wantsearch")
def wantsearch(sender_id, cmd, **extends):
    Views.getinput(sender_id)

@ampalibe.command("/wantbrowse")
def wantbrowse(sender_id, cmd, **extends):
    Views.option.browse(sender_id)

@ampalibe.command("/testmtlist")
def testmtist(sender_id, cmd, type, **extends):
    testmt = Fetchs.livres(type)
    Views.chapters(sender_id, testmt)

@ampalibe.action("/wantupload")
def returnverse(sender_id, cmd, **extends):
    subtitle = cmd.replace(' ','')
    versetext = Fetchs.verse(subtitle) 
    Views.uploadoption(sender_id, subtitle, versetext)

@ampalibe.command("/render")
def render(sender_id, cmd, subtitle, type, verse, **extends):
    if type == "message" : content = verse
    elif type == "textfile": content = Upload.textfile(subtitle, verse)
    elif type == "pdf": content = Upload.pdf(subtitle, verse)
    elif type == "png": content = Upload.png(subtitle, verse)
    else: raise TypeError("output types are message, pdf, text file and png")
    Views.render(sender_id, content)


