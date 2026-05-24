from threading import Event, Thread


class AgendadorVisitas:
    def __init__(self, buscar_visitas_excedidas, ao_encontrar_visitas, primeiro_intervalo_segundos=2, intervalo_segundos=600):
        self.__buscar_visitas_excedidas = buscar_visitas_excedidas
        self.__ao_encontrar_visitas = ao_encontrar_visitas
        self.__primeiro_intervalo_segundos = primeiro_intervalo_segundos
        self.__intervalo_segundos = intervalo_segundos
        self.__stop_event = Event()
        self.__thread = Thread(target=self.__executar, daemon=True)

    def iniciar(self):
        if not self.__thread.is_alive():
            self.__thread.start()

    def parar(self):
        self.__stop_event.set()

    def __executar(self):
        intervalo_atual = self.__primeiro_intervalo_segundos

        while not self.__stop_event.wait(intervalo_atual):
            try:
                visitas_excedidas = self.__buscar_visitas_excedidas()
                if visitas_excedidas:
                    self.__ao_encontrar_visitas(visitas_excedidas)
            except Exception as e:
                print(f'Erro ao executar agendador de visitas: {e}')
            intervalo_atual = self.__intervalo_segundos
