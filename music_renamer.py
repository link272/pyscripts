#-*- coding: utf-8 -*-
import os
import subprocess
import sys

class Cleaner():

    unwanted_string = [
                        " soundtrack",
                        " lyrics",
                        " lyric",
                        " trailer",
                        " hd",
                        " cover"
                            ]
    def check_bloc(self, string, index):
        tmp = BaseFileName.Bloc(string)
        with open("./music_renamer_data/badbloc", "r") as f:
            for i in f.readlines():
                if i in string:
                    tmp.is_badbloc = True
        for i in range(10):
            if "0" + str(i) in string[:2]:
                tmp.is_badbloc = True
                
        if index == 0:
            tmp.is_artist = True
        else:
            tmp.is_song = True
        
        return tmp
            
        

    def lower(self, string):
        return string.lower()

    def change_apostrophy(self, string):
        if "'" in string:
            string = string.replace("'", "§")
        return string
    
    def change_comma(self, string):
        if "," in string:
            string = string.replace(",", "-")
        return string

    def reverse_apostrophy(self, string):
        if "§" in string:
            string = string.replace("§", "'")
        return string

    def remove_multiple(self, string):
        for i in [" ", "-", "_"]:
            change = True
            while change == True:
                if i+i in string:
                    change = True
                    string = string.replace(i+i, i)
                else:
                    change = False
        return string

    def remove_unwanted_char(self, string = ""):
        for i in "#◄►^@%~":
            if i in string:
                string = string.replace(i, "")
        return string

    def remove_bracet(self, string = ""):
        for i in [["[", "]"],["(",")"],["{","}"]]:
            if i[0] in string:
                a = string.find(i[0])
                b = string.find(i[1])
                string = string.replace(string[a:b+1], "")
        return string

    def format_string(self, string):
        tmp =  []
        for i in string.split(" "):
            i = self.check_space(i)
            i = i.lower()
            i = i[0].upper() + i[1:]
            tmp.append(i)
        string = " ".join(tmp)
        print(string)
        return string

    def check_space(self, string):
        if string[0] == " ":
            string = string[1:]
        if string[-1] == " ":
            string = string[:-1]
        return string

    def remove_unwanted_string(self, string):
        for j in self.unwanted_string:
            if j in string:
                string = string.replace(j, "")
        return string


