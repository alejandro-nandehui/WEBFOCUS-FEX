#===========================================
#Autor: Alejandro Nandehui Romero Palma
#Email: (paginacion_webmaster_@hotmail.com)
#skype: alejandro.nande1
#===========================================


import sublime
import sublime_plugin, os

import subprocess
import webbrowser

#==========================================================================
#Abrir fex
#Ejemplo: http://localhost:8080/ibi_apps/WFServlet?IBIF_ex=myfex.fex


servidor = 'localhost'
puerto = '8080'
#==========================================================================


#==========================================================================
#Abrir Pagina HTML
#Ejemplo: http://localhost:8080/approot/ibisamp/myhtml.html

proyectohtml = 'ibisamp'
puertohtml = '8080'
#==========================================================================





























class WebFocusBuscSeleccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selecc in self.view.sel():
            if selecc.empty():
                palabra = self.view.word(selecc)

            palabra = self.view.substr(selecc)
            Buscar(palabra)

class WebFocusBuscInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Buscar en el Foro:', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        Buscar(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

def Buscar(palabra):
    url = 'http://forums.informationbuilders.com/eve/forums?a=search&reqWords=' + palabra.replace(' ','+')
    webbrowser.open_new_tab(url)


    
class WebFocusExeFexCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            filename = os.path.split(self.view.file_name())[1]
            ie = webbrowser.get(webbrowser.iexplore)
            ie.open('http://'+servidor+':'+puerto+'/ibi_apps/WFServlet?IBIF_ex='+filename)


class WebFocusExeHtmlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            filenamehtml = os.path.split(self.view.file_name())[1]
            ie = webbrowser.get(webbrowser.iexplore)
            ie.open('http://'+servidorhtml+':'+puertohtml+'/approot/'+proyectohtml+'/'+filenamehtml)
