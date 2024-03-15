'''
Aplikasi deteksi gempa
MODULARISASI dengan FUNCTION
MODULARISASI dengan PACKAGE
'''
import gempa_terkini

if __name__ == '__main__':
    print ('Aplikasi utama')
    result = gempa_terkini.ekstraksi_data()
    gempa_terkini.tampilkan_data(result)
    