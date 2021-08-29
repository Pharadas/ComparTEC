# firebase imports
import pyrebase
import uuid
import random
import os

nombres = [
	"Audrea Shadley",
	"Shantay Dyal",
	"Shery Bocanegra",
	"Twila Rosa",
	"Joetta Stahler",
	"Rubi Erb",
	"Kristian Buzard",
	"Lyman Najar",
	"Deloras Desilva",
	"Deeann Brunelle",
	"Francesca Mcbeath",
	"Kattie Crumley",
	"Ellie Pressey",
	"Macy Maisch",
	"Cecil Furlong",
	"Estrella Axelson",
	"Carolynn Cumbee",
	"Obdulia Spagnuolo",
	"Rich Kabel",
	"Dionna Eutsey",
	"Nu Densmore",
	"Lila Murrell",
	"Pete Bosak",
	"Ashely Knisely",
	"Dick Look",
	"Gordon Cross",
	"Johnathan Day",
	"Shanti Patino",
	"Fatima Storm",
	"Joye Selley",
	"Shela Morningstar",
	"Dexter Looby",
	"Florinda Fuerst",
	"Tracey Portis",
	"Kiesha Rye",
	"Mariam Renegar",
	"Magdalene Auguste",
	"Neomi Villarreal",
	"Kourtney Tyrrell",
	"Bobbi Majeski",
	"Cherryl Cuevas",
	"Marion Singer",
	"Kay Salvador",
	"Nancee Coutu",
	"Dorathy Satter",
	"Euna Ronald",
	"Arlean Bartholomew",
	"Rey Jelley",
	"Clair Meacham",
	"Bree Osbourn"
]

