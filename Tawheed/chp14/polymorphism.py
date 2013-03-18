class HighSchool:
    def homeroom(self):
        print "hommy"
    def classroom(self):
        print "This is the high school calssrom"

class College(HighSchool):
    def library(self):
        print "library forever"
    def classroom(self):
        print "Thi is the college class room"



high = HighSchool()
high.classroom()

coll = College()
coll.classroom()
coll.homeroom()






























