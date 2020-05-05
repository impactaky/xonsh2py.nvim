# -*- coding: utf-8 -*-
import neovim
# from xonsh2py import xonsh2py

@neovim.plugin
class Xonsh2Py(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('xonsh2py', sync=False)
    def convert(self, args):
        print('hello')
        # self.nvim.current.line = xonsh2py(self.nvim.current.line)
