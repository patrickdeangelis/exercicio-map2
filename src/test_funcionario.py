import pytest
from funcionario import Funcionario


class TestFuncionario:
    @pytest.fixture
    def funcionario_exemplo(self):
        return Funcionario(
            "João Silva",
            "Desenvolvedor Sênior",
            8000.0,
            "Rua das Flores, 123",
            "São Paulo",
            "01234-567"
        )

    def test_init(self, funcionario_exemplo):
        assert funcionario_exemplo.get_nome() == "João Silva"
        assert funcionario_exemplo.get_cargo() == "Desenvolvedor Sênior"
        assert funcionario_exemplo.get_salario_base() == 8000.0

    def test_formatar_endereco(self, funcionario_exemplo):
        endereco_formatado = funcionario_exemplo.formatar_endereco()
        assert endereco_formatado == "Rua das Flores, 123, São Paulo - CEP: 01234-567"

    def test_calcular_salario_mensal(self, funcionario_exemplo):
        salario = funcionario_exemplo.calcular_salario_mensal()
        assert salario == 8800.0  # 8000 + 10% bonus

    def test_calcular_salario_mensal_valor_diferente(self):
        funcionario = Funcionario(
            "Maria Santos",
            "Analista",
            5000.0,
            "Av. Brasil, 456",
            "Rio de Janeiro",
            "20000-000"
        )
        salario = funcionario.calcular_salario_mensal()
        assert salario == 5500.0  # 5000 + 10% bonus

    def test_gerar_relatorio_html(self, funcionario_exemplo):
        relatorio = funcionario_exemplo.gerar_relatorio_html()
        assert '<h1>Relatório de Funcionário</h1>' in relatorio
        assert 'João Silva' in relatorio
        assert 'Desenvolvedor Sênior' in relatorio
        assert 'R$ 8800.00' in relatorio
        assert 'Rua das Flores, 123, São Paulo - CEP: 01234-567' in relatorio
        assert relatorio.startswith('<div>')
        assert relatorio.endswith('</div>')

    def test_getters(self, funcionario_exemplo):
        assert funcionario_exemplo.get_nome() == "João Silva"
        assert funcionario_exemplo.get_cargo() == "Desenvolvedor Sênior"
        assert funcionario_exemplo.get_salario_base() == 8000.0


if __name__ == "__main__":
    pytest.main([__file__])
