#testing note.py
import note

#create a note

data1 = "This is my note1"
data2 = "this is my note2"

note1 = note.Note()

note1.set_title("Note 1")
note1.set_category("Testing")

print "Note 1 data: "
print "Title: ", note1.get_title()
print "Category: ", note1.get_category()

note2 = note.Note()

note2.set_title("Note 2")
note2.set_category("Testing")

note1.write_data("notes",data1)

print "Note1's start: ", note1.get_start()
print "Note1's end: ", note1.get_end()

note2.write_data("notes",data2)
print "Note2's start: ", note2.get_start()
print "Note2's end: ", note2.get_end()

