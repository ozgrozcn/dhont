parties = {
	"chp":[],
	"akp":[],
	"mhp":[],
	"iyip":[],
	"hdp":[],
	"tip":[],
	"diger":[]
}
numberOfDeputy = {
	"chp":0,
	"akp":0,
	"mhp":0,
	"iyip":0,
	"hdp":0,
	"tip":0,
	"diger":0
} 
districtDeputyNumber = int(input("Bölgedeki toplam milletvekili hakkını giriniz: "))
rates = list()
persistence = 100

for i in parties.keys():
	while True:
		value = float(input("{} oy oranını giriniz:".format(i.upper())))
		if (value <= persistence):
			parties[i].append(value)
			persistence -= value
			print("Kalan yüzdelik dilim: % {}\n".format(persistence))
			break
		else:
			print("Girilen değer yüzdelik dilimi aşmaktadır.\nKalan %'lik dilim: {}".format(persistence))
			continue

for p in parties.keys():
	rates.append(parties[p][0])
	for v in range(2, int(parties[p][0]) + 1):
		r = parties[p][0] / v
		parties[p].append(r)
		rates.append(r)
	

rates = set(rates)
rates = list(rates)
rates.sort(reverse=True)

for party in numberOfDeputy.keys():
	for rate in rates[:districtDeputyNumber]:
		if (parties[party].count(rate) != 0):
			numberOfDeputy[party] += 1
		else: 
			continue
print("-" * 30)
for result in numberOfDeputy.keys():
	print("{} {} milletvekili çıkarıyor.\n".format(result.upper(), numberOfDeputy[result]), "-"*30, sep="")
