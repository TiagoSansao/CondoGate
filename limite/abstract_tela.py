from abc import ABC, abstractmethod
import datetime
import FreeSimpleGUI as sg


class AbstractTela(ABC):
    ESTILO_JANELA = 'DarkGrey7'
    TITULO_BASE = 'CondoGate'

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init_opcoes(self):
        pass

    @abstractmethod
    def tela_opcoes(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def __validar_input_numerico(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            return True
        except ValueError:
            self.mostra_mensagem(f"O campo '{campo_legivel}' deve conter apenas números.", "erro")
            return False

    def __validar_input_obrigatorio(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            if valor == '':
                raise Exception(f"O campo '{campo_legivel}' é obrigatório.")
            return True
        except Exception as e:
            self.mostra_mensagem(e, "erro")
            return False

    def __validar_data(self, values: dict, chave: str, campo_legivel: str, formato="%d-%m-%Y") -> bool:
        valor = values.get(chave, "").strip()
        try:
            datetime.datetime.strptime(valor, formato)
            return True
        except ValueError:
            self.mostra_mensagem(f"Data inválida no campo '{campo_legivel}'. Formato esperado: DD-MM-YYYY", "erro")
            return False

    def __validar_input_float(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            float(valor)
            return True
        except ValueError:
            self.mostra_mensagem(f"O campo '{campo_legivel}' deve conter apenas números.", "erro")
            return False

    def __validar_input_cpf(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            if len(valor) != 11:
                raise ValueError
            return True
        except ValueError:
            self.mostra_mensagem(
                f"Valor incorreto! Formato esperado para '{campo_legivel}' deve conter exatamente 11 digitos.", "erro")
            return False

    def __validar_input_telefone(self, values: dict, chave: str, campo_legivel: str) -> bool:
        valor = values.get(chave, "").strip()
        try:
            int(valor)
            if len(valor) != 11:
                raise ValueError
            return True
        except ValueError:
            self.mostra_mensagem(
                f"Valor incorreto! Formato esperado para '{campo_legivel}' deve conter exatamente 11 digitos e sem espaços.\n Exemplo: 47988303706",
                "erro")
            return False

    def _validar_campos(self, values: dict, regras: list[tuple]) -> bool:
        for tipo, chave, campo_legivel in regras:
            if tipo.lower() == "obrigatorio" and not self.__validar_input_obrigatorio(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "numero" and not self.__validar_input_numerico(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "float" and not self.__validar_input_float(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "cpf" and not self.__validar_input_cpf(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "telefone" and not self.__validar_input_telefone(values, chave, campo_legivel):
                return False
            elif tipo.lower() == "data" and not self.__validar_data(values, chave, campo_legivel):
                return False
        return True

    def _extrair_valor(self, values: dict, chave: str) -> str:
        return values.get(chave, "").strip()

    def mostra_mensagem(self, mensagem: str, tipo: str = "info"):
        if tipo.lower() == "erro":
            sg.popup_error(mensagem, title="Erro")
        elif tipo.lower() == "sucesso":
            sg.popup_ok(mensagem, title="Sucesso")
        elif tipo.lower() == "aviso":
            sg.popup_yes_no(mensagem, title="Atenção")
        else:
            sg.popup(mensagem, title="Mensagem")

    def pega_cpf(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('SELECIONAR', font=("Helvica", 20), justification='center')],
                  [sg.Text('Digite o CPF', font=("Helvica", 15))],
                  [sg.Text('CPF:', size=(15, 1)),
                   sg.InputText(key='codigo', tooltip='Digite o CPF (ex: 12656972900)', size=(20, 1))],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.Close()
                return None

            if not self._validar_campos(values, [("obrigatorio", "codigo", "CPF"), ("cpf", "codigo", "CPF")]):
                continue

            window.Close()
            return str(self._extrair_valor(values, 'codigo'))

    def _pega_dados(self, schema):
        sg.theme(self.ESTILO_JANELA)

        layout = []
        layout.append([sg.Text(schema["title"], font=("Helvica", 20), justification="center")])

        validation_rules = []
        for field in schema["fieldList"]:
            layout.append([
                sg.Text(f'{field["label"]}:', size=(15, 1)),
                sg.InputText(key=field["key"], tooltip=field["tooltip"])
            ])

            if field["isRequired"]:
                validation_rules.append(("obrigatorio", field["key"], field["label"]))

            validation_rules.append((field["dataType"].value, field["key"], field["label"]))

        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])

        window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.Close()
                return None

            if not self._validar_campos(values, validation_rules):
                continue

            dados = {}

            for field in schema["fieldList"]:
                dados[field["key"]] = field["parseAs"](self._extrair_valor(values, field["key"]))

            window.Close()
            return dados
