class Funcionario:
    def __init__(self, nome: str, cargo: str, salario_base: float, rua: str, cidade: str, cep: str):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base
        self.rua = rua
        self.cidade = cidade
        self.cep = cep

    def formatar_endereco(self) -> str:
        return f"{self.rua}, {self.cidade} - CEP: {self.cep}"

    def calcular_salario_mensal(self) -> float:
        bonus = self.salario_base * 0.1
        return self.salario_base + bonus

    def gerar_relatorio_html(self) -> str:
        salario_calculado = self.calcular_salario_mensal()
        relatorio = '<div>'
        relatorio += '<h1>Relatório de Funcionário</h1>'
        relatorio += f'<p><strong>Nome:</strong> {self.nome}</p>'
        relatorio += f'<p><strong>Cargo:</strong> {self.cargo}</p>'
        relatorio += f'<p><strong>Salário Final:</strong> R$ {salario_calculado:.2f}</p>'
        relatorio += f'<p><strong>Endereço:</strong> {self.formatar_endereco()}</p>'
        relatorio += '</div>'
        return relatorio

    def get_nome(self) -> str:
        return self.nome

    def get_cargo(self) -> str:
        return self.cargo

    def get_salario_base(self) -> float:
        return self.salario_base


if __name__ == "__main__":
    funcionario = Funcionario(
        "João Silva",
        "Desenvolvedor Sênior",
        8000.0,
        "Rua das Flores, 123",
        "São Paulo",
        "01234-567"
    )

    print(funcionario.gerar_relatorio_html())
