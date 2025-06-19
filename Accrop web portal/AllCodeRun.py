from UserAUGD import  user_create, user_update, user_disable, user_enable, get_user
from Framework import framework_add, framework_update, framework_search

Uid = user_create(4,"Raj23@mathur.com","Raj","Kumar","Mathur","+91","IN",600000)
user_update(2,"raj23@mathur.com","Raja Ji",Uid,"NewMathur004","Important","+91","IN","20001010")
user_disable(Uid, "Disabled by code.")
user_enable(Uid, "Enabled by code.")
get_user("raj23@mathur.com")


id = framework_add("ByCodeFrame001", "Description001 By Code", "By Code001","www.accorpwebportal.web.app")
framework_update("684bf3b5af606a2b0ec68eba","ByCodeFrame003", "Description003 By Code", "By Code003","www.flipkart.com")
framework_search("bycode")