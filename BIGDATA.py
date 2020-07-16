# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 01:03:37 2020

@author: GONZALO
"""

#%%
import kivy
kivy.require("1.9.2")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder


class Migrilla(Widget):
    pass
            
        
        
        
        
Builder.load_file('my.kv')
        
class MyApp(App):
    def build(self):
        return Migrilla()




if __name__=="__main__":
    MyApp().run()






