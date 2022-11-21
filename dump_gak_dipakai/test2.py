from tabulate import tabulate

def z(x1, x2):
    return 8 * x1 + 6 * x2

def fb1(x1, x2):
    return 4 * x1 + 2 * x2 <= 60

def fb2(x1, x2):
    return 2 * x1 + 4 * x2 >= 48

class Simplex:
    def __init__(self, z, slack, rhs):
        self.tab = []
        self.z = z
        self.slack = slack
        self.rhs = rhs

        self.rk = 0
        self.ck = 0

        self.headers = ["z"]
        for i in range(len(self.z)):
            self.headers.append(f"x{i + 1}")
        for j in range(len(self.z)):
            self.headers.append(f"s{j + 1}")
        self.headers.append("rhs")
        self.headers.append("ratio")

    def showTable(self):
        print(tabulate(self.tab, self.headers, tablefmt="grid"))

    def initTableu(self):
        if(len(self.tab) == 0):
            tab0 = []
            tab0.append(1)
            for j in range(len(self.z)):
                tab0.append(-1 * self.z[j])
            for k in range(len(self.z)):
                tab0.append(0)
            tab0.append(0)
            tab0.append(0)
            self.tab.append(tab0)
            for i in range(len(self.slack)):
                tabx = []
                tabx.append(0)
                for f in range(len(self.z)):
                    tabx.append(self.slack[i][f])
                for h in range(len(self.z)):
                    tabx.append(0)
                tabx.append(self.rhs[i])
                tabx.append(0)
                self.tab.append(tabx)
                self.tab[i + 1][len(self.z)+ 1 + i] = 1

        self.columnKey()
        self.rowKey()

    def columnKey(self):
        xTab = []
        columnK = 0
        for ma in self.tab:
            xTab.append(min(ma))
        for i in range(len(self.tab)):
            if(min(xTab) in self.tab[i]):
                columnK = self.tab[i].index(min(xTab))
        self.ck = columnK

    def rowKey(self):
        cTab = []
        for i in range(len(self.slack)):
            ratio = self.tab[i + 1][-2] / self.tab[i + 1][self.ck]
            self.tab[i + 1][-1] = ratio
            cTab.append(ratio)
        self.rk = cTab.index(min(cTab)) + 1

    def obd(self):
        pivot = self.tab[self.ck][self.rk]
        for i in range(len(self.tab[self.ck]) - 1):
            self.tab[self.ck][i] = self.tab[self.ck][i] / pivot

        for j in range(len(self.tab) - 1):
            oper = self.tab[self.ck - j - 1][self.rk]
            for k in range(len(self.tab[self.ck]) - 1):
                self.tab[self.ck - j - 1][k] = self.tab[self.ck - j - 1][k] - (oper * self.tab[self.ck][k])

        self.columnKey()
        self.rowKey()

    def run(self):
        self.initTableu()
        self.showTable()
        print("")
        while(True):
            try:
                self.obd()
            except:
                break
            self.showTable()
            print("")

        print(f"Jadi, nilai x1 = {self.tab[1][-2]} dan x2 = {self.tab[2][-2]}.")
        print(f"Maka nilai maksimum z adalah {z(self.tab[1][-2], self.tab[2][-2])}")

pp = Simplex([8,6], [[4, 2], [2, 4]], [60, 48])
pp.run()