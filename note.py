'''
Class: Note
Description: This contains all the information about the note
The note has the following attributes:
- title: the note's title
- category: what category the note is under
- source: where the note came from
- tags: search keywords
- root: root directory set by the main module
- store: file where the note contents are stored
'''

import os
import hashlib as h
from datetime import datetime as d

class Note:
  def __init__(self,title,root):
    self._set_title("title")
    self.root = root
    self._set_category("")
    self._set_source("")
    self.tags = set()
    self.store = h.sha1(title+
                        d.now().strftime('%Y%m%d%H%M%S')).hexdigest()
    
  def set_title(self,title):
    self.title = title

  def set_category(self,category):
    self.category = category

  def set_source(self,source):
    self.source = source

  def get_title(self):
    return self.title

  def get_category(self):
    return self.category

  def get_source(self):
    return self.source

  def get_store(self):
    return self.store 

  _set_title = set_title
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

  def write_data(self,note):
    path = os.path.join(self.root,self.store)
    data = open(path,'w')
    data.write(note)
    data.close

  def read_data(self):
    path = os.path.join(self.root,self.store)
    data = open(path,'r')
    content = data.read()
    return content

