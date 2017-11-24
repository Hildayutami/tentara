class dataOperasi:
    def __init__(self, operasi, sulit):
        self.operasi = operasi
        self.sulit = sulit

    def __str__(self):
        return ("operasi "+self.operasi+self.sulit)
        
class dataTentara:
    def __init__(self, nama, umur, kekuatan):
        self.nama = nama
        self.umur = umur
        self.kekuatan = kekuatan
        self.level = 1

    def __str__(self):
        nama = "Nama: "+self.nama
        umur = "HP: "+str(self.umur)
        kekuatan = "Power: "+str(self.kekuatan)
        return(nama,umur,kekuatan)

    def __repr__(self):
        data = self.nama,self.umur,self.kekuatan
        return str(data)

    def set_kekuatan(self, banyak):
        self.kekuatan += banyak

    def set_level(self, naik):
        self.level += naik

    def get_nama(self):
        return self.nama

    def get_umur(self):
        return self.umur

    def get_kekuatan(self):
        return self.kekuatan

        
class Tentara:
    def __init__(self, n):
        self.d = {}
        self.operasi = []
        
        for i in range(n):
            #snipper 3
            print("jenis tentara dan jumlahnya")
            b = input().split()

            if b[0] not in self.d: 
                self.d[b[0]]=[]
                
            for j in range(int(b[1])):
                print("masukkan data per tentara")
                c = input() # ===> agus;12;12
                data_diri = c.split(";")
                  
                self.d[b[0]].append(dataTentara(data_diri[0],data_diri[1],data_diri[2]))
   

    def new_tentara(self, jenis, list_data):
        data = list_data.split(";")
        if jenis in self.d:  #kalau udah ada
            self.d[jenis].append(dataTentara(data[0],data[1],data[2]))
        else:
            self.d[jenis]=[]
            self.d[jenis].append(dataTentara(data[0],data[1],data[2]))

        print(data[0]+" bergabung")

    def new_operasi(self, nama_operasi, tingkat_sulit):
        if nama_operasi in self.operasi:  #kalau udah ada
            self.operasi.append(dataOperasi(nama_operasi,tingkat_sulit))
        else:
            self.operasi=[]
            self.operasi.append(dataOperasi(nama_operasi,tingkat_sulit))

        print(nama_operasi+" dengan tingkat kesulitan "+tingkat_sulit+" berhasil dibuat")
         

    def join_operasi(self, jenis_tentara, nama, nama_operasi):
        if jenis_tentara in self.d:
            #for j in self.d.values():
                #if nama not in self.d:
                #    print("Tidak ada jenis tentara "+jenis_tentara+" bernama "+nama)

                if nama_operasi in self.operasi.keys():
                    self.operasi.append([jenis_tentara,nama])
                    print("berhasil tambahin")
                           
                else:   
                    print("Tidak ada operasi bernama "+nama_operasi)

        else:
            print("Tidak ada jenis tentara "+jenis_tentara)


    def keluar_operasi(self, nama, nama_operasi):
        if nama_operasi in self.operasi:
            if nama in nama_operasi:
                for i in range(len(operasi)-1):
                    for j in range(len(operasi[i])-1):
                        if nama in operasi[i][j]:
                            operasi[j].append([])
                            data = operasi[i][j]
                            operasi[i].remove(data)
            else:
                print("Tidak ada tentara bernama "+nama+" pada tim operasi "+nama_operasi)
        else:
            print("Tidak ada operasi bernama "+nama_operasi)


    def pelatihan(self,jenis):
        if jenis in self.d:
            for key in self.d.keys():
                if key == jenis:
                    print(self.d[key].set_kekuatan(100))
                    
        else:
            print("Tidak ada "+jenis)

    def beraksi(self, nama_operasi):
        if nama_operasi in self.operasi:
            for i in self.operasi:
                if self.operasi[i][2] <= 0:
                    print("Tidak ada personil pada tim operasi "+nama_operasi)
                else:
                    
                    
        else:
            print("Tidak ada operasi "+nama_operasi)
        


print("nilai awal")
t = Tentara(int(input()))

while(True):
    #masukan perintah
    print("masukkan perintah baru")
    perintah = input().split()    

    #NEW​ ​TENTARA​ ​Fighter​ ​Boy;25;125
    if perintah[0] == 'new' and perintah[1] == 'tentara':    
        t.new_tentara(perintah[2],perintah[3])
    
    
    #NEW​ ​OPERASI​ ​Trikora​ ​2 (tingkat kesulitan)
    elif perintah[0] == 'new' and perintah[1] == 'operasi':
        t.new_operasi(perintah[2],perintah[3])

    #MASUK​ ​Sniper​ ​Yumna​ ​Trikora
    elif perintah[0] == 'masuk':
        t.join_operasi(perintah[1],perintah[2],perintah[3])


    #KELUAR​ ​Jarjit​ ​Trikora
    elif perintah[0] == 'keluar':
        t.keluar_operasi(perintah[1],perintah[2])

    #pelatihan sniper
    elif perintah[0] == 'pelatihan':
        t.pelatihan(perintah[1])

    #BERAKSI​ OPERASI​ <namaOperasi​>
    elif perintah[0] == 'beraksi':
        t.beraksi(perintah[2])