materias = [
	"Acustica Aplicada",
	"Administracion",
	"Administración Configuració E Instalación De Sistemas",
	"Administracion de Bases de Datos",
	"Administracion de la Calidad Total",
	"Administracion de la Produccion",
	"Administracion De La Produccion II",
	"Administracion de Mantenimiento",
	"Administracion de Mtto.",
	"Administracion de negocios",
	"Administracion de Operaciones de Manufactura",
	"Administracion de Proyectos",
	"Administracion de Proyectos de Software",
	"Administracion de Recursos Humanos y Lab.",
	"Administracion de Recursos Humanos y Lab.",
	"Administracion de Sistemas de informacion",
	"Administracion de Sistemas de Informacion",
	"Administracion de Ventas",
	"Administracion del Mantenimiento Aeronautico",
	"Administracion Financiera",
	"Administración, Configuración E Instalación De Sistemas",
	"ADMON. DE LA PRODUCCION I",
	"Adquisicion De Datos",
	"Adquisicion de Datos y lab.",
	"Aerodinamica I",
	"Aerodinamica II",
	"Ahorro de Energia Electrica",
	"Ahorro de Energia Termica",
	"Aleaciones no Ferrosas",
	"Aleman Avanzado",
	"Algebra Lineal",
	"Algebra para Ingenieria",
	"Álgebra Para Ingeniería (Prepodeutico)",
	"Algoritmos",
	"Algoritmos computacionales",
	"Alumbrado e Instalaciones electricas",
	"Ambiente Aeroportuario",
	"Ambiente y Sustentabilidad",
	"Analisis de Elemento Finito",
	"Analisis de Fallas",
	"Analisis De Las Capas Atmosfericas",
	"Analisis de Sistemas",
	"Analisis de Sistemas de Produccion",
	"Analisis de variables en las telecomunicaciones",
	"Analisis de Vibracion Aplicado al Mantenimiento",
	"Analisis Numerico",
	"Analisis Y Deteccion De Fallas",
	"Antropologia social",
	"Antropologia Social Cultura Regional",
	"Aplicacion de las Tecnologias de Informacion",
	"Apreciacion de las Artes",
	"Arquitectura de Computadoras",
	"Arquitectura De Robots",
	"Arquitectura de Robots y Lab.",
	"Artes Escenicas Y Lab.",
	"Artes y Humanidades",
	"Aseguramiento De Calidad",
	"Aseguramiento de la Calidad",
	"Aseguramiento de la Calidad Aeronautica",
	"ATI",
	"Auditoria de Sistemas",
	"Auditoria Informatica",
	"Autocuidado y estilos de vida saludable",
	"Automatizacion",
	"Automatizacion de Sistemas",
	"Automatizacion Industrial",
	"Automatizacion y control de sistemas dinamicos y Laboratorio",
	"Automatizacion y Lab.",
	"Avionica"
	"CAD-CAM",
	"CAD/CAM",
	"CAD/CAM (Avanzado)",
	"CAD/CAM y lab.",
	"CAE",
	"CAE (Avanzado)",
	"Calculo Diferencial",
	"Calculo Integral",
	"Calidad Aplicada a Manufactura",
	"Calidad en el software",
	"Calidad Total en Manufactura",
	"Caracterizacion de Materiales",
	"Caracterizacion de Polimeros",
	"Cemento y Concreto",
	"Ceramicos",
	"Certificacion",
	"Ciencia de los Materiales",
	"Ciencias De Los Materiales",
	"Ciencias del Ambiente",
	"Circuitos analogos y digitales y Lab",
	"Circuitos Electricos",
	"Circuitos Electricos de C.A.",
	"Circuitos Electricos de C.D.",
	"Circuitos Electricos y Lab.",
	"Circuitos Electronicos y Electronica de Potencia",
	"Circuitos Magneticos Y Maquinas De C.D.",
	"Circuitos Magneticos Y Máquinas De CD",
	"CISCO I",
	"CISCO II",
	"CISCO III",
	"CISCO IV",
	"Civica Y Etica",
	"CNC en Tipos de Controles y Maquinas",
	"Codigos y especificaciones electricas",
	"Combustion",
	"Comercio Internacional",
	"Comercio Internacional Aeronautico",
	"Comercio Internacional Negocios",
	"Competencia Comunicativa",
	"Competencia Comunicativa en Ingles",
	"Comportamiento organizacional",
	"Computacion",
	"Computo integrado y Laboratorio",
	"Comunicacion Oral y escrita",
	"Comunicaciones Moviles y Lab.",
	"Comunicaciones Opticas",
	"Comunicaciones opticas y laboratorio",
	"Configuracion e Instalacion de Sistemas y Lab.",
	"Contabilidad Financiera",
	"Contabilidad y Costos",
	"Contexto Social de la Profesion",
	"Control Clasico",
	"Control Clasico y Lab.",
	"Control de Procesos y Lab.",
	"Control de Produccion",
	"Control de Robots y Lab.",
	"Control Digital y Lab.",
	"Control Electronico de Motores y Lab.",
	"Control Estadistico de la Calidad",
	"Control Estocastico",
	"Control Moderno Para Mecatronica",
	"Control Moderno para Mecatronica y Lab.",
	"Control Moderno y Lab.",
	"Control Numerico",
	"Control Numerico Directo (DNC) I",
	"Control Numerico Directo (DNC) II",
	"Control Optimo",
	"Controladores y microcontroladores programables y Lab",
	"Corrosion",
	"Costos Industriales",
	"Crecimiento Biologico y lab.",
	"CuItura de calidad",
	"Cultura Alemana",
	"Cultura de Calidad",
	"Cultura De La Lengua Inglesa",
	"Cultura Inglesa",
	"Cultura Regional",
	"Culturas indigenas mexicanas",
	"Curso De Inducción"
]


def init():
	firebaseConfig = {
		"apiKey": "AIzaSyDxEfgarWakUpDHQDu1Ws1BD1KzstbZSEY",
		"authDomain": "olas-f3ad7.firebaseapp.com",
		"databaseURL": "https://olas-f3ad7-default-rtdb.firebaseio.com/",
		"projectId": "olas-f3ad7",
		"storageBucket": "olas-f3ad7.appspot.com",
		"messagingSenderId": "184572869633",
		"appId": "1:184572869633:web:b52415d0c3b28302b31400",
		"measurementId": "G-BC3KP5NQ37"
	}

	firebase = pyrebase.initialize_app(firebaseConfig)

	global db
	db = firebase.database()

if __name__ == '__main__':
	init()

	items = db.get()
	if items.each() != None:
		for person in items.each():
			# print(person.val())
			print(person.key())
			db.child(person.key()).remove()
			# print(person.val())

	for i in range(50):
		data = {
			"user_id": str(uuid.uuid1()),
			"user_name": random.choice(nombres),
			"upload_date": str(random.randint(0, 1000)),
			"subject": random.choice(materias),
			"pdf_name": random.choice(os.listdir("C:/Users/david/Documents/repos/testthings/ComparTEC/testpdfs"))
		}

		print(data)
		db.push(data)

# # Push data
# data = {
# 	"name": "gaming",
# 	"age": "20"
# }

# db.push(data)
# user = db.child("-MiFKdihsM65wW-WWHeU").get()
# print(user.val())