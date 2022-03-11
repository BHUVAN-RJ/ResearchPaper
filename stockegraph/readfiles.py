import pandas as pd
import numpy as np
col = ['Date', 'Open', 'Close']
india = []

india_acc = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/acc.csv", usecols=col)
india_airtel = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/airtel.csv", usecols=col)
india_apollo = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/apollo.csv", usecols=col)
india_asian_paints = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/asianpaints.csv", usecols=col)
india_britannia = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/britannia.csv", usecols=col)
india_DLF = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/DLF.csv", usecols=col)
india_DMART = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/DMART.csv", usecols=col)
india_NTPC = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/NTPC.csv", usecols=col)
india_SBI = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/SBI.csv", usecols=col)
india_TCS = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/india/TCS.csv", usecols=col)

india = [india_NTPC, india_asian_paints, india_acc, india_apollo, india_SBI, india_DMART, india_britannia, india_TCS,
         india_airtel, india_DLF]

china_alibaba = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/alibaba.csv", usecols=col)
china_foods = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/chinafoods.csv", usecols=col)
china_mobile = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/chinamobiles.csv", usecols=col)
china_country = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/countrygarden.csv", usecols=col)
china_industrial_bank = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/industrialbank.csv", usecols=col)
china_medicine = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/jaingsumedicine.csv", usecols=col)
china_building_materials = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/petrochem.csv", usecols=col)
china_petrochemicals = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/alibaba.csv", usecols=col)
china_tencent = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/tencent.csv", usecols=col)
china_wise_ally = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/china/wiseally.csv", usecols=col)

china = [china_petrochemicals, china_building_materials, china_wise_ally, china_medicine, china_industrial_bank,
         china_alibaba, china_foods, china_tencent, china_mobile, china_country]

russia_cherkizovo = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/cherkizovo.csv", usecols=col)
russia_gazprom = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/gazprom.csv", usecols=col)
russia_GEMA = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/GEMA.csv", usecols=col)
russia_interRAO = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/interRAO.csv", usecols=col)
russia_PJS = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/PJS.csv", usecols=col)
russia_polyus = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/polyus.csv", usecols=col)
russia_sberbank = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/sberbank.csv", usecols=col)
russia_MCtelephone = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/telophone.csv", usecols=col)
russia_united_aircraft = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/unitedaircraft.csv", usecols=col)
russia_yandex = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/russia/yandex.csv", usecols=col)

russia = [russia_gazprom, russia_polyus, russia_united_aircraft, russia_GEMA, russia_sberbank, russia_interRAO,
          russia_cherkizovo, russia_yandex,russia_MCtelephone, russia_PJS]

uk_astra = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/astra.csv", usecols=col)
uk_british_tobacco = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/britishtobacco.csv", usecols=col)
uk_harbour = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/harbour.csv", usecols=col)
uk_helios = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/helios.csv", usecols=col)
uk_NEXT = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/NEXT.csv", usecols=col)
uk_ocado_group = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/ocadogroup.csv", usecols=col)
uk_prudential = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/prudential.csv", usecols=col)
uk_purple_bricks = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/purplebricks.csv", usecols=col)
uk_unilever = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/unilever.csv", usecols=col)
uk_rio_tinto = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/UK/riotinto.csv", usecols=col)

uk = [uk_harbour, uk_rio_tinto, uk_unilever, uk_astra, uk_prudential, uk_NEXT, uk_british_tobacco, uk_ocado_group,
      uk_helios, uk_purple_bricks]

usa_align = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/align.csv", usecols=col)
usa_american_tower = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/americantower.csv", usecols=col)
usa_apple = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/apple.csv", usecols=col)
usa_at_t = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/atandt.csv", usecols=col)
usa_bunge = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/bunge.csv", usecols=col)
usa_cv_stealth = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/cvstealth.csv", usecols=col)
usa_exxon = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/exxon.csv", usecols=col)
usa_JPmorgan = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/jpmorgan.csv", usecols=col)
usa_tesla = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/tesla.csv", usecols=col)
usa_united_steel = pd.read_csv("/Users/bhuvanrj/Desktop/paper/dataset/USA/unitedsteel.csv", usecols=col)

usa = [usa_exxon, usa_united_steel, usa_align, usa_cv_stealth, usa_JPmorgan, usa_tesla, usa_bunge, usa_apple, usa_at_t,
       usa_american_tower]


countries = {"russia": russia, "india": india, "china": china, "uk": uk, "usa": usa}


def name(x):
    return countries[x]


def percent(x, y):
    x1 = np.array(x).astype(float)
    x2 = np.array(y).astype(float)
    return np.multiply(np.divide(np.subtract(x2, x1), x1), 100)


class Data:
    def __init__(self, name1, country,i):
        self.name = name1
        self.i = i
        self.co = country

    def components(self):
        k = f"{self.co}" + f"_{self.i}"
        x_v = self.name.iloc[:, 0:1].values
        y_v = percent(self.name.iloc[:, 1:2].values, self.name.iloc[:, 2:3].values)
        self.i += 1
        return k, x_v, y_v




