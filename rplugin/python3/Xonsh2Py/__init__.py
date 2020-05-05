# -*- coding: utf-8 -*-
import neovim
from Xonsh2Py import xonsh2py

@neovim.plugin
class Xonsh2Py(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('Xonsh2Py')
    def convert(self, args):
        self.nvim.current.line = xonsh2py.convert(self.nvim.current.line)
