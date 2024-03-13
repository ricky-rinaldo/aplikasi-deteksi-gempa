'''
Aplikasi deteksi gempa
MODULARISASI dengan FUNCTION
'''


def ekstraksi_data():
    '''
    tanggal: 13 Maret 2024
    waktu: 23:39:21 WIB
    magnitudo: 5.2
    kedalaman: 182 km
    lokasi: LS 6.58, BT 129.99
    pusat gempa: 212 km BaratLaut TANIMBAR
    keterangan: tidak berpotensi TSUNAMI
    :return:
    '''
    hasil = dict()
    hasil['tanggal']= '13 Maret 2024'
    hasil['waktu']= '23:39:21 WIB'
    hasil['magnitudo']= 5.2
    hasil['kedalaman']= '182 km'
    hasil['lokasi']= {'ls':6.58, 'bt':129.99}
    hasil['pusat_gempa']= '212 km Barat Laut TANIMBAR'
    hasil['keterangan']= 'tidak berpotensi TSUNAMI'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG :')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi : LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Pusat Gempa {result['pusat_gempa']}")
    print(f"Keterangan {result['keterangan']}")


if __name__ == '__main__':
    print ('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
    