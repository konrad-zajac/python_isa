import io
from contextlib import redirect_stdout


class Helpers(object):
    """Klasa z przydatnymi narzedziami"""

    @staticmethod
    def get_print_output(callback):
        """
        Przechwytuje wydruk z funkcji uzywajacej print()
        :param funkcja: (function)
        :return: str
        """
        # tworzymu bufor w pamięci do przechowywania
        # wartości string
        memory_buffer = io.StringIO()

        # przekierowujemy standardowy output do buforu
        with redirect_stdout(memory_buffer):
            # wywołujemy funkcję przekazaną w argumencie
            callback()
            # zwracamy string z zawartościa naszego bufora
            return memory_buffer.getvalue()

if __name__ == '__main__':
    def print_cos():
        print('Wiktor')


    w = Helpers.get_print_output(print_cos)
    print(w.strip() == 'Wiktor')