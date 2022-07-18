from copy import deepcopy


class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    unique_ip = 0
    def __init__(self, buffer=[]):
        self.buffer = deepcopy(buffer)

    
    def __new__(cls, *args):
        obj = super().__new__(cls)
        obj.ip = cls.unique_ip
        cls.unique_ip += 1
        return obj
    
    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) 
        с указанным IP-адресом получателя (пакет отправляется роутеру и 
        сохраняется в его буфере - локальном свойстве buffer);
        """
        Router.obj.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было, 
        то возвращается пустой список) и очищает входной буфер;
        """
        last_buffer = self.buffer        
        self.buffer = []
        return last_buffer

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    obj = None

    def __new__(cls, *args):
        cls.obj = super().__new__(cls)
        return cls.obj

    # buffer пакетов
    def __init__(self, buffer=[], servers=[]):
        self.buffer = deepcopy(buffer)
        self.servers = deepcopy(servers)

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        self.servers.append(server)
    
    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        index = self.buffer.index(server)
        self.buffer = self.buffer[:index] + self.buffer[index+1:]
    
    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера 
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        servers = self.servers
        ips_and_servers = list(map(lambda x: (x,x.ip), servers))
        
        for data in self.buffer:
            
            # переменная для поиска
            # сервера совпадающего с сервером в отправялемых данных
            find_server = None

            # цикл для поиска сервера
            for server in servers:

                # если ip совпадают, то мы нашли сервер и вышли из поиска
                if server.ip == data.ip: 
                    find_server = server
                    break
            
            # к найденному серверу мы присоедини данные
            find_server.buffer.append(data)
        self.buffer = []
    

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(len(msg_lst_to))
