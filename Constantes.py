dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port= '5432'

QUERY_CLIENTES_ACTIVOS = 'SELECT * FROM scexamen.personas  WHERE estado = 1'
QUERY_VUELOS_BY_PASAJERO = ('SELECT c.nombre as "Ciudad origen", c2.nombre as "Ciudad destino" FROM scexamen.vuelos v JOIN scexamen.usuariosvuelo uv ON v.id=uv.idvuelo JOIN scexamen.personas p ON p.id=uv.idpasajero '
                            'JOIN scexamen.ciudades c ON c.id=v.idciudadorigen JOIN scexamen.ciudades c2 ON c2.id=v.idciudaddestino WHERE p.id=%(id_pasajero)s')
QUERY_VUELOS = 'SELECT * FROM scexamen.vuelos'
QUERY_DATOS_VUELO_ID = ('SELECT p.nombre, p.apellidos, c.nombre as "Ciudad origen", c2.nombre as "Ciudad destino", uv.preciobillete as "Precio_billete" FROM scexamen.vuelos v JOIN scexamen.usuariosvuelo uv ON v.id=uv.idvuelo JOIN scexamen.personas p ON p.id=uv.idpasajero '
                            'JOIN scexamen.ciudades c ON c.id=v.idciudadorigen JOIN scexamen.ciudades c2 ON c2.id=v.idciudaddestino WHERE v.id=%(id_vuelo)s')
UPDATE_MAYORES = 'UPDATE scexamen.usuariosvuelo uv SET uv.mayorEdad="S" WHERE p.edad > 17 JOIN scexamen.personas ON p.id=uv.idpasajero'
UPDATE_MENORES = 'UPDATE scexamen.usuariosvuelo uv SET uv.mayorEdad="N" WHERE p.edad < 18 JOIN scexamen.personas ON p.id=uv.idpasajero'