'''
Class: Note
Description: This will reference where in the file the note is stored
The note has the following attributes:
- start: where it starts in storage
- end: where it ends in storage
- title: the note's title
- category: what category the note is under
- source: where the note came from
- tags: search keywords
'''

import os

class Note:
  def __init__(self):
    self._set_title("")
    self._set_start(0)
    self._set_end(0)
    self._set_category("")
    self._set_source("")
    self.tags = set()
    
  def set_title(self,title):
    self.title = title

  def set_start(self,start):
    self.start = start

  def set_end(self,end):
    self.end = end

  def set_category(self,category):
    self.category = category

  def set_source(self,source):
    self.source = source

  def get_title(self):
    return self.title

  def get_start(self):
    return self.start

  def get_end(self):
    return self.end

  def get_category(self):
    return self.category

  def get_source(self):
    return self.source 

  _set_title = set_title
  _set_start = set_start
  _set_end = set_end
  _set_category = set_category
  _set_source = set_source 

  def add_tag(self,tag):
    self.tags.append(tag)

  def remove_tag(self,tag):
    success = false
    if tag in self.tags:
      self.tags.remove(tag)
      success = true
    return success

  def edit_tag(self,old_tag,new_tag):
    success = false
    if old_tag in self.tags and new_tag not in self.tags:
      index = self.tags.index(old_tag)
      self.tags.insert(index,new_tag)
      success = true
    return success

  def write_data(self,filename,note):
    data = open(filename,'a')
    self._set_start(data.tell())
    data.write(note)
    self._set_end(data.tell())
    data.close

