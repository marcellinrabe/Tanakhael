class Search:

    def __init__(self, chat) -> None:
        self.chat = chat

    def template(self, sender_id):
        """
            video example of search input format
        """
        self.chat.send_message(sender_id, "afaka manadina ianao")
        pass