import random
import load_art as art


class LogHandler:

    def __init__(self):
        self.n_zones = 50
        self.lith_names = ["Unknown", "Halite", "Gypsum", "Anhydrite", "Dolomite", "Dolomitic LS", "Cherty Dol LS",
                           "Cherty Dol", "Limestone", "Cherty LS", "Chert", "Shale", "Sandstone", "Ironstone", "Coal"]
        self.lith_index_map = [0, 1, 11, 2, 3, 11, 4, 7, 5, 11, 6, 10, 9, 8, 11, 12, 13, 11, 14]
        self.lith = self.Lithology()
        self.user_lith = []
        self.true_lith = []
        self.logs = {}
        self.generate_sequence()

    def generate_sequence(self):
        mark = self.MarkovChain()
        self.lith = self.Lithology()

        self.true_lith = []

        for i in range(self.n_zones):
            self.true_lith.append(mark.next_state())

        ls = self.log_suite(self.lith, self.true_lith, 4, 10.0)

        self.true_lith = [self.lith_index_map[x] for x in self.true_lith]

        u = random.uniform(0, 1)
        depth_0 = int(1950 + 10 * int(u * 325.0))
        depth = ['Depth (ft)'] + list(range(depth_0, depth_0 + 90, 10))

        self.logs = {'GR': ls.gamma,
                     'NPHI': ls.nphi,
                     'DPHI': ls.dphi,
                     'PE': ls.pef,
                     'DEPTH': depth}

    class MarkovChain:

        def __init__(self):
            self.state = 0
            self.current_length = 0
            self.entry_prob = [0.0375, 0.075, 0.1125, 0.15, 0.21, 0.27, 0.33, 0.39, 0.45, 0.51, 0.57, 0.63, 0.69, 0.75,
                               0.8125, 0.875, 0.9375, 1.0]
            self.trans_prob = [
                [0.82, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.1, 0.6, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.35, 0.65, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.35, 0.4, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.2, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.06, 0.86, 0.92, 0.98, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.8, 0.8, 0.8, 0.92, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.08, 0.08, 0.88, 0.88, 0.92, 0.92, 0.92, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.07, 0.07, 0.07, 0.9, 0.9, 0.9, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2, 0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.15, 0.15, 0.15, 0.15, 0.85, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.12, 0.12, 0.12, 0.21, 0.91, 1.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.15, 0.85, 1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.09, 0.94, 0.94, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.09, 0.12, 0.82, 1.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.48, 0.48, 0.6, 1.0]]

        def next_state(self):

            if self.state == 0:
                u = random.uniform(0, 1)
                i = 1
                while (i <= 18) and (u >= self.entry_prob[i - 1]):
                    i += 1
                self.state = i
                self.current_length = 1

                return self.state

            else:
                u = random.uniform(0, 1)
                i = 1
                while (i <= 18) and (u >= self.trans_prob[self.state - 1][i - 1]):
                    i += 1
                if self.state == 1:
                    self.current_length += 1
                else:
                    self.current_length = 1
                self.state = i
                return self.state

    class Lithology:
        def __init__(self):
            self.min_comp = []
            self.comp_mat = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [99.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 35.0, 55.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.0],
                             [0.0, 99.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 99.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0, 55.0, 35.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.0],
                             [0.0, 0.0, 0.0, 0.0, 90.0, 1.0, 1.0, 0.0, 0.0, 0.0, 8.0],
                             [0.0, 0.0, 0.0, 0.0, 47.0, 47.0, 1.0, 0.0, 0.0, 0.0, 8.0],
                             [0.0, 0.0, 0.0, 0.0, 47.0, 1.0, 47.0, 0.0, 0.0, 0.0, 5.0],
                             [0.0, 0.0, 0.0, 55.0, 0.0, 0.0, 35.0, 0.0, 0.0, 0.0, 10.0],
                             [0.0, 0.0, 0.0, 0.0, 32.0, 32.0, 32.0, 0.0, 0.0, 0.0, 8.0],
                             [0.0, 0.0, 0.0, 0.0, 1.0, 88.0, 1.0, 0.0, 0.0, 0.0, 10.0],
                             [0.0, 0.0, 0.0, 0.0, 1.0, 44.0, 45.0, 0.0, 0.0, 0.0, 4.0],
                             [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 96.0, 0.0, 0.0, 0.0, 2.0],
                             [0.0, 0.0, 0.0, 55.0, 0.0, 35.0, 0.0, 0.0, 0.0, 0.0, 10.0],
                             [0.0, 0.0, 0.0, 1.0, 0.0, 75.0, 0.0, 0.0, 0.0, 0.0, 25.0],
                             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 50.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0, 0.0, 35.0, 0.0, 0.0, 55.0, 0.0, 10.0],
                             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 90.0, 10.0]]

        def get_comp(self, lith_index, fuzz):
            min_comp = []
            comp_sum = 0.0

            for i in range(0, 11):

                min_comp.append(self.comp_mat[lith_index][i])

                if min_comp[i] > 0.0:
                    min_comp[i] += fuzz * random.uniform(0, 1)

                comp_sum += min_comp[i]

            if comp_sum > 0.0:
                for i in range(0, 11):
                    min_comp[i] = min_comp[i] / comp_sum

            return min_comp

    class log_suite:

        def __init__(self, lith, lith_index, nmpz, fuzz):

            gamma_vals = [5.0, 5.0, 5.0, 200.0, 12.0, 15.0, 10.0, 5.0, 130.0, 5.0, 0.0]
            nphi_vals = [-3.0, 60.0, -2.0, 30.0, 5.0, -5.0, 0.0, 12.0, 38.0, 35.0, 100.0]
            rhob_vals = [2.04, 2.35, 2.98, 2.8, 2.87, 2.65, 2.71, 3.89, 2.63, 1.77, 1.0]
            u_vals = [9.59, 9.4, 15.2, 8.48, 8.9, 4.8, 13.8, 58.4, 3.92, 0.32, 0.5]

            nzones = len(lith_index)
            self.nmsmts = nmpz * nzones
            self.gamma = [0] * self.nmsmts
            self.nphi = [0] * self.nmsmts
            self.dphi = [0] * self.nmsmts
            self.pef = [0] * self.nmsmts

            i = 0

            for j in range(0, nzones):

                for k in range(0, nmpz):

                    comp = lith.get_comp(lith_index[j], fuzz)
                    rhob = 0.0
                    u = 0.0

                    for m in range(0, 11):
                        tempvar = self.gamma
                        tempvar[i] += gamma_vals[m] * comp[m]
                        tempvar = self.nphi
                        tempvar[i] += nphi_vals[m] * comp[m]
                        rhob += rhob_vals[m] * comp[m]
                        u += u_vals[m] * comp[m]

                    tempvar = self.gamma
                    tempvar[i] += 10.0 * random.uniform(0, 1)
                    self.dphi[i] = 100 * (2.71 - rhob) / 1.7
                    self.pef[i] = u / rhob

                    i += 1

            self.convolve(self.gamma)
            self.convolve(self.nphi)
            self.convolve(self.dphi)
            self.convolve(self.pef)

        def convolve(self, x):
            n = len(x)
            xtemp = [None] * n

            xtemp[0] = x[0]
            xtemp[1] = 0.25 * x[0] + 0.5 * x[1] + 0.25 * x[2]

            i = 2
            while i < n - 2:
                xtemp[i] = 0.05 * x[i - 2] + 0.2 * x[i - 1] + 0.5 * x[i] + 0.2 * x[i + 1] + 0.05 * x[i + 2]
                i += 1
            xtemp[n - 2] = 0.25 * x[n - 3] + 0.5 * x[n - 2] + 0.25 * x[n - 1]
            xtemp[n - 1] = x[n - 1]

            i = 0
            while i < n:
                x[i] = xtemp[i]
                i += 1

    def get_lith_art(self, lith):
        image_map = {
            'Unknown': art.UnknownIMG, 'Halite': art.HaliteIMG, 'Gypsum': art.GypsumIMG,
            'Anhydrite': art.AnhydriteIMG, 'Dolomite': art.DolomiteIMG, 'Dolomitic LS': art.DolomiticLSIMG,
            'Cherty Dol LS': art.ChertyDolLSIMG, 'Cherty Dol': art.ChertyDolIMG, 'Limestone': art.LimestoneIMG,
            'Cherty LS': art.ChertyLSIMG, 'Chert': art.ChertIMG, 'Shale': art.ShaleIMG,
            'Sandstone': art.SandstoneIMG, 'Ironstone': art.IronstoneIMG, 'Coal': art.CoalIMG
        }
        return image_map[lith]

    def get_lith(self, lith):
        if isinstance(lith, str):
            return self.lith_names.index(lith)
        elif isinstance(lith, int):
            return self.lith_names[lith]
        else:
            raise TypeError('Must be string or integer')
