import math

# tehtävä 5

leiviskat_lkm = float(input('Anna leiviskien määrä:'))
naulat_lkm = float(input('Anna naulojen määrä:'))
luodit_lkm = float(input ('Anna luotien määrä:'))

# lasketaan leiviskät mukaan nauloihin
naulat_lkm = leiviskat_lkm * 20 + naulat_lkm
# lasketaan naulat mukaan luoteihin
luodit_lkm = naulat_lkm * 32 + luodit_lkm

# välitarkastus
#print('Koko massa luoteina: {luodit_lkm}')

massa_g = luodit_lkm * 13,3

print(f'Massa nykymittojen mukaan: {massa_g // 1000:.0f} kiloa ja {massa_g % 1000} grammaa.')
