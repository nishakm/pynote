#testing note.py
import note

#create a note

root = ".notes"

data1 = "This is my note1"
data2 = "this is my note2"

note1 = note.Note("Note 1", root)
note1.set_category("Testing")

print "Note 1 data: "
print "Title: ", note1.get_title()
print "Category: ", note1.get_category()

note2 = note.Note("Note 2",root)
note2.set_category("Testing")

print "Writing data"
note1.write_data(data1)
note2.write_data(data2)
print "Reading data"
print note1.read_data()
print note2.read_data()

