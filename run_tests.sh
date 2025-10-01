# Verifica se o ambiente virtual está ativo
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo "AVISO: Ambiente virtual não detectado!"
    echo "Recomenda-se ativar o ambiente virtual antes de executar este script:"
    echo "source venv/bin/activate"
    
    # Pergunta se deseja continuar
    read -p "Deseja continuar mesmo assim? (s/n): " choice
    if [[ "$choice" != "s" && "$choice" != "S" ]]; then
        echo "Abortando execução. Ative o ambiente virtual e tente novamente."
        exit 1
    fi
fi

echo "Executando testes unitários..."
python -m pytest tests/unit -v --html=evidence/report.html --self-contained-html

echo "Testes concluídos! Relatório disponível em:"
echo "- evidence/report.html"
