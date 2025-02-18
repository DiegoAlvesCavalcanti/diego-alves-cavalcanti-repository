dist_metros = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(dist_metros, (dist_metros/1000), (dist_metros/100), (dist_metros/10), (dist_metros*10), (dist_metros*100), (dist_metros*1000)))

