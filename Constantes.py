dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port= '5432'

QUERY_CLIENTES_ACTIVOS = 'SELECT * FROM scexamen.personas  WHERE estado = 1'
QUERY_VUELOS_BY_PASAJERO = ('SELECT c.nombre as "Ciudad origen", c2.nombre as "Ciudad destino" FROM scexamen.vuelos v JOIN scexamen.usuariosvuelo uv ON v.id=uv.idvuelo JOIN scexamen.personas p ON p.id=uv.idpasajero '
                            'JOIN scexamen.ciudades c ON c.id=v.idciudadorigen JOIN scexamen.ciudades c2 ON c2.id=v.idciudaddestino WHERE p.id=%(id_pasajero)s')