import ampalibe

from controllers.base import Controller

from services.verseapi import VerseAPI
VERSE_API = VerseAPI()
controller = Controller(VERSE_API)


@ampalibe.command('/')
def choice_testament(sender_id, cmd, suggestion=None, **ext):
    greetings = ["tanakhael", "salama", "hello", "bonjour", "azafady"]

    if suggestion is not None:
        if "aoka izao" in suggestion:
            controller.end_session(sender_id)
        elif "eny" in suggestion:
            controller.choice_testament(sender_id)
        return None
    
    for greeting in greetings:
        if greeting in str(cmd).lower():
            controller.choice_testament(sender_id)
            return None

    controller.propose_greeting_keys(sender_id, greetings)


@ampalibe.command('/choice-book')
def choice_book(sender_id, cmd, testament, **ext):
    controller.choice_book(sender_id, testament)


@ampalibe.command('/choice-chapter')
def choice_chapter(sender_id, cmd, book, **ext):
    controller.choice_chapter(sender_id, book)


@ampalibe.command("/output-type")
def choice_verse_getter(sender_id, cmd, book, chapter, **ext):
    controller.choice_output(sender_id, book, chapter)


@ampalibe.command("/verse-number")
def get_verse(sender_id, cmd, option, last_index, **ext):
    controller.get_verse_number(sender_id, option, last_index)


@ampalibe.action("/verse-text")
def build_request(sender_id, cmd, **ext):
    controller.show_verse(sender_id, cmd)

