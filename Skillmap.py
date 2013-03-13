import sys
import pprint
import string
#ff = open("final.tex",'w');

class Skill(object):
  def __init__(self, name):
    self.name=name
    self.list_of_subskills=[]

  def AddNewSkill(self, skill):
    self.list_of_subskills.append( skill )
  def __iter__(self):
    for each in self.list_of_subskills:
      yield self.__getattribute__(each)


class Skillmap:
  """Skillmap class"""
  def __init__(self):
  
    # list of skills
    self.skills_list = []

  def AddMainSkill(self, s):
    """Add new main skill"""
    
    self.skills_list.append(s)

  def AddSecondLevelSkillToMainSkill(self, main_skill, second_skill):
    idx = self.skills_list.index(main_skill)
    self.skills_list.insert( idx+1, [ second_skill ] )
    print idx

  def AddThirdLevelSkillToSecondSkill(self, second_skill, third_skill):
    pass
    
  def PrintSkills(self):
    for main_skill in self.skills_list:
      if main_skill is list:
        for sec in main_skill:
          print sec
      else:
        print main_skill

m = Skillmap()
m.PrintSkills()
