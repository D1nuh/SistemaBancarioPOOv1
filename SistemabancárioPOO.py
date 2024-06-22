from abc import ABC

class cliente:
	def __init__(self, endereco):
		self.endereco = endereco
		self.conta = []
		
	def realizar_transacao(self, conta, transacao):
		transacao.registrar(conta)
		
	def adicionar_conta(self, conta):
		self.contas.append(conta)
	
class pessoaFisica(cliente):
	def cadastrar(self, cpf, nome, data_nascimento):
		super().__init__(endereco)
		self.cpf = cpf
		self.nome = nome
		self.data_nascimento
	
class conta:
	def __init__(self, numero, cliente):
		self.saldo = 0
		self.numero = numero
		self.agencia = "0001"
		self.cliente = cliente
		self.historico = Historico()
		
	@classmethod
	def nova_conta(cls, cliente, numero):
		return (cliente, numero)
	
	@property
	def saldo(self):
	    return self._saldo
	
	@property
	def numero(self):
	    return self._numero
	    
	@property
	def agencia(self):
		return self._agencia
    	
    @property
    def cliente(self):
    	return self._cliente
    	
    @property
    def historico(self):
    	return self._historico
		
	def sacar(self, valor):
		if self.sacar <= valor:
			print("Saque feito com sucesso")
			return True
			
		elif self.sacar > valor
			print("Saque falhou, saldo insuficiente!")
			
		else:
			print("Operação falhou, por favor verifique se a operação esta correta!")
			return False
		
class contaCorrente(conta):
	
	def limites(self, limite=500, limite_saques=3):
		super().__init__(numero, cliente)
		self.limite = limite
		self.limite_saques = limite_saques
		
		def sacar(self, valor):
			numero_saques = len(historico)
			
			if valor > self.limite:
				print("Saque falhou! O valor do saque excede o limite."")
				
			elif numero_saques >= self.limite_saques:
				print("Saldo falhou! Número máximo de saques excedido.")
				 else:
            return 
        def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
	
class Trasancao(ABC):
	
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_trans
            
		
class historico:
	self.historico = []
	def adicionar_transacao(self, transacao):
		self.historico = historico
		historico.append(transacao)	