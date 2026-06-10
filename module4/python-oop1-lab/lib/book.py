class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Use the setter to trigger validation on initialization
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            # Setting it to None or zero prevents an unassigned attribute error
            self._page_count = None 

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")