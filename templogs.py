import lasio
import OzMachine_python.load_art as art


class LogHandler:
    def __init__(self):
        las = lasio.read('ozwell3.las')
        self.n_zones = 50
        self.lith_names = ["Unknown", "Halite", "Gypsum", "Anhyrite", "Dolomite", "Dolomitic ls", "Cherty dol ls",
                           "Cherty dol", "Limestone", "Cherty ls", "Chert", "Shale", "Sandstone", "Ironstone", "Coal"]
        self.lith_index_map = [0, 1, 11, 2, 3, 11, 4, 7, 5, 11, 6, 10, 9, 8, 11, 12, 13, 11, 14]
        self.lith = []
        self.user_lith = []
        self.true_lith = las.curves.trul.data[0::4]
        depth = ['Depth (ft)'] + [x + int(las.curves.dept.data[0]) for x in range(10, 100, 10)]
        nphi = [x * 100 for x in las.curves.nphi.data]
        dphi = [x * 100 for x in las.curves.dphi.data]
        self.logs = {'GR': list(las.curves.gr.data),
                     'NPHI': list(nphi),
                     'DPHI': list(dphi),
                     'PE': list(las.curves.pef.data),
                     'DEPTH': list(depth)}

    def get_lith_art(self, lith):
        image_map = {
            'Unknown': art.UnknownIMG, 'Halite': art.HaliteIMG, 'Gypsum': art.GypsumIMG,
            'Anhydrite': art.AnhydriteIMG, 'Dolomite': art.DolomiteIMG, 'Dolomitic LS': art.DolomiticLSIMG,
            'Cherty Dol LS': art.ChertyDolLSIMG, 'Cherty Dol': art.ChertyDolIMG, 'Limestone': art.LimestoneIMG,
            'Cherty LS': art.ChertyLSIMG, 'Chert': art.ChertIMG, 'Shale': art.ShaleIMG,
            'Sandstone': art.SandstoneIMG, 'Ironstone': art.IronstoneIMG, 'Coal': art.CoalIMG
        }
        return image_map[lith]

    def get_lith_button_art(self, lith):
        return None

    def get_lith(self, lith):

        if isinstance(lith, str):
            return self.lith_names.index(lith)
        elif isinstance(lith, int):
            return self.lith_names[lith]
        else:
            raise TypeError('Must be string or integer')
