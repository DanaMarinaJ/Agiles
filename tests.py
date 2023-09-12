from main import Ahorcado
import unittest

class TestAhorcado(unittest.TestCase):

    def test_arriesgar_palabra_correcta(self):

        juego = Ahorcado()        
        self.assertTrue(juego.arriesgar_palabra("hola"))
    
    def test_arriesgar_palabra_incorrecta(self):
        juego = Ahorcado()
        self.assertFalse(juego.arriesgar_palabra("chau"))

    def test_arriesgar_letra_correcta(self):
        juego = Ahorcado()        
        self.assertTrue(juego.arriesgar_letra("l"))
    
    def test_arriesgar_letra_incorrecta(self):
        juego = Ahorcado()        
        self.assertFalse(juego.arriesgar_letra("k"))
    
    def test_devolver_posicion_mayor_cero(self):
        juego = Ahorcado()
        self.assertGreater(juego.devolver_posicion_letra("o"),0)

if __name__ == '__main__':
   unittest.main()