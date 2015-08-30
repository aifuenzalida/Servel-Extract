rawdata = open("A1321029.txt")
OutputFile = open("A1321029-v2.txt", 'w')
users = []
OutputFile.write('Nombre' + ';' + 'RUT' + ';' + 'Sexo' + ';' +
                 'Domicilio' + ';' + 'Circunscripcion' + ';' + 'Mesa')
OutputFile.write("\n")
for line in rawdata:
    if len(line) >= 40:
        user = {}
        guion = "-"
        dist1 = "PROVIDENCIA"
        discriminador = "ELECTORAL"
        posdiscriminador = line.find(discriminador,0)
        if posdiscriminador == -1:
            largodist1 = len(dist1)
            largolinea = len(line)
            posguion = line.find(guion, 20)
            posvar = line.find(" VAR ", 0)
            posmuj = line.find(" MUJ ", 0)
            posdist1 = line.find(dist1, largolinea - 25)
            varesp = " "
            comrut = line.find(varesp, posguion - 11)
            cierremesa = line.find(varesp, largolinea - 4)
            user['nombre'] = line[0: posguion - 10].strip()
            user['rut'] = line[comrut:posguion + 2].strip()

            if posvar == -1:
                user['sexo'] = line[posmuj + 1:posmuj + 4].strip()
            elif posmuj == -1:
                user['sexo'] = line[posvar + 1:posvar + 4].strip()

            user['direccion'] = line[posguion + 6:posdist1].strip()
            user['circunscripcion'] = line[posdist1:posdist1 + largodist1].strip()
            user['mesa'] = line[posdist1 + largodist1:cierremesa].strip()

            users.append(user)

for user in users:
    OutputFile.write(user['nombre'] + ';' + user['rut'] + ';' +user['sexo'] + ';' + user['direccion'] + ';' + user['circunscripcion'] + ';' + user['mesa'])
    OutputFile.write("\n")
rawdata.close()
OutputFile.close()
