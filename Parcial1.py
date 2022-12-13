### Programacion de Computadoras IV
## Parcial 1
# Braulio Rodriguez 8-899-1093

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import Float
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456789@localhost/Parcial1')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

#Creacion de tabla para el inventario

class Inventario(Base):
    __tablename__ = 'Inventario'
    id = Column(Integer(), primary_key=True, AutoIncrement=True)
    Producto = Column(String(100))
    Cantidad = Column(Integer)
    Precio = Column(Float)
    Proveedor = Column(String(100))

#Funciones

def add(var1, var2, var3, var4):
    add = Inventario(Producto=var1, Cantidad=var2, Precio=var3, Proveedor=var4)
    session.add(add)
    session.commit()


def edit(editar):
    edit = session.query(Inventario).get(editar)
    print("Que desea editar?")
    op = input("1.Precio     2.Cantidad     3.Proveedor")
    if op == 1:
        var5 = float(input("Ingrese el nuevo precio del producto: "))
        edit.Precio = var5
    elif op == 2:
        var5 = int(input("Ingrese la nueva cantidad del producto: "))
        edit.Cantidad = var5
    elif op == 3:
        var5 = input("Ingrese el nuevo proveedor del producto: ")
        edit.Proveedor = var5
    else:
        print("Opcion Invalida")
    session.commit()


def delete(eliminar):
    session.query(Inventario).filter(Inventario.Producto == eliminar).delete()
    session.commit()


def view():
    mostrar = session.query(Inventario).all()
    for stock in mostrar:
        print("Producto: ", + stock.Producto +
              " Cantidad: ", str(stock.Cantidad) +
              " Precio: " + str(stock.Precio) +
              " Proveedor: " + stock.Proveedor)


def search(var6):
    buscar = session.query(Inventario).filter_by(Producto=var6)
    for productos in buscar:
        print("Producto: ", + productos.Producto +
              " Cantidad: ", str(productos.Cantidad) +
              " Precio: " + str(productos.Precio) +
              " Proveedor: " + productos.Proveedor)


# Menu de opciones
print("""
1. Insertar
2. Editar
3. Borrar
4. Visualizar
5. Buscar
6. Salir
""")

resp = 1
while(resp == 1):
    opcion = input("Ingrese una opcion")

    if (opcion == 1):
        print("Ingresar nuevo producto en el inventario")
        var1 = input("Ingrese el nombre del producto: ")
        var2 = input("Ingrese la cantidad: ")
        var3 = input("Ingrese el precio: ")
        var4 = input("Ingrese el nombre del proveedor: ")
        add(var1, var2, var3, var4)

    elif (opcion == 2):
        editar = input("Ingrese el Producto que desea editar: ")
        edit(editar)

    elif opcion == 3:
        print("Borre un registro")
        eliminar = input("Ingrese el Producto que desea eliminar del inventario")
        delete(eliminar)

    elif opcion == 4:
        view()

    elif opcion == 5:
        print("Buscar producto dentro del inventario")
        var6 = input("Ingrese el producto que desea buscar: ")
        search(var6)

    elif opcion == 6:
        break

    else:
        print("ERROR! OPCION INVALIDA")

    resp = input("Si desea continuar presione [1]")