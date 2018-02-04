''' Simple Class Desktop
    We're going to use the PyQt5 module, not present in the 
    standard library but we have to download it from command 
    $ pip3 install pyqt (for Linux users).
    This application consist in a simple and white desktop 
    with two buttons:
    - Text Editor 
    - Web Browser
'''

#Start importing the necessary module from the pyqt library
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#Define the functions to build and run the window
def BuildWindow():
    '''Create a window'''
    #control if the application yet exsist
    app = QApplication.instance()
    #if not exsist, I create it 
    if not app: app = QApplication([])
    #I create a window but it isn't visible
    window = QWidget()
    #I resize the window and I put any title I want
    window.resize(500, 300)
    window.setWindowTitle('')
    return app, window

def runApp(app, window):
    '''Run the application'''
    #show the window
    window.show()
    #Launch the app
    app.exec_()
    
#Create a class to define and object QWBrowser
class QWBrowser:
    
    def __init__(self, window, app):
        app, window = BuildWindow()
        self.app = app
        self.window = window
    
    #define the method to build the Browser interface
    def _build_browser(self):
        #Set the window title
        self.window.setWindowTitle('Web Browser')
        self.window.resize(700, 400)
        #Create a toolbar layout for the command to go back
        #to go forward and to search an url
        toolbar_layout = QHBoxLayout()
        #Create the Browser layout to view the page
        #and the toolbar
        browser_layout = QVBoxLayout()
        #Create the back, forward buttons
        button_back = QPushButton('<')
        button_forward = QPushButton('>')
        #create a navigation bar to navigate into the urls
        navigation_bar = QLineEdit('')
        widgetlist = [button_back, button_forward, navigation_bar]
        #Add the widget to the toolbar layout
        for x in widgetlist: toolbar_layout.addWidget(x)
        #Add the toolbar layout to the browser_layot
        browser_layout.addLayout(toolbar_layout)
        #Create the space to which view the pages
        web_view = QWebEngineView()
        browser_layout.addWidget(web_view)
        #Set the layout to the window
        self.window.setLayout(browser_layout)
        #Now I have to define the callBack for the widget
        def LoadPage():
            #Now i control if the url in the navigation_bar is egual to
            #the url of the current page
            if navigation_bar.text() == web_view.url().toString():
                return 
            text = navigation_bar.text()
            #Now I format the navigation bar to search correctly an url
            if ' ' in text or '.' not in text:
                text = ('http://google.com/search?q='+
                        '+'.join(text.split()))
            elif '://' not in text:
                text = 'http://'+text
            web_view.setUrl(QUrl(text))
        
        def SetUrl():
            #Set the url to the navigation bar
            navigation_bar.setText(web_view.url().toString())
        
        #Now I setting up the callback to the respective widget
        navigation_bar.returnPressed.connect(LoadPage)
        web_view.urlChanged.connect(SetUrl)
        button_back.clicked.connect(web_view.back)
        button_forward.clicked.connect(web_view.forward)
        
        
