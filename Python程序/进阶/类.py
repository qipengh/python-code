import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   


####################################################
#                5. Classes                        #
#                5. Àà                             #
####################################################

class Human(object):

    # ÀàÊôÐÔ£¬½«±»Õâ¸öÀàµÄËùÓÐÊµÀýËù¹²Ïí
    species = "H. sapiens"+0

    #»ù±¾µÄ³õÊ¼»¯º¯Êý£¨¹¹ÔìÆ÷£©
    def __init__(self, nm):
        # ²ÎÊý¸³ÖµÎªÊµÀýµÄnameÊôÐÔ
        self.name = nm

    #ÏÂÃæÊÇÊµÀý·½·¨£¬ËùÓÐ·½·¨¶¼ÒÔ self ÎªµÚÒ»¸ö²ÎÊý
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # Àà·½·¨»á±»ËùÓÐÊµÀý¹²Ïí¡£
    # Àà·½·¨ÔÚµ÷ÓÃÊ±£¬»á½«Àà±¾Éí×÷ÎªµÚÒ»¸ö²ÎÊý´«Èë¡£
    @classmethod
    def get_species(cls):
        return cls.species

    # ¾²Ì¬·½·¨ÔÚµ÷ÓÃÊ±£¬²»»á´«ÈëÀÛ»òÊµÀýµÄÒýÓÃ¡£
    @staticmethod
    def grunt():
        return "*grunt*"

# ÊµÀý»¯Ò»¸öÀà
i= Human(name="Ian")
print (i.say("hi") )      # ´òÓ¡³ö "Ian: hi"

j = Human("joel")
print (j.say("hello"))

# µ÷ÓÃÎÒÃÇµÄÀà·½·¨
i.get_species()

# ÐÞ¸Ä¹²ÏíÊôÐÔ
Human.species = "H. neanderthalensis"
i.get_species()         # =>"H.neanderthalensis"
j.get_species()

# µ÷ÓÃ¾²Ì¬·½·¨
Human.grunt()       # =>"*grunt*"


# ÀýÒ» ´´½¨°üº¬Á½¸ö Person ÀàµÄÊµÀýµÄ list£¬²¢¸øÁ½¸öÊµÀýµÄ name ¸³Öµ£¬È»ºó°´ÕÕ name ½øÐÐÅÅÐò¡£


class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2:cmp(p1.name, p2.name)) # ÅÅÐòº¯Êý

print (L2[0].name)
print (L2[1].name)
print (L2[2].name)


# Àý¶þ ¶¨ÒåPersonÀàµÄ__init__·½·¨£¬³ýÁË½ÓÊÜ name¡¢gender ºÍ birth Íâ£¬
# »¹¿É½ÓÊÜÈÎÒâ¹Ø¼ü×Ö²ÎÊý£¬²¢°ÑËûÃÇ¶¼×÷ÎªÊôÐÔ¸³Öµ¸øÊµÀý¡£ 

class Person(object):
    def __init__(self, name, gender, birth, **kw): # ¶¨Òå¹Ø¼ü×Ö²ÎÊý£¬Ê¹ÓÃ **kw
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems(): #¿ÉÍ¨¹ý setattr(self, 'name', 'xxx') ÉèÖÃÊôÐÔ
            setattr(self, k, v)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job = 'Student')

print (xiaoming.name)
print (xiaoming.job)


# PythonÖÐ·ÃÎÊÏÞÖÆ
'python ¶ÔÊôÐÔÈ¨ÏÞµÄ¿ØÖÆÊÒÍ¨¹ýÊôÐÔÃûÀ´ÊµÏÖµÄ£¬ÈôÒ»¸öÊôÐÔÓÉË«ÏÂ»®Ïß¿ªÍ·£¨__£©,¸ÃÊôÐÔ¾ÍÎÞ·¨±»Íâ²¿·ÃÎÊ¡£'

class Person(object):
    def __init__(self, name): 
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'

p = Person('Bob')
print (p.name)
print (p._title)
print (p.__job)  # ÎÞ·¨Ö±½Ó±»Íâ²¿·ÃÎÊ


