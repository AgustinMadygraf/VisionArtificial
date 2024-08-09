import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from install.installer_utils import ProjectInstaller, ShortcutManager, BatFileCreator
from pathlib import Path
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class TestProjectInstaller(unittest.TestCase):

    @patch('src.installer_utils.LoggerConfigurator')
    @patch.object(Path, 'name', new_callable=PropertyMock, return_value='TestProject')
    def test_get_project_name(self, mock_name, MockLoggerConfigurator):
        mock_logger = MockLoggerConfigurator().configure()
        installer = ProjectInstaller()
        installer.logger = mock_logger

        project_name = installer.get_project_name()
        self.assertEqual(project_name, 'TestProject')

    @patch('src.installer_utils.BatFileCreator')
    @patch('src.installer_utils.ShortcutManager')
    @patch('src.installer_utils.LoggerConfigurator')
    def test_main(self, MockLoggerConfigurator, MockShortcutManager, MockBatFileCreator):
        mock_logger = MockLoggerConfigurator().configure()
        installer = ProjectInstaller()
        installer.logger = mock_logger

        with patch.object(installer, 'get_project_name', return_value='TestProject'):
            with patch('src.installer_utils.Path.is_file', return_value=False):
                installer.main()
                MockBatFileCreator().crear_archivo_bat_con_pipenv.assert_called_once()
                MockShortcutManager().create_shortcut.assert_called_once()

class TestShortcutManager(unittest.TestCase):

    @patch('win32com.client.Dispatch')
    def test_create_shortcut(self, MockDispatch):
        mock_logger = MagicMock()
        mock_strategy = MagicMock()
        mock_strategy.create_shortcut.return_value = True
        manager = ShortcutManager(Path('/dummy'), 'TestProject', mock_logger, mock_strategy)
        
        with patch('winshell.desktop', return_value='/dummy'):
            with patch.object(manager, 'verificar_icono', return_value=True):
                result = manager.create_shortcut(Path('/dummy/test.bat'))
                self.assertTrue(result)
                mock_strategy.create_shortcut.assert_called_once()

    def test_verificar_icono(self):
        mock_logger = MagicMock()
        mock_strategy = MagicMock()
        manager = ShortcutManager(Path('/dummy'), 'TestProject', mock_logger, mock_strategy)

        with patch('pathlib.Path.is_file', return_value=True):
            self.assertTrue(manager.verificar_icono(Path('/dummy/icon.ico')))

        with patch('pathlib.Path.is_file', return_value=False):
            self.assertFalse(manager.verificar_icono(Path('/dummy/icon.ico')))

class TestBatFileCreator(unittest.TestCase):

    def test_crear_archivo_bat_con_pipenv(self):
        mock_logger = MagicMock()
        creator = BatFileCreator(Path('/dummy'), 'TestProject', mock_logger)

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            creator.crear_archivo_bat_con_pipenv()
            mock_file.assert_called_once_with(Path('/dummy/TestProject.bat'), 'w')
            mock_file().write.assert_called_once()

if __name__ == '__main__':
    unittest.main()
