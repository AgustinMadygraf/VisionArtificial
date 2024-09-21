"""
tests/test_install.py
Archivo de pruebas unitarias para la instalación del proyecto.
"""

import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.install.project_installer import ProjectInstaller

class TestProjectInstaller(unittest.TestCase):
    """
    Clase para probar la instalación del proyecto.
    """

    @patch('src.install.project_installer.logging.getLogger')
    @patch('src.install.project_installer.ProjectNameRetriever')
    def setUp(self, MockProjectNameRetriever, MockGetLogger):
        """
        Configuración inicial para las pruebas.
        """
        self.mock_logger = MagicMock()
        MockGetLogger.return_value = self.mock_logger

        self.mock_project_name_retriever = MagicMock()
        MockProjectNameRetriever.return_value = self.mock_project_name_retriever
        self.mock_project_name_retriever.get_project_name.return_value = "TestProject"

        # Crear la instancia del instalador después de configurar los mocks
        self.installer = ProjectInstaller()

    def test_initialization(self):
        """
        Prueba la inicialización del instalador del proyecto.
        """
        self.assertEqual(self.installer.name_proj, "TestProject")
        self.mock_logger.info.assert_called_with("Logger configurado correctamente.")

    @patch('src.install.project_installer.print')
    def test_main(self, mock_print):
        """
        Prueba el método principal de instalación.
        """
        self.installer.main()
        mock_print.assert_any_call("Iniciando instalador")
        mock_print.assert_any_call(f"Directorio del script: {self.installer.project_dir}")
        mock_print.assert_any_call(f"Nombre del proyecto: {self.installer.name_proj}")

if __name__ == '__main__':
    unittest.main()
