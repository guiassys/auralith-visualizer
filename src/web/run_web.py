"""Script para executar a interface Web do Auramove."""

import sys
import os

# Adiciona o diretório raiz do projeto ao path para importar módulos
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

from src.web.app import interface

if __name__ == "__main__":
    print("🚀 Iniciando Auralith-Visualizer...")
    print("📱 Acesse: http://localhost:7861")
    print("❌ Pressione Ctrl+C para parar")

    interface.launch(
        server_name="0.0.0.0",
        server_port=7861,
        show_error=True
    )