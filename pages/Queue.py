import streamlit as st

class Queue:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

# Fungsi utama untuk memproses permainan
def suspense_game(n, binarystring):
    resultstring = []

    # Cek apakah input valid (biner)
    for i in range(n):
        if binarystring[i] not in ['0', '1']:
            return "Invalid input"

    # Membagi string menjadi pilihan Alice dan Bob
    if n % 2 == 0:
        alice_choices = binarystring[:n // 2]
        bob_choices = binarystring[n // 2:]
    else:
        alice_choices = binarystring[:(n // 2) + 1]
        bob_choices = binarystring[(n // 2) + 1:]

    reverse_bob_choices = bob_choices[::-1]

    elemen_alice = Queue()
    elemen_bob = Queue()

    for char in alice_choices:
        elemen_alice.enqueue(char)

    for char in reverse_bob_choices:
        elemen_bob.enqueue(char)

    # Game-play untuk Alice dan Bob
    is_alice_turn = True
    while not (elemen_alice.is_empty() and elemen_bob.is_empty()):
        if is_alice_turn and not elemen_alice.is_empty():
            char = elemen_alice.dequeue()
            # Alice tries to make resultstring lexicographically smallest
            if resultstring and char < resultstring[0]:
                resultstring.insert(0, char)
            else:
                resultstring.append(char)
        elif not is_alice_turn and not elemen_bob.is_empty():
            char = elemen_bob.dequeue()
            # Bob tries to make resultstring lexicographically largest
            if resultstring and char > resultstring[0]:
                resultstring.insert(0, char)
            else:
                resultstring.append(char)

        # Alternate turns
        is_alice_turn = not is_alice_turn

    # Menggabungkan list menjadi string untuk hasil akhir
    final_result = ''.join(resultstring)
    return final_result

# Streamlit UI
st.title("Suspense String Game")
st.write("Selamat datang di permainan Suspense String! Masukkan string biner untuk melihat hasil akhir setelah permainan.")

# Input user untuk panjang dan string biner
n = st.number_input("Masukkan jumlah elemen dalam string biner:", min_value=1, step=1)
binarystring = st.text_input("Masukkan string biner:")

# Validasi input dan menampilkan hasil
if st.button("Lihat Hasil Permainan"):
    if len(binarystring) != n:
        st.write("Panjang string biner harus sama dengan jumlah elemen yang dimasukkan.")
    else:
        hasil = suspense_game(n, binarystring)
        if hasil == "Invalid input":
            st.write("Input tidak valid. Pastikan hanya memasukkan karakter '0' dan '1'.")
        else:
            st.write("Hasil string T setelah bermain adalah:")
            st.write(hasil)

# Tombol "Lihat Kode" menggunakan expander
with st.expander("Lihat Kode Program"):
    st.code('''\
import streamlit as st

class Queue:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

def suspense_game(n, binarystring):
    resultstring = []
    for i in range(n):
        if binarystring[i] not in ['0', '1']:
            return "Invalid input"
    if n % 2 == 0:
        alice_choices = binarystring[:n // 2]
        bob_choices = binarystring[n // 2:]
    else:
        alice_choices = binarystring[:(n // 2) + 1]
        bob_choices = binarystring[(n // 2) + 1:]
    reverse_bob_choices = bob_choices[::-1]
    elemen_alice = Queue()
    elemen_bob = Queue()
    for char in alice_choices:
        elemen_alice.enqueue(char)
    for char in reverse_bob_choices:
        elemen_bob.enqueue(char)
    is_alice_turn = True
    while not (elemen_alice.is_empty() and elemen_bob.is_empty()):
        if is_alice_turn and not elemen_alice.is_empty():
            char = elemen_alice.dequeue()
            if resultstring and char < resultstring[0]:
                resultstring.insert(0, char)
            else:
                resultstring.append(char)
        elif not is_alice_turn and not elemen_bob.is_empty():
            char = elemen_bob.dequeue()
            if resultstring and char > resultstring[0]:
                resultstring.insert(0, char)
            else:
                resultstring.append(char)
        is_alice_turn = not is_alice_turn
    final_result = ''.join(resultstring)
    return final_result
    ''', language='python')
