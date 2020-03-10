#!/usr/bin/env python
# coding: utf-8

# # Chatbot
# ## import libraries

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 


# ## Define Bot

# In[2]:


bot=ChatBot("Jinosh_Mon")
bot.set_trainer(ChatterBotCorpusTrainer)


# ## Training Bot

# In[3]:


bot.train("chatterbot.corpus.english")


# In[4]:


while(1):
    msg=input("You: ")
    if(msg=="Bye" or msg=="bye"):
            print("{}: {}".format(bot.name,"Kk see u"))
            break
    if(msg!="Bye" or msg!="bye"):
            reply=bot.get_response(msg)
            print("{}: {}".format(bot.name,reply))


# In[ ]:


bot.train("chatterbot.corpus.english")


# In[ ]:




