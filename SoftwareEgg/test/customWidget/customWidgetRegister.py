# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:48:01 2020

@author: 1msc20
"""

from pygubu import BuilderObject, register_widget
from passwordWidget import PasswordWidget


class PasswordWidgetBuilder(BuilderObject):
    class_ = PasswordWidget


register_widget('customWidgetRegister.passwordwidget', PasswordWidgetBuilder,
                'PasswordWidget', ('ttk', 'customapp'))