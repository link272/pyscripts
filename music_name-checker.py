import os
import subprocess
for root, dirs, files in os.walk("./music", topdown=True):
    lastname = root
    newname = root.split('-')
    newname = newname[0]
     if ' ' in newname:
         newname.replace(' ', '_')
     if newname[0] == '_':
         newname = newname[1:]
     if '(' in newname:
         newname.replace('(', '[')
     if ')' in newname:
         newname.replace(')', ']')
     if lastname != newname:
         print('mv ' + lastname + ' '+ newname)
         subprocess.check_call(['mv', lastname, newname])

class MusicFileName(object):

    unwanted = ["'", 
                "JustSomeMotion (JSM) - ",
                "00-",
                "01-",
                "02-",
                "03-",
                "04-",
                "05-",
                "06-",
                "07-",
                "08-",
                "09-",
                "10-",
                "11-",
                "12-",
                "13-",
                "14-",
                "15-",
                "16-",
                "17-",
                "18-",
                "19-",
                "20-",
                "21-",
                "22-",
                "►",
                "◄"
                ] + [str(i) for i in range(100, 3000)]
    unwanted2 = [["[","]"],["(",")"]]

    def __init__(self, root, filename):
        self.root = root + '/'
        self.old_filename = filename
        self.filename = filename[:-4]
        self.extension = filename[-4:]
        self.clean()
        #self.simulate()
        self.rename()

    def rename(self):
        if self.old_filename != self.filename+self.extension:
            subprocess.check_call(['mv',
                                self.root+self.old_filename,
                                self.root+self.filename+self.extension])


    def simulate(self):
        print("mv " + self.root + self.old_filename + " " + self.root + self.filename + self.extension)

    def __str__(self):
        return self.filename

    def clean(self):
        for x in self.unwanted:
            if x in self.filename:
                self.filename = self.filename.replace(x, '')
        if "--" in self.filename:
                self.filename = self.filename.replace('--', '-')
        if "  " in self.filename:
                self.filename = self.filename.replace('  ', ' ')

        for x in self.unwanted2:
            while x[0] in self.filename:
                    a = self.filename.find(x[0])
                    b = self.filename.find(x[1])
                    tmp = self.filename[a:b+1]
                    self.filename = self.filename.replace(tmp, "")

        self.filename = self.filename.replace("'", '@')
        self.filename = self.filename.replace('"', '@')
        self.filename = self.filename.lower()
        tmp = self.filename.split('-')
        if len(tmp) > 1:
            artist = tmp[0].lower()
            name = tmp[1].lower()
        else:
            name = tmp[0]
            artist = self.root.split('/')
            artist = artist[-1]

        for x in self.unwanted:
            if x in artist:
                artist = artist.replace(x, "")                 
            if x in name:
                name = name.replace(x, "")

        for x in self.unwanted2:
            if x[0] in artist:
                try:
                    a = artist.find(x[0])
                    b = artist.find(x[1])
                    tmp = artist[a:b]
                    artist = artist.replace(tmp, "")
                except:
                    pass
        for x in self.unwanted2:
            if x[0] in name:
                try:
                    a = name.find(x[0])
                    b = name.find(x[1])
                    tmp = name[a:b+1]
                    name = name.replace(tmp, "")
                except:
                    pass
        try:
            if artist[0] == ' ':
                artist = artist[1:]
            if name[0] == ' ':
                name = name[1:]
        except:
            pass
        try:
            if artist[-1] == ' ':
                artist = artist[:-1]
            if name[-1] == ' ':
                name = name[:-1]
        except:
            pass

        if len(artist) > 1:
            artist = artist[0].upper() + artist[1:]
        if len(name) > 1:    
            name = name[0].upper() + name[1:]
        if len(artist) >= 0:
            self.filename = artist + " - "+ name
        else:
            self.filename = name
        self.filename = self.filename.replace('@', "'")
        if "  " in self.filename:
                self.filename = self.filename.replace('  ', ' ')
        if "  " in self.filename:
                self.filename = self.filename.replace('  ', ' ')
        if self.filename[0] in [str(i) for i in range(10)]:
                self.filename = self.filename[1:]
        self.filename = self.filename.replace("_", " ")
        tmp1 = self.filename
        tmp2 = []
        if " - " in self.filename[:4]:
            self.filename = self.filename[3:]
        tmp = self.filename.split(" ")

        for i in tmp:
            try:
                i = i[0].upper() + i[1:]
                tmp2.append(i)
            except:
                if i == '-':
                    tmp2.append(i)
        self.filename = " ".join(tmp2)
        self.filename = self.filename.replace("Feat.", "ft.")
        self.filename = self.filename.replace("Feat", "ft.")
        self.filename = self.filename.replace("Ft.", "ft.")
        self.filename = self.filename.replace("Ft", "ft.")
        if self.filename[-1] == " ":
            self.filename = self.filename[:-1]





for root, dirs, files in os.walk("./action", topdown=True):
    for f in files:
        MusicFileName(root, f)


