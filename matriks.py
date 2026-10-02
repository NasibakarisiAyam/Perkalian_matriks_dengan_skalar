##fungsi input
def input_matriks():
    print("=== Input Matriks Persegi ===")
    while True:
        try:
            n = int(input("Masukkan ordo/ukuran matriks persegi (N): "))
            if n <= 0:
                print("Error: Ukuran matriks harus lebih besar dari 0!")
                continue
            break
        except ValueError:
            print("Error: Harap masukkan angka bulat positif.")
    
    matriks = []
    print(f"\nMasukkan {n} elemen per baris (pisahkan angka dengan spasi):")
    for i in range(n):
        while True:
            try:
                data_baris = list(map(float, input(f"Baris ke-{i+1}: ").split()))
                if len(data_baris) != n:
                    print(f"Error: Harap masukkan tepat {n} angka untuk matriks {n}x{n}!")
                    continue
                matriks.append(data_baris)
                break
            except ValueError:
                print("Error: Input harus berupa angka. Silakan coba lagi.")
                
    return matriks, n


##main Function
def main():
    #input matriks
    matriks, n = input_matriks()
    
    #Input Skalar
    print("\n=== Input Skalar ===")
    while True:
        try:
            skalar = float(input("Masukkan nilai skalar: "))
            break
        except ValueError:
            print("Error: Skalar harus berupa angka.")
    
    #Hitung Perkalian Matriks dengan Skalar
    hasil = [[elemen * skalar for elemen in baris] for baris in matriks]
    
    # 4. Tampilkan Hasil
    print("\n" + "="*35)
    print(f"HASIL PERKALIAN MATRIKS ({n}x{n})")
    print("="*35)
    for baris in hasil:
        formatted_baris = [f"{val:g}" for val in baris]
        print("[ " + "  ".join(formatted_baris) + " ]")

if __name__ == "__main__":
    main()