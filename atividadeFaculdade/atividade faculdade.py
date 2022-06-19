tarifa = 0.28172
kwh = int(input('digite seu consumo em kwh: '))
fornecimento = (tarifa * kwh) + kwh

def icms (parmtr_fornecimento):
    if parmtr_fornecimento <= 200 :
        result_icms1 = (parmtr_fornecimento*0.136363)
        return result_icms1
    elif parmtr_fornecimento > 200 :
        result_icms2 = (parmtr_fornecimento*0.0333333)
        return result_icms2
    else:
        print('erro 404')

icms(fornecimento)
resultado_icms = icms(fornecimento)
print(resultado_icms)


def confins (parmtr_fornecimento):
    if parmtr_fornecimento <= 200 :
        result_confins1 = (parmtr_fornecimento*0.0614722)
        return result_confins1
    elif parmtr_fornecimento > 200 :
        result_confins2 = (parmtr_fornecimento*0.0730751)
        return result_confins2
    else:
        print('erro 404')


resultado_confins = confins(fornecimento)
print(resultado_confins)


def pisPasep (parmtr_fornecimento):
    if parmtr_fornecimento <= 200 :
        result_pisPasep1 = (parmtr_fornecimento*0.013346)
        return result_pisPasep1
    elif parmtr_fornecimento > 200 :
        result_pisPasep2 = (parmtr_fornecimento*0.0158651)
        return result_pisPasep2
    else:
        print('erro 404')

resultado_pisPasep = pisPasep(fornecimento)
print(resultado_pisPasep)

icms_confins = fornecimento*resultado_icms*resultado_confins
print(icms_confins)

icms_pisPasep = fornecimento*resultado_icms*resultado_pisPasep
print(icms_pisPasep)

valor_fatura = fornecimento+resultado_icms+resultado_confins+resultado_pisPasep+icms_confins+icms_pisPasep

print(f'o valor total da fatura é: {valor_fatura}')