class BaseFileName(object):
    
    feat_list_pattern = ["feat.", "ft.", "feat", "ft"]
    feat_pattern = ""
    remix_list_pattern = ["rmx", "remix"]
    root = ""
    old_name = ""
    name = ""
    is_remix = False
    has_feat = False
    cmd = []
    blocs_list = []


    def build(self):
        self.pre()
        self.post()

    def pre(self):
        self.cleaner = Cleaner()
        self.name = self.cleaner.change_apostrophy(self.name)
        self.name = self.cleaner.change_comma(self.name)
        self.name = self.cleaner.remove_unwanted_char(self.name)
        self.name = self.cleaner.lower(self.name)
        self.name = self.name.replace("_", " ")
        for i in self.remix_list_pattern:
            if i in self.name:
                self.is_remix = True
                self.name = self.name.replace(i, "")
        for i in self.feat_list_pattern:
            if i in self.name:
                self.has_feat = True
                self.feat_pattern = i
        self.name = self.cleaner.remove_bracet(self.name)
        self.name = self.cleaner.remove_multiple(self.name)
        self.name = self.cleaner.remove_unwanted_string(self.name)
        self.generate_blocs()
        self.reverse_filename()

    def post(self):
        self.name = self.cleaner.reverse_apostrophy(self.name)

    def generate_blocs(self):
        tmp = self.name.split("-")
        j = 0
        if self.has_feat == True:
            for i in tmp:
                if self.feat_pattern in i:
                    i = i.split(self.feat_pattern)
                    self.blocs_list.append(self.Bloc(i[0]), artist = True)
                    j+=1
                    self.blocs_list.append(self.Bloc(i[1], feat = True))
                    j+=1
                else:
                    a = self.cleaner.check_bloc(i)
                    if a.is_badbloc == False:
                        self.blocs_list.append(a)
                        j+=1
                    else:
                        with open("renamer.log", "w") as f:
                            f.write("\t"+ i +"\n")
                        
        else:
            for i in tmp:
                    a = self.cleaner.check_bloc(i, j)
                    if a.is_badbloc == False:
                        self.blocs_list.append(a)
                        j+=1
                    else:
                        with open("renamer.log", "w") as f:
                            f.write("\t"+ i +"\n")
                

    def reverse_filename(self):
        artist, song= "",""
        for bloc in self.blocs_list:
            #print(["Bloc", bloc, bloc.is_artist, bloc.is_song, bloc.is_badbloc])
            if bloc.is_artist == True:
                artist += bloc.reverse()
            if bloc.is_song == True:
                if song != "":
                    song += " " + bloc.reverse()
                else:
                    song += bloc.reverse()
        if self.has_feat == True:
            for bloc in self.blocs_list:
                if bloc.is_feat == True:
                    artist += "ft. "+ bloc.reverse()
        if self.is_remix == True:
            song += " [Remix]"
        self.name = []
        if artist != "":
            self.name.append(artist)
        else:
            if isinstance(self, MusicFileName):
                self.name.append("Unknown")
        if song != "":
            self.name.append(song)
        self.name = " - ".join(self.name)


    class Bloc(object):

        bloc = None
        is_artist = False
        is_badbloc = False
        is_song = False
        is_feat = False


        def __init__(self, string,feat = False, artist = False, song = False, badbloc = False):
            self.is_song = song
            self.is_artist = artist
            self.cleaner = Cleaner()
            self.is_feat = feat
            self.bloc = string
            self.bloc = self.cleaner.remove_multiple(self.bloc)
            self.bloc = self.cleaner.check_space(self.bloc)


        def __repr__(self):
            return self.reverse()
                


        def reverse(self):
            self.bloc = self.bloc.split(" ")
            tmp = []
            for i in self.bloc:
                i = self.cleaner.remove_multiple(i)
                i = self.cleaner.check_space(i)
                i = self.cleaner.format_string(i)
                tmp.append(i)
            return " ".join(tmp)


class MusicFileName(BaseFileName):

    ext = ""

    def __init__(self, path, name):
        self.blocs_list = []
        self.old_name = name
        self.ext = name[-4:]
        self.name = name[:-4]
        self.path = path +"/"
        self.build()

    def __str__(self):
        return self.path+self.old_name + "\t" + self.path+self.name+self.ext

    def cmd(self):
        return ['mv', self.path+self.old_name, self.path+self.name+self.ext]

class MusicDirectoryName(BaseFileName):


    def __init__(self, name):
        self.blocs_list = []
        self.old_name = name
        self.name = name
        self.build()

    def __str__(self):
        return self.old_name + "\t" + self.name

    def cmd(self):
        return ['mv', self.old_path, self.name]

class Manager(object):

    path = ""
    directories = []
    files = []

    def __init__(self, path = "./music", simulate = False, confirm = False):
        self.path = path
        self.scan()
        if simulate == True:
            self.simulate()
        if confirm == True:
            self.rename()

    
    def scan(self):
        print("scanning...")
        for root, dirs, files in os.walk(self.path, topdown=True):
            self.directories.append((MusicDirectoryName(root)))
            for name in files:
                self.files.append(MusicFileName(root, name))


    def simulate(self):
        for directory in self.directories:
            print(directory)
        for filename in self.files:
            print(filename)

    def rename(self):
        with open("renamer.log", "w") as f:
            for filename in self.files:
                cmd = filename.cmd()
                f.write("\t".join(cmd)+"\n")
                subprocess.check_call(cmd)
            for directory in self.directories:
                cmd = directory.cmd()
                f.write("\t".join(cmd)+"\n")
                subprocess.check_call(cmd)


Manager("./music", simulate = True, confirm = False)
