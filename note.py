import os
import hashlib as h
from datetime import datetime as d


class Note:

    """
    Class: Note
    Description: This contains all the information about the note

    Attributes:
    - title: the note's title
    - category: what category the note is under
    - source: where the note came from
    - tags: search keywords
    - dir: the directory where the note is filed
    - file: file where the note contents are filed
    """

    def __init__(self, title, dir):
        self._set_title("title")
        self.dir = dir
        self._set_category("")
        self._set_source("")
        self.tags = set()
        # the file name is the title plus the hex digest
        self.file = h.sha1(title +
                           d.now().
                           strftime('%Y%m%d%H%M%S')).hexdigest()

    def set_title(self, title):
        self.title = title

    def set_category(self, category):
        self.category = category

    def set_source(self, source):
        self.source = source

    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_source(self):
        return self.source

    def get_file(self):
        return self.file

    _set_title = set_title
    _set_category = set_category
    _set_source = set_source

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        success = false
        if tag in self.tags:
            self.tags.remove(tag)
            success = true
        return success

    def replace_tag(self, old_tag, new_tag):
        success = false
        if old_tag in self.tags and new_tag not in self.tags:
            index = self.tags.index(old_tag)
            self.tags.insert(index, new_tag)
            success = true
        return success

    def write_data(self, content):
        path = os.path.join(self.dir, self.file)
        data = open(path, 'w')
        data.write(content)
        data.close

    def read_data(self):
        path = os.path.join(self.dir, self.file)
        data = open(path, 'r')
        content = data.read()
        return content
