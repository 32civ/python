frutas = {'Plátano':4000, 'Manzana':10000, 'Pera':9000, 'Naranja':5000, 'Guayaba':4000, 'Sandia':12000, 'Banana':4000, 'Fresa':8000}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")