import wx
import wx.animate
import gui
import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('excel_finals.xlsx')
worksheet = workbook.add_worksheet()
#Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

class MainApp(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

        self.panelzero=Panel0(self)
        self.panelOne = Panel1(self)
        self.panelTwo = Panel2(self)
        self.panelThree=Panel3(self)
        self.panelFour=Panel4(self)
        self.panelFive=Panel5(self)
        self.panelSix=Panel6(self)
        self.panelOne.Hide()
        self.panelTwo.Hide()
        self.panelThree.Hide()
        self.panelFour.Hide()
        self.panelFive.Hide()
        self.panelSix.Hide()


class Panel0(gui.panel_zero):
    def __init__(self, parent):
        gui.panel_zero.__init__(self, parent)
        self.parent = parent
    #change intro pannel will change the content and store the button value
    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel one Showing")
            self.Hide()
            self.parent.panelOne.Show()
            #buttonResult = self.

class Panel1(gui.panel_one):
    def __init__(self, parent):
        gui.panel_one.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel Two Showing")
            self.Hide()
            self.parent.panelTwo.Show()
            buttonResult1 = self.m_radioBox5.GetStringSelection()
            print(buttonResult1)
            #Write some numbers, with row/column notation.
            worksheet.write(0,0,buttonResult1)

class Panel2(gui.panel_two):
    def __init__(self, parent):
        gui.panel_two.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel three Showing")
            self.Hide()
            self.parent.panelThree.Show()
            buttonResult2 = self.m_radioBox4.GetStringSelection()
            print(buttonResult2)
            worksheet.write_string(1,0, buttonResult2)
            

class Panel3(gui.panel_three):
    def __init__(self, parent):
        gui.panel_three.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel four Showing")
            self.Hide()
            self.parent.panelFour.Show()
            buttonResult3 = self.m_radioBox2.GetStringSelection()
            print(buttonResult3)
            worksheet.write(2,0, buttonResult3)

class Panel4(gui.panel_four):
    def __init__(self, parent):
        gui.panel_four.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel five Showing")
            self.Hide()
            self.parent.panelFive.Show()
            buttonResult4 = self.m_radioBox3.GetStringSelection()
            print(buttonResult4)
            worksheet.write(3,0, buttonResult4)

class Panel5(gui.panel_five):
    def __init__(self, parent):
        gui.panel_five.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Panel six showing")
            self.Hide()
            self.parent.panelSix.Show()
            buttonResult5 = self.m_radioBox6.GetStringSelection()
            print(buttonResult5)
            worksheet.write(4,0,buttonResult5)
            

class Panel6(gui.panel_six):
    def __init__(self, parent):
        gui.panel_six.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self,event):
        if self.IsShown():
            self.parent.SetTitle("panel zero showing")
            #self.Hide()
            self.parent.panelzero.Show()
            self.Hide()
            


def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
