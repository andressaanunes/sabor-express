class contaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    def __str__(self):
        return f'Titular: {self._titular.ljust(25)} | Saldo: {str(self._saldo).ljust(25)}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta1 = contaBancaria("João", 1000)
conta2 = contaBancaria("Maria", 2000)

print(conta1)
print(conta2)
    
conta3 = contaBancaria("José", 3000)
print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
contaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa? {conta3._ativo}')

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
        
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f'Titular da conta 4: {conta4.titular}')

class ClientBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco   
        self._cpf = cpf
        self._profissao = profissao
        
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
        
cliente1 = ClientBanco("Fernanda", 25, "Rua 1", "123.456.789-00", "Desenvolvedora")
cliente2 = ClientBanco("João", 30, "Rua 2", "987.654.321-00", "Analista")
cliente3 = ClientBanco("Maria", 35, "Rua 3", "456.789.123-00", "Gerente")

conta_cliente1 = ClientBanco.criar_conta("Fernanda", 1500)
print(f'Conta de {conta_cliente1.titular} criada com sucesso! Saldo inicial: {conta_cliente1.saldo}')