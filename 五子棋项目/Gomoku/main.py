#!/usr/bin/python
# -*- coding:cp936 -*-

import time
import wx
from Defines import *


class DragShape:
    def __init__(self, bmp):
        self.bmp = bmp
        self.pos = (0, 0)
        self.shown = True
        self.text = None
        self.fullscreen = False

    def HitTest(self, pt):
        rect = self.GetRect()
        return rect.InsideXY(pt.x, pt.y)

    def GetRect(self):
        return wx.Rect(self.pos[0], self.pos[1],
                       self.bmp.GetWidth(), self.bmp.GetHeight())

    def Draw(self, dc, op=wx.COPY):
        if self.bmp.Ok():
            memDC = wx.MemoryDC()
            memDC.SelectObject(self.bmp)

            dc.Blit(self.pos[0], self.pos[1],
                    self.bmp.GetWidth(), self.bmp.GetHeight(),
                    memDC, 0, 0, op, True)

            return True
        else:
            return False


class MainWindow(wx.Frame):
    def __init__(self, parent, id, title):
        self.dirname = ''
        wx.Frame.__init__(self, parent, -1, title, size=(600 + 5, 537 + 46),
                          style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)

        # self.SetSizeHints(600,537)
        self.CentreOnScreen()
        self.SetMaxSize([600 + 5, 537 + 46])
        # ����ͳ�ʼ��һЩȫ�ֵı���
        self.InitValues()
        # �����˵�
        self.BuildMenu()
        # ������ʱ��
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(200)
        self.Notify()

        # ��Ϣ��
        self.Bind(wx.EVT_MENU, self.OnNew, id=ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_HELP_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLButtonDown)

        self.Show(1)

    def BuildMenu(self):

        # ����һ��"��Ϸ"���в˵���������Ŀ
        FileMenu = wx.Menu()  # ����"��Ϸ"�˵���
        j = 0
        for Item in FileMenuNameList:
            i = FileMenuNameList.index(Item)
            if Item[0] == '':
                FileMenu.AppendSeparator()
                j -= 1
            else:
                FileMenu.Append(ID_NEW + i + j, Item[0], Item[1])

        # ����һ���ܰ������в˵��Ĳ˵���
        menuBar = wx.MenuBar()
        menuBar.Append(FileMenu, "��Ϸ")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # ����һ������"����"�˵���������Ŀ
        ToolMenu = wx.Menu()  # ����"����"�˵���
        j = 0
        for Item in ToolMenuNameList:
            i = ToolMenuNameList.index(Item)
            if Item[0] == '':
                ToolMenu.AppendSeparator()
                j -= 1
            else:
                ToolMenu.Append(ID_HELP_ABOUT + i + j, Item[0], Item[1])

        # ����һ���ܰ������в˵��Ĳ˵���
        menuBar.Append(ToolMenu, "����")  # ����һ��"����"�˵����˵���
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

    def InitValues(self):
        self.m_PpLastPos = (-1, -1)  # ����ߵ�ǰһ����
        self.m_PcLastPos = (-1, -1)  # ������ߵ�ǰһ����
        self.m_bWhoFirst = False  # ˭���ߣ�1Ϊ�������ߣ�0Ϊ�������
        self.m_bInit = False  # �ж���Ϸ�Ƿ��Ǵ��ڸտ�ʼ�׶�
        self.m_bPlayerWin = False  # �ж��Ƿ����Ӯ
        self.m_bComputerWin = False  # �ж��Ƿ�����Ӯ
        self.m_bCTable = []  # ����״̬��¼��ԭ��������һ����ά����[15][15][572]
        self.m_iWin = []  # ԭ��������һ����ά����[2][572]
        self.m_bPTable = []  # ԭ��������һ����ά����[15][15][572]
        self.m_bStart = True  # ��¼�Ƿ��ֵ����
        self.m_bPlayer = False  # ��¼�Ƿ��ֵ������
        self.m_bComputer = False
        self.m_iBoard = []
        self.m_BmpBoard = wx.Bitmap('res/board.bmp')
        self.m_Bmplastwhitechess = wx.Bitmap('res/lastwhite.bmp')
        self.m_Bmplastblackchess = wx.Bitmap('res/lastblack.bmp')
        self.m_Bmpblack = wx.Bitmap('res/black.bmp')
        self.m_Bmpwhitechess = wx.Bitmap('res/whitechess.bmp')
        self.m_Bmpblackchess = wx.Bitmap('res/blackchess.bmp')

        # �ж��ķ��ȿ�ʼ
        if self.m_bWhoFirst:
            self.m_bPlayer = False
            self.m_bComputer = True
        else:
            self.m_bPlayer = True
            self.m_bComputer = False

        # ��ʼ�����������ҵĻ�ʤ������
        self.m_bPTable = [[[False] * 572 for x in range(15)] for x in range(15)]
        self.m_bCTable = [[[False] * 572 for x in range(15)] for x in range(15)]
        self.m_iWin = [[0] * 572 for x in range(2)]
        self.m_iBoard = [[2] * 15 for x in range(15)]

        count = 0
        for i in range(15):
            for j in range(11):
                for k in range(5):
                    self.m_bPTable[j + k][i][count] = True
                    self.m_bCTable[j + k][i][count] = True
                    k += 1
                count += 1

        for i in range(15):
            for j in range(11):
                for k in range(5):
                    self.m_bPTable[i][j + k][count] = True
                    self.m_bCTable[i][j + k][count] = True
                    k += 1
                count += 1

        for i in range(11):
            for j in range(11):
                for k in range(5):
                    self.m_bPTable[j + k][i + k][count] = True
                    self.m_bCTable[j + k][i + k][count] = True
                    k += 1
                count += 1

        for i in range(11):
            j = 14
            while j >= 4:
                for k in range(5):
                    self.m_bPTable[j - k][i + k][count] = True
                    self.m_bCTable[j - k][i + k][count] = True
                    k += 1
                count += 1
                j -= 1

    def OnLButtonDown(self, event):
        if self.m_bPlayer and event.m_x <= 535 and event.m_y <= 535:  # �ж��Ƿ�����Ч����
            tx = x = event.m_x - 24
            ty = y = event.m_y - 25
            while tx >= 36:
                tx -= 36
            while ty >= 36:
                ty -= 36
            tx += x / 36
            ty += y / 36
            if tx > 18:
                x = x / 36 + 1
            else:
                x /= 36
            if ty > 18:
                y = y / 36 + 1
            else:
                y /= 36
            if self.m_iBoard[x][y] == 2:
                self.m_iBoard[x][y] = 0  # ��Ϊ��ҵ�����
                if self.m_PpLastPos[0] != -1 and self.m_PpLastPos[1] != -1:
                    if not self.m_bWhoFirst:
                        self.DrawWhiteChess(self.m_PpLastPos[0], self.m_PpLastPos[1])
                    else:
                        self.DrawBlackChess(self.m_PpLastPos[0], self.m_PpLastPos[1])
                if not self.m_bWhoFirst:
                    self.DrawNowWhite(x, y)
                else:
                    self.DrawNowBlack(x, y)
                self.m_PpLastPos = (x, y)
                i = 0
                while i < 572:  # �޸�������Ӻ�����״̬�ı仯
                    if i == 80:
                        i = 80
                    if self.m_bPTable[x][y][i] and self.m_iWin[0][i] != 7:
                        self.m_iWin[0][i] += 1
                    if self.m_bCTable[x][y][i]:
                        self.m_bCTable[x][y][i] = False
                        self.m_iWin[1][i] = 7
                    i += 1
                self.m_bPlayer = False
                self.m_bComputer = True

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.TileBackground(dc)
        for i in range(15):
            for j in range(15):
                if self.m_iBoard[i][j] == 0:  # ��ҵ�����
                    if self.m_PpLastPos[0] == i and self.m_PpLastPos[1] == j:
                        if not self.m_bWhoFirst:
                            self.DrawNowWhite(self.m_PpLastPos[0], self.m_PpLastPos[1])
                        else:
                            self.DrawNowBlack(self.m_PpLastPos[0], self.m_PpLastPos[1])
                        continue
                    if not self.m_bWhoFirst:
                        self.DrawWhiteChess(i, j)
                    else:
                        self.DrawBlackChess(i, j)

                if self.m_iBoard[i][j] == 1:  # �����������
                    if self.m_PcLastPos[0] == i and self.m_PcLastPos[1] == j:
                        if not self.m_bWhoFirst:
                            self.DrawNowBlack(self.m_PcLastPos[0], self.m_PcLastPos[1])
                        else:
                            self.DrawNowWhite(self.m_PcLastPos[0], self.m_PcLastPos[1])
                        continue

                    if not self.m_bWhoFirst:
                        self.DrawBlackChess(i, j);
                    else:
                        self.DrawWhiteChess(i, j);

    def TileBackground(self, dc):
        sz = self.GetClientSize()
        w = self.m_BmpBoard.GetWidth()
        h = self.m_BmpBoard.GetHeight()

        x = 0

        while x < sz.width:
            y = 0

            while y < sz.height:
                dc.DrawBitmap(self.m_BmpBoard, x, y)
                y = y + h

            x = x + w

    def IsWin(self):
        for i in range(572):
            if self.m_iWin[0][i] == 5:
                self.m_bPlayerWin = True
                print 'playerwin'
                break
            if self.m_iWin[1][i] == 5:
                self.m_bComputerWin = True
                print 'Computerwin'
                break

    def Notify(self):
        self.IsWin()
        if self.m_bPlayerWin:
            # time.Stop()
            d = wx.MessageDialog(self, "��ϲ����������!", "�����С���", wx.OK)
            if d.ShowModal() == wx.ID_OK:
                self.Close(True)
            d.Destroy()
            self.m_bPlayerWin = False
            self.m_bComputer = False
            self.m_bInit = True
        elif self.m_bComputerWin:
            # time.Stop()
            d = wx.MessageDialog(self, "������������!", "�����С���", wx.OK)
            if d.ShowModal() == wx.ID_OK:
                self.Close(True)
            d.Destroy()
            self.m_bPlayerWin = False
            self.m_bComputer = False
            self.m_bInit = True
        else:
            if self.m_bComputer:
                self.ComTurn()
    def SearchBlank(self, Nowboard, List = None):
        for x in range(15):
            for y in range(15):
                if Nowboard[x][y] == 2:
                    List[0] = x
                    List[1] = y
                    return 1
        return 0

    def ComTurn(self):
        temp1 = [-1] * 20
        temp2 = [-1] * 20
        tmpList = [0, 0]
        cscore = -10000
        ctempboard = [[0] * 15 for x in range(15)]
        ptempboard = [[0] * 15 for x in range(15)]
        if self.m_bStart:
            if self.m_iBoard[7][7] == 2:
                bestx = 7
                besty = 7
            else:
                bestx = 8
                besty = 8
            self.m_bStart = False
        else:  # Ѱ�����λ��
            for i in range(15):
                for j in range(15):
                    ctempboard[i][j] = self.m_iBoard[i][j]

            while self.SearchBlank(ctempboard, tmpList) == True:
                i = tmpList[0]
                j = tmpList[1]
                n = 0
                pscore = 10
                for k in range(15):
                    for l in range(15):
                        ptempboard[k][l] = self.m_iBoard[k][l]
                ctempboard[i][j] = 3  # ����ѱ�����
                ctemp = self.GiveScore(1, i, j)
                for m in range(572):  # ��ʱ���������Ϣ
                    if self.m_bPTable[i][j][m]:
                        temp1[n] = m
                        self.m_bPTable[i][j][m] = False
                        temp2[n] = self.m_iWin[0][m]
                        self.m_iWin[0][m] = 7
                        n += 1
                    # print ctempboard
                ptempboard[i][j] = 1
                pi = i
                pj = j
                while self.SearchBlank(ptempboard, tmpList) == True:
                    i = tmpList[0]
                    j = tmpList[1]
                    # print ('i=%d j=%d n=%d' % (i,j,n))
                    ptempboard[i][j] = 3  # ����ѱ�����
                    ptemp = self.GiveScore(0, i, j)
                    # print ptempboard
                    if pscore > ptemp:  # ��ʱΪ������ӣ����ü�С����ʱӦѡȡ��Сֵ
                        pscore = ptemp
                for m in range(n):  # �ָ������Ϣ
                    self.m_bPTable[pi][pj][temp1[m]] = True
                    self.m_iWin[0][temp1[m]] = temp2[m]
                if ctemp + pscore > cscore:  # ��ʱΪ��������ӣ����ü�С����ʱӦѡȡ�����ֵ
                    cscore = ctemp + pscore
                    # print ('%f,%f,%f' %(ctemp,pscore,cscore))
                    bestx = pi
                    besty = pj

        self.m_iBoard[bestx][besty] = 1
        if self.m_PcLastPos[0] != -1 and self.m_PcLastPos[1] != -1:  # ��ǰһ����
            if not self.m_bWhoFirst:
                self.DrawBlackChess(self.m_PcLastPos[0], self.m_PcLastPos[1])
            else:
                self.DrawWhiteChess(self.m_PcLastPos[0], self.m_PcLastPos[1])

        if not self.m_bWhoFirst:
            self.DrawNowBlack(bestx, besty)
        else:
            self.DrawNowWhite(bestx, besty)
        self.m_PcLastPos = (bestx, besty)
        for i in range(572):  # �޸ļ�������Ӻ����̵ı仯״��
            if self.m_bCTable[bestx][besty][i] and self.m_iWin[1][i] != 7:
                self.m_iWin[1][i] += 1
            if self.m_bPTable[bestx][besty][i]:
                self.m_bPTable[bestx][besty][i] = False
                self.m_iWin[0][i] = 7
        self.m_bComputer = False
        self.m_bPlayer = True

    def GiveScore(self, type, x, y):
        score = 0
        for i in range(572):  # �������
            if type == 1:
                if self.m_bCTable[x][y][i]:
                    if self.m_iWin[1][i] == 1:
                        score += 5
                    elif self.m_iWin[1][i] == 2:
                        score += 50
                    elif self.m_iWin[1][i] == 3:
                        score += 100
                    elif self.m_iWin[1][i] == 4:
                        score += 10000
            else:  # ����
                if self.m_bPTable[x][y][i]:
                    if self.m_iWin[0][i] == 1:
                        score -= 5
                    elif self.m_iWin[0][i] == 2:
                        score -= 50
                    elif self.m_iWin[0][i] == 3:
                        score -= 500
                    elif self.m_iWin[0][i] == 4:
                        score -= 5000
        return score

    def DrawNowWhite(self, x, y, dc=None):
        if dc == None:
            dc = wx.ClientDC(self)

        memDC = wx.MemoryDC()
        memDC.SelectObject(self.m_Bmpblack)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.OR_INVERT, True)
        memDC.SelectObject(self.m_Bmplastwhitechess)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.AND, True)

    def DrawNowBlack(self, x, y, dc=None):
        if dc == None:
            dc = wx.ClientDC(self)

        memDC = wx.MemoryDC()
        memDC.SelectObject(self.m_Bmpblack)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.OR_INVERT, True)
        memDC.SelectObject(self.m_Bmplastblackchess)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.AND, True)

    def DrawWhiteChess(self, x, y, dc=None):
        if dc == None:
            dc = wx.ClientDC(self)

        memDC = wx.MemoryDC()
        memDC.SelectObject(self.m_Bmpblack)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.OR_INVERT, True)
        memDC.SelectObject(self.m_Bmpwhitechess)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.AND, True)

    def DrawBlackChess(self, x, y, dc=None):
        if dc == None:
            dc = wx.ClientDC(self)

        memDC = wx.MemoryDC()
        memDC.SelectObject(self.m_Bmpblack)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.OR_INVERT, True)
        memDC.SelectObject(self.m_Bmpblackchess)
        dc.Blit(24 + x * 36 - x - 18, 25 + y * 36 - y - 18, 33, 33, memDC, 0, 0, wx.AND, True)

    def OnNew(self, e):
        self.InitValues()
        self.Refresh()

    def OnAbout(self, e):
        d = wx.MessageDialog(self, "�ο���һ����������VC��д�Ŀ�Դ���������\n��ֲ��qipengh \nEmail��qipengh@163.com", "����Python��Դ��ļ����������˻�����",
                             wx.OK)
        # Create a message dialog box
        d.ShowModal()  # Shows it
        d.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close()  # Close the frame.


def main():
    app = wx.App()
    frame = MainWindow(None, -1, "�������˻�����")
    frame.Show(1)
    # mainloop�������ڵĳ�Ա������Ҳ���Ǳ�ʾ��app������������ʼ�������ĺͼ��̵Ĳ�����
    app.MainLoop()


if __name__ == '__main__':
    main()
