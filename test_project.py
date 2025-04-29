import pytest
from unittest.mock import MagicMock, patch
from project import show, clear, solve, backspace, initialize_tkinter

'''
> intinya, function di project itu gaada yang return value semua. dia hanya mengubah state GUI
> kita pakai MagicMock supaya kita bisa meniru perilaku objek tanpa harus menjalankan kode aslinya, 
    apalagi yang pakai lingkungan eksternal kayak GUI atau database.
> dengan magic mock kita bisa memalsukan fungsi dari StringVar() dan Tk()
    (root dan equation, variabel yang daritadi bermasalah)
> Kontrol Penuh terhadap Perilaku: 
    Kamu bisa menentukan apa yang terjadi ketika fungsi tertentu dipanggil. 
    Misalnya, equation.get = MagicMock(return_value="") berarti setiap kali equation.get() dipanggil, 
    ia akan mengembalikan string kosong ("") tanpa harus benar-benar mengambil nilai dari GUI.
'''  
# Mocking the Tkinter functions
@pytest.fixture(autouse=True)
def mock_tkinter(mocker):
    global equation
    # Patch Tk and StringVar
    with patch('project.Tk'), patch('project.StringVar') as MockStringVar:
        equation = MockStringVar.return_value
        equation.set = MagicMock()
        equation.get = MagicMock(return_value="")   
        '''
        > equation.get return string kosong supaya kalau ga sengaja kepanggil, ga bakal jadi masalah
            sebenernya gaada pake get sih
        > intinya disini kita fokus ke equation.set
        '''

        # Initialize the mock setup
        initialize_tkinter()
        clear()

def test_show():
    show('5')
    show('+')
    show('3')
    equation.set.assert_called_with('5+3')  # Use assert_called_with, not called_with

def test_clear():
    show('5')
    clear()
    equation.set.assert_called_with('')

def test_solve_addition():
    show('5')
    show('+')
    show('3')
    solve()
    equation.set.assert_called_with(8)  # Check if 5 + 3 = 8

def test_solve_subtraction():
    show('10')
    show('-')
    show('4')
    solve()
    equation.set.assert_called_with(6)  # Check if 10 - 4 = 6

def test_solve_multiplication():
    show('6')
    show('x')
    show('2')
    solve()
    equation.set.assert_called_with(12)  # Check if 6 * 2 = 12

def test_solve_division():
    show('8')
    show('/')
    show('4')
    solve()
    equation.set.assert_called_with(2)  # Check if 8 / 4 = 2

def test_percentage():
    show('50')
    show('%')
    solve()
    equation.set.assert_called_with(0.5)  # Check if 50% = 0.5

def test_backspace():
    show('543')
    backspace()
    equation.set.assert_called_with('54')  # Check if last digit removed

def test_backspace_on_empty():
    clear()  # Ensure it's empty first
    backspace()
    equation.set.assert_called_with('')  # Check if backspace on empty input does nothing